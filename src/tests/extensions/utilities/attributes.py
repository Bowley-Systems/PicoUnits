# pylint: skip-file
""" Filename: attributes.py """

import unittest

from picounits.extensions.utilities.attributes import AttributeCheck
from picounits.utilities.errors import InvalidSectionError, InvalidKeyError


class TestAttributes(unittest.TestCase):
    """ Unit tests for the attribute check class """

    def test_is_valid_non_string(self):
        """ Test if the valid attribute check ignores non-strings """
        items = [1, 2.2, [1, 2, 3], ["hi", "b", "a"], None, True, {'a': 1}]

        for item in items:
            result = AttributeCheck._is_valid_attribute(item)
            self.assertFalse(result)

    def test_is_valid_identifier(self):
        """ Test valid python identifiers are accepted """
        items = ['foo', 'bar', '_private', 'my_var', 'CamelCase', 'x1', '_']

        for item in items:
            result = AttributeCheck._is_valid_attribute(item)
            self.assertTrue(result, f"Expected '{item}' to be valid")

    def test_is_valid_invalid_identifier(self):
        """ Test invalid python identifiers are rejected """
        items = ['1foo', 'my-var', 'my var', 'my.var', '', 'foo!', '@bar', '#tag']

        for item in items:
            result = AttributeCheck._is_valid_attribute(item)
            self.assertFalse(result)

    def test_is_keyword(self):
        """ Test python keywords are detected """
        items = [
            'and', 'as', 'assert', 'class', 'def', 'if', 'else',
            'for', 'while', 'return', 'True', 'False', 'None',
            'import', 'from', 'lambda', 'yield'
        ]

        for item in items:
            result = AttributeCheck._is_keyword(item)
            self.assertTrue(result)

    def test_is_not_keyword(self):
        """ Test non-keywords are not flagged as keywords """
        items = ['foo', 'bar', 'my_var', 'CamelCase', 'x1', '_']

        for item in items:
            result = AttributeCheck._is_keyword(item)
            self.assertFalse(result)

    def test_is_valid_attribute_keyword(self):
        """ Test that keywords are rejected as attributes """
        items = ['if', 'else', 'for', 'while', 'return', 'True', 'False', 'None']

        for item in items:
            result = AttributeCheck._is_valid_attribute(item)
            self.assertFalse(result)

    def test_validate_section_valid(self):
        """ Test valid section names pass validation """
        valid_sections = ['foo', 'bar', 'my_section', 'a.b', 'a.b.c', 'root.child.leaf']

        for section in valid_sections:
            try:
                AttributeCheck.validate_section(section, 0)
            except InvalidSectionError:
                self.fail()

    def test_validate_section_invalid(self):
        """ Test invalid section names raise InvalidSectionError """
        invalid_sections = [
            '1foo', 'my-var', 'my var', 'if', 'for', 'class', 'a.1b', 'a.if'
        ]

        for section in invalid_sections:
            with self.assertRaises(InvalidSectionError):
                AttributeCheck.validate_section(section, 0)

    def test_validate_key_valid(self):
        """ Test valid key names pass validation """
        valid_keys = ['foo', 'bar', 'my_key', 'CamelCase', 'x1', '_private']

        for key in valid_keys:
            try:
                AttributeCheck.validate_key(key, 0)
    
            except InvalidKeyError:
                self.fail()

    def test_validate_key_invalid(self):
        """ Test invalid key names raise InvalidKeyError """
        invalid_keys = [
            '1foo', 'my-var', 
            'my var', 'if', 
            'for', 'class', 
            'return', 'True', ''
        ]

        for key in invalid_keys:
            with self.assertRaises(InvalidKeyError):
                AttributeCheck.validate_key(key, 0)

    def test_validate_section_nested_dots(self):
        """ Test section validation with nested dot notation """
        # Valid nested sections
        valid = ['a.b.c.d', 'root.child.leaf']

        for section in valid:
            try:
                AttributeCheck.validate_section(section, 0)
    
            except InvalidSectionError:
                self.fail()

        # Invalid nested sections (one bad item)
        invalid = ['a.b.1c', 'a.if.c', 'a.b.class']
        for section in invalid:
            with self.assertRaises(InvalidSectionError):
                AttributeCheck.validate_section(section, 0)


if __name__ == '__main__':
    unittest.main()