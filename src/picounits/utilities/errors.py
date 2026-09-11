"""
Filename: errors.py

Description:
    Defines the runtime/parser errors classes 
    to ensure descriptive error messages.
"""

from abc import ABC, abstractmethod
from typing import Any
from pathlib import Path

# pylint: disable=line-too-long

# Generic Errors
class ParserError(ValueError):
    """ Exception for Parser errors when parsing """
    CODE = "PUPE001"

    def __init__(self, caller: str, error: str):
        """ Returns a custom error message """
        msg = f"[{self.CODE}] {caller!r} raised error: {error}. "
        super().__init__(msg)


class ParseListFailure(ValueError):
    """ Exception for failure of parsing lists """
    CODE = "PUPE002"

    def __init__(self, caller: Any, msg: str):
        """ Returns a failed casting error """
        msg = f"[{self.CODE}] {caller!r} raised error: {msg}. "
        super().__init__(msg)


class UnitError(TypeError):
    """ Exception for Unit Error """
    CODE = "PURE001"

    def __init__(self, error: str, messenger: str |  None = None):
        """ Returns a custom error message """
        if messenger:
            msg = f"[{self.CODE}] {messenger!r} raised error: {error}."
        else:
            msg = f"[{self.CODE}] Unit error occurred: {error}."

        super().__init__(msg)


class DimensionError(ValueError):
    """ Exception for unit error """
    CODE = "PURE002"

    def __init__(self, caller: str, message: str):
        """ Returns a custom error message for unit error """
        msg = f"[{self.CODE}]  {caller!r} {message}"
        super().__init__(msg)


# Specific errors
class LazyImportError(ImportError):
    """ Exception for failed lazy imports """
    CODE = "PURE003"

    def __init__(self, caller: str, module: str):
        """ Returns a custom error message for lazy imports """
        msg = f"[{self.CODE}]  Could not import '{module}' for '{caller}'. This usually means picounits was not installed correctly"
        super().__init__(msg)


class ExtensionNotFound(FileNotFoundError):
    """ Exception for failed lazy imports """
    CODE = "PURE004"

    def __init__(self, caller: str, extension: str):
        """ Returns a custom error message for file not found """
        msg = f"[{self.CODE}]  {caller!r} was unable to find '{extension}' file in the current working directory."
        super().__init__(msg)


class AttributeNotFound(AttributeError):
    """ Exception for attribute not found error """
    CODE = "PURE005"

    def __init__(self, attribute: str, path: str):
        """ Returns a custom error message """
        self.path = path
        self.attribute = attribute

        msg = f"[{self.CODE}]  {attribute!r} not found at {path!r} within loader tree"
        super().__init__(msg)


class InjectionError(Exception):
    """Raised when a value cannot be injected into a Loader tree."""
    CODE = "PURE006"

    def __init__(self, path: str, value: Any):
        self.path = path
        self.value = value

        msg = f"[{self.CODE}]  Failed to inject {value!r} at {path!r}"
        super().__init__(msg)


class UnknownOperator(ValueError):
    """ Exception for unknown operator during construction """
    CODE = "PUPE003"

    def __init__(self, char: str, operator: str):
        """ Returns a custom error message """
        msg = f"[{self.CODE}] {char!r} is an unknown operator. Supported operators are {operator!r}"
        super().__init__(msg)


class UnknownPrefix(ValueError):
    """ Exception for unknown prefix during construction """
    CODE = "PUPE004"

    def __init__(self, char: str, prefixes: str):
        """ Returns a custom error message """
        msg = f"[{self.CODE}] {char!r} is an prefix. Supported prefix are {prefixes!r}"
        super().__init__(msg)


class FailedCasting(ValueError):
    """ Exception for failure during casting """
    CODE = "PUPE005"

    def __init__(self, text: Any, error: str):
        """ Returns a failed casting error """
        msg = f"[{self.CODE}] Failed to cast {text!r} as python primitive, error: {error!r}"
        super().__init__(msg)


class ColumnAttribute(AttributeError):
    """ Exception for column attribute out of range"""
    CODE = "PUPE006"

    def __init__(self, attribute_type: Any):
        """ Returns a column attribute error """
        msg = f"[{self.CODE}] Failed to construct nested array due to {attribute_type!r} out of range"
        super().__init__(msg)


class UnsupportedType(ValueError):
    """ Exception for unsupported type during unit construction"""
    CODE = "PUPE007"

    def __init__(self, value_type: Any):
        """ Returns a column attribute error """
        msg = f"[{self.CODE}] Failed to construct unit due to unsupported type: {value_type!r}"
        super().__init__(msg)


class UnbalancedDepth(Exception):
    """ Exception for unbalanced parentheses or brackets when parsing """
    CODE = "PUPE008"

    def __init__(self, caller: str, line: str, symbol: str):
        """ Returns a unbalanced depth error """
        msg = f"[{self.CODE}] {caller!r} attempted to parse {line!r} but depth of {symbol!r} is unbalanced."
        super().__init__(msg)


class InvalidSectionError(ValueError):
    """ Exception for malformed section header """
    CODE = "PUP009"

    def __init__(self, section: str, line: str):
        """ Returns a malformed section error """
        msg = f"[{self.CODE}] Malformed section header: {section!r} at line {line!r}. Must be a validate section."
        super().__init__(msg)


class DuplicateSectionError(ValueError):
    """ Exception for duplicate section in file """
    CODE = "PUPE010"

    def __init__(self, section: str, line: int):
        """ Returns a duplicate section error """
        msg = f"[{self.CODE}] Duplicate section {section!r} at line: {line!r}. Sections must be unique."
        super().__init__(msg)


class InvalidKeyError(ValueError):
    """ Exception for malformed key-value pair """
    CODE = "PUPE011"

    def __init__(self, line: str, line_num: int):
        """ Returns a malformed key-value error """
        msg = f"[{self.CODE}] Malformed key-value pair at line {line_num}: {line!r}. Must be validate key."
        super().__init__(msg)


class UnitNotFoundError(ValueError):
    """ Exception for referenced unit that doesn't exist """
    CODE = "PUPE012"

    def __init__(self, unit: str, available_units: list):
        """ Returns a unit not found error """
        available = ", ".join(available_units) if available_units else "none defined"
        msg = f"[{self.CODE}] Unit {unit!r} not found. Available units: {available}"
        super().__init__(msg)


# Notifications / Warning classes
class ParserNotification(ABC):
    """ Abstract base class for parser notifications messages """
    CODE: str = ""      # Placeholder

    @abstractmethod
    def __init__(self):
        """ Initializes the class and sets the message variable """
        self.message: str = ""

    def display(self) -> None:
        """ Prints the message """
        print(self.message)

    def __str__(self) -> str:
        """ returns the str(message) """
        return str(self.message)


class BackCompatibilityWarning(ParserNotification):
    """ Warning for missing 'format' key in version """
    CODE = "PUPW001"

    def __init__(self, file_path: str):
        """ Returns a compatibility warning """
        filename = Path(file_path).name
        note = f"Tip: {filename} missing 'format' key."
        compatibility = "Add 'version.format: 0.1.1' for compatibility."

        # Sets the message for display
        self.message = f"[{self.CODE}] {note} {compatibility}"


class UnitFrameCompatibilityWarning(ParserNotification):
    """ Warning for missing 'unit_frame' in version """
    CODE = "PUPW002"

    def __init__(self, filepath: str):
        filename = Path(filepath).name
        note = f"Tip: {filename} missing 'unit_frame'."
        improvement = "Add 'version.unit_frame: (your_derived_units).ut'."

        # Sets the message for display
        self.message = f"[{self.CODE}] {note} {improvement}"
