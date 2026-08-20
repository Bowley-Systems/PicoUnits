"""
Filename: attributes.py

Description:
    Ensures that the attribute name
    for a section or key is valid within
    python
"""

from __future__ import annotations
from picounits.extensions.utilities.errors import InvalidSectionError, InvalidKeyError


class AttributeCheck:
    """ Validates a attribute key or section name is validate """
    @classmethod
    def validate_section(cls, section: str, index: int) -> None:
        """ Validates a section name for attribute tree """
        path_items = section.split('.')

        for item in path_items:
            if not cls._is_valid_attribute(item):
                # If item fails validation, raise error
                raise InvalidSectionError(section, index)

    @classmethod
    def validate_key(cls, key: str, index: int) -> None:
        """ Validates a key name for attribute tree """
        if not cls._is_valid_attribute(key):
            raise InvalidKeyError(key, index)

    @classmethod
    def _is_valid_attribute(cls, name: str) -> bool:
        """ Checks if the name can be used as a Python attribute. """
        if not isinstance(name, str):
            return False

        return name.isidentifier() and not cls._is_keyword(name)

    @classmethod
    def _is_keyword(cls, name: str) -> bool:
        """ Checks if the name is a python keyword """
        return name in KEYWORDS


# Python keywords (as of Python 3.10+)
KEYWORDS = {
    'and', 'as', 'assert', 'async', 'await', 
    'break', 'case', 'class', 'continue', 
    'def', 'del', 'elif', 'else', 'except', 
    'False', 'finally', 'for', 'from', 'global',
    'if', 'import', 'in', 'is', 'lambda', 'match',
    'None', 'nonlocal', 'not', 'or', 'pass', 'raise', 
    'return', 'True', 'try', 'while', 'with', 'yield'
}
