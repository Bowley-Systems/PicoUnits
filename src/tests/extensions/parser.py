# pylint: skip-file
""" Filename: parser.py """

import unittest
from pathlib import Path
from tempfile import TemporaryDirectory

from picounits.extensions.parser import Parser, ParseLines, ParseLineState


from picounits.extensions.loader import Loader, DynamicLoader
from picounits.utilities.errors import ParserError,DuplicateSectionError 


class TestParserOpen(unittest.TestCase):
    """ Unit tests for Parser.open """
    def setUp(self):
        """ Setup of a temporary directory for testing"""
        self.tmp = TemporaryDirectory()
        self.dir = Path(self.tmp.name)

    def tearDown(self):
        """ Cleans up temporary directory """
        self.tmp.cleanup()

    def _write(self, name: str, text: str) -> Path:
        """ Writes to a file within the temporary directory """
        path = self.dir / name
        path.write_text(text, encoding="utf-8")
        return path

    def test_open_wrong_suffix(self):
        """ Non-.uiv files raise ParserError """
        path = self._write("bad.txt", "[version]\nformat: 1.0\n")
        with self.assertRaises(ParserError):
            Parser.open(path)

    def test_open_missing_file(self):
        """ Missing file raises FileNotFoundError """
        with self.assertRaises(FileNotFoundError):
            Parser.open(self.dir / "nope.uiv")

    def test_open_returns_loader(self):
        """ Valid .uiv returns a Loader instance """
        path = self._write("ok.uiv", "[version]\nformat: 1.0\n\n[mass]\nthing: 10 m(kg)\n")

        result = Parser.open(path)
        self.assertIsInstance(result, Loader)

    def test_open_uses_default_loader(self):
        """ Default loader is DynamicLoader """
        path = self._write("ok.uiv", "[version]\nformat: 1.0\n\n[mass]\nthing: 10 (kg)\n")

        result = Parser.open(path)
        self.assertIsInstance(result, DynamicLoader)

    def test_open_accepts_string_path(self):
        """ String path is accepted """
        path = self._write("ok.uiv", "[version]\nformat: 1.0\n\n[mass]\nthing: 10 (kg)\n")

        result = Parser.open(str(path))
        self.assertIsInstance(result, Loader)


class TestParserImportDerived(unittest.TestCase):
    """ Unit tests for Parser.import_derived """

    def setUp(self):
        """ Setup of a temporary directory for testing"""
        self.tmp = TemporaryDirectory()
        self.dir = Path(self.tmp.name)

    def tearDown(self):
        """ Cleans up temporary directory """
        self.tmp.cleanup()

    def _write(self, name: str, text: str) -> Path:
        """ Writes to a file within the temporary directory """
        path = self.dir / name
        path.write_text(text, encoding="utf-8")
        return path

    def test_import_derived_wrong_suffix(self):
        """ Non-.ut files raise ParserError """
        path = self._write("bad.uiv", "[version]\nformat: 1.0\n")
        with self.assertRaises(ParserError):
            Parser.import_derived(path)


class TestParserReadLines(unittest.TestCase):
    """ Unit tests for Parser._read_lines """

    def setUp(self):
        """ Setup of a temporary directory for testing"""
        self.tmp = TemporaryDirectory()
        self.dir = Path(self.tmp.name)

    def tearDown(self):
        """ Cleans up temporary directory """
        self.tmp.cleanup()

    def test_read_lines_missing(self):
        """ Missing file raises FileNotFoundError """
        with self.assertRaises(FileNotFoundError):
            Parser._read_lines(self.dir / "missing.txt")

    def test_read_lines_returns_list(self):
        """ Returns list of lines """
        path = self.dir / "file.txt"
        path.write_text("a\nb\nc\n", encoding="utf-8")

        result = Parser._read_lines(path)
        self.assertEqual(result, ["a\n", "b\n", "c\n"])


class TestParseLines(unittest.TestCase):
    """ Unit tests for ParseLines """
    def test_parse_empty_lines(self):
        """ Empty input returns empty dict """
        result = ParseLines.parse([], "fake.uiv")
        self.assertEqual(result, {})

    def test_parse_simple_section(self):
        """ Parses a simple section with one value """
        lines = ["[version]\n", "format: 1.0\n", "[mass]\n", "thing: 10 (kg)\n"]

        result = ParseLines.parse(lines, "fake.uiv")
        self.assertIn("version", result)
        self.assertIn("mass", result)
        self.assertIn("thing", result["mass"])

    def test_parse_duplicate_section(self):
        """ Duplicate section raises DuplicateSectionError """
        lines = ["[version]\n", "format: 1.0\n", "[mass]\n", "thing: 10 (kg)\n", "[mass]\n", "other: 1 (kg)\n"]

        with self.assertRaises(DuplicateSectionError):
            ParseLines.parse(lines, "fake.uiv")

    def test_parse_key_outside_section(self):
        """ Key-value pair outside a section raises ParserError """
        lines = ["thing: 10 (kg)\n"]

        with self.assertRaises(ParserError):
            ParseLines.parse(lines, "fake.uiv")

    def test_parse_invalid_key(self):
        """ Invalid key name raises InvalidKeyError """
        from picounits.utilities.errors import InvalidKeyError
        lines = ["[version]\n", "format: 1.0\n", "[mass]\n", "if: 10 (kg)\n"]

        with self.assertRaises(InvalidKeyError):
            ParseLines.parse(lines, "fake.uiv")

    def test_parse_multi_line_list(self):
        """ Multi-line list values are joined """
        lines = ["[version]\n", "format: 1.0\n", "[data]\n",  "values: [1, 2,\n", "3, 4] (kg)\n"]
    
        result = ParseLines.parse(lines, "fake.uiv")
        self.assertIn("values", result["data"])


class TestParseLinesHelpers(unittest.TestCase):
    """ Unit tests for ParseLines static helpers """
    def test_skip_comment_empty(self):
        """ Empty lines are skipped """
        self.assertTrue(ParseLines.skip_comment(""))
        self.assertTrue(ParseLines.skip_comment("   "))

    def test_skip_comment_hash(self):
        """ Comment lines are skipped """
        self.assertTrue(ParseLines.skip_comment("# hello"))
        self.assertTrue(ParseLines.skip_comment("   # indented"))

    def test_skip_comment_content(self):
        """ Content lines are not skipped """
        self.assertFalse(ParseLines.skip_comment("thing: 10"))
        self.assertFalse(ParseLines.skip_comment("[section]"))

    def test_count_brackets(self):
        """ Counts open and close brackets """
        self.assertEqual(ParseLines._count_brackets("[a]"), (1, 1))
        self.assertEqual(ParseLines._count_brackets("[[a]]"), (2, 2))
        self.assertEqual(ParseLines._count_brackets("none"), (0, 0))

    def test_is_section_true(self):
        """ Section line is detected """
        result, name = ParseLines._is_section("[version]")
        self.assertTrue(result)
        self.assertEqual(name, "version")

    def test_is_section_false(self):
        """ Non-section line returns False """
        result, name = ParseLines._is_section("thing: 10")
        self.assertFalse(result)
        self.assertEqual(name, "")

    def test_handle_multi_line_with_comment(self):
        """ Inline comments in continuation lines are stripped """
        state = ParseLineState()
        state.index = 1
        lines = ["[1, 2, # comment", "3, 4] # hello \n"]

        result = ParseLines._handle_multi_line(state, lines, lines[0])
        self.assertNotIn("#", result)
        self.assertIn("3, 4]", result)


if __name__ == '__main__':
    unittest.main()