# pylint: skip-file
"""
Filename: lazy_imports.pyi

Description:
    Static type hinting for the lazy import module.
"""

from picounits.core.quantities.factory import Factory

def import_factory(caller: str) -> type[Factory]: ...