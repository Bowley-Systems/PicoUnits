"""
Filename: dsl_parser.py

Description:
    Domain specific language parser for .ut (unit types)
    & .uiv (unit informed values) supports v1.0 and v1.1.
    
    Orchestrates deserialization, syntax analysis & 
    construction of units
"""


from __future__ import annotations
from pathlib import Path

from picounits.configuration.management import add_derived_units

from picounits.extensions.loader import Loader, DynamicLoader
from picounits.extensions.utilities.attributes import AttributeCheck
from picounits.extensions.core.syntax import ExtractPairs, QualityExtraction
from picounits.extensions.core.construction import ConstructQuantity, ConstructUnits

from picounits.extensions.utilities.errors import (
    ParserError, BackCompatibilityWarning, DuplicateSectionError
)

class Parser:
    """ Parser for .ut & .uiv file formats"""
    @classmethod
    def open(
        cls,
        filepath: Path | str,
        derived: Path | str = None,
        loader: Loader = DynamicLoader
    ) -> Loader:
        """ Parses .uiv file into an attribute tree structure """
        # Imports derived units if available
        if derived: cls.import_derived(derived)

        # Checks file type and reads lines into memory
        path = Path(filepath)
        if path.suffix.lower() != '.uiv':
            msg = f"Expected .uiv file, got {path.suffix}"
            raise ValueError(msg) from None

        lines = cls._read_lines(filepath)

        # Parses lines and filename into dynamic loader
        data = ParseLines.parse(lines, filepath)
        return loader(data, path.stem)

    @classmethod
    def import_derived(cls, filepath: Path | str) -> None:
        """ Parses .ut file and interprets unit strings into runtime registry """
        # Checks file type and read lines into memory
        derived_path = Path(filepath)
        if derived_path.suffix.lower() != '.ut':
            msg = f"Expected .ut file, got {derived_path.suffix}"
            raise ValueError(msg) from None

        lines = cls._read_lines(filepath)

        # State & derived unit dictionary
        status = False
        registry = {}

        # Constructs a registry of derived units
        for line in lines:
            if ParseLines.skip_comment(line):
                # Skips comments and empty lines
                continue

            # Splits the key and the value pairs into two strings
            result = ExtractPairs.extract_key_value(line)
            if not result:
                # If no key value pairs are extracted
                continue

            # Decomposes result into symbol & units
            symbol, unit_str = result
            if symbol.lower() == "format":
                # Updates the format state variable
                status = True
                continue

            # Constructs the unit
            registry[symbol] = ConstructUnits.construct_unit(unit_str)

        if not status:
            # Raises warning for missing 'format' key in version
            BackCompatibilityWarning(filepath).display()

        return add_derived_units(registry)

    @staticmethod
    def _read_lines(filepath_or_file: Path | str) ->  list[str]:
        """ Read lines from file path or file-like object. """
        # Convert to Path and validate
        filepath = Path(filepath_or_file)
        if not filepath.exists():
            msg = f"File not found: {filepath}"
            raise FileNotFoundError(msg) from None

        with filepath.open('r', encoding='utf-8') as f:
            return f.readlines()


class ParseLineState:
    """Stores the state of the line parser"""
    index: int = 0
    status: bool = False
    format_status: bool = False
    section: str | None = None
    content: dict | None = None


class ParseLines:
    """ Parse lines for .ut & .uiv files formats """
    @classmethod
    def parse(cls, lines: list[str], filepath: Path | str) -> dict:
        """ Parses and extracts logic from raw text into qualities """
        # Initializes the parser state
        state = ParseLineState()
        state.content = {}

        while state.index < len(lines):
            line = lines[state.index].strip()
            state.index += 1

            if cls.skip_comment(line):
                # Skips comments and empty lines
                continue

            is_section, name = cls._is_section(line)
            if is_section:
                # Ensures section is validate and not a duplication
                AttributeCheck.validate_section(name, state.index)
                if name in state.content:
                    # Section Duplication check
                    raise DuplicateSectionError(name, state.index)

                # Updates section based if identified
                state.section = name
                state.content[name] = {}

                # Updates compatibility
                state.status = False
                if name.lower() == "version": state.status = True
                continue

            # Attempts to parse key-value pair
            split_result = ExtractPairs.extract_key_value(line)
            if not split_result: continue

            if state.section is None:
                # Key-value pair found outside a parent section
                msg = f"key-value pair outside section {line!r}"
                raise ParserError(cls.__name__, msg) from None

            # Extracts key and ensure the key name is validate
            key, raw_value = split_result
            AttributeCheck.validate_key(key, state.index)

            if raw_value.startswith('['):
                # Handles multi-line values (lists that span multiple lines)
                raw_value = cls._handle_multi_line(state, lines, raw_value)

            # Checks for format section
            if state.status:
                if key.lower() == "format":
                    # If format is found within the [version] section
                    state.format_status = True

            # Extracts value, prefix and unit then constructs the quality
            value, prefix, unit = QualityExtraction.extract(raw_value)
            quantity = ConstructQuantity.quantity(value, prefix, unit)

            state.content[state.section][key] = quantity

        if not state.format_status:
            # Raises warning for missing 'format' key in version
            BackCompatibilityWarning(filepath).display()

        return state.content

    @classmethod
    def skip_comment(cls, line: str) -> bool:
        """ Check if line should be skipped (empty or comment) """
        line = line.strip()

        # Returns the result as a boolean
        return not line or line.startswith('#')

    @classmethod
    def _handle_multi_line(cls, state: ParseLineState, lines: list[str], raw_value: str) -> str:
        """ Handles multi-line values such as lists """
        open_count, close_count = cls._count_brackets(raw_value)

        # Collects lines until balanced
        while open_count > close_count and state.index < len(lines):
            # Removes whitespaces and adds next_line
            next_line = lines[state.index].strip()

            # Remove inline comments first
            if '#' in next_line: next_line = next_line[:next_line.index('#')].rstrip()

            state.index += 1
            raw_value += ' ' + next_line

            # Finds next open and close bracket and iterates values
            next_open, next_close = cls._count_brackets(next_line)
            open_count += next_open
            close_count += next_close

        return raw_value

    @classmethod
    def _count_brackets(cls, text: str) -> tuple[int, int]:
        """ Count opening and closing brackets """
        return text.count('['), text.count(']')

    @classmethod
    def _is_section(cls, line: str) -> tuple[bool, str]:
        """ Check if line defines a section [name] """
        line = line.strip()
        if line.startswith('[') and line.endswith(']'):
            # Returns the contents if true
            return True, line[1:-1]

        # Returns a empty string if false
        return False, ""
