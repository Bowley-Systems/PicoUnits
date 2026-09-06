# pylint: skip-file
"""
Filename: lazy_imports.pyi

Description:
    Static type hinting for the lazy import module.
"""

from typing import Any
from picounits.core.quantities.factory import Factory


def import_factory(caller: str) -> type[Factory]: ...
def lazy_import(caller: str) -> Any: ...