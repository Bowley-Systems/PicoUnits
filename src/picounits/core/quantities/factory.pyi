# pylint: skip-file
"""
Filename: factory.pyi

Description:
    Static type hinting for the factory module.
"""

from enum import Enum
from dataclasses import dataclass
from typing import Callable, overload
from numpy import ndarray, integer, floating, complexfloating

from picounits.core.unit import Unit
from picounits.core.scales import PrefixScale
from picounits.core.quantities.scalars.types.complex import ComplexPacket
from picounits.core.quantities.scalars.types.real import RealPacket
from picounits.core.quantities.vectors.types.array import ArrayPacket


Packet = ComplexPacket | RealPacket | ArrayPacket


class Factory:

    @overload
    @classmethod
    def create(
        cls,
        value: complex | complexfloating,
        unit: Unit,
        prefix: PrefixScale | None = None,
    ) -> ComplexPacket: ...

    @overload
    @classmethod
    def create(
        cls,
        value: float | int | floating | integer,
        unit: Unit,
        prefix: PrefixScale | None = None,
    ) -> RealPacket: ...

    @overload
    @classmethod
    def create(
        cls,
        value: ndarray | list | tuple,
        unit: Unit,
        prefix: PrefixScale | None = None,
    ) -> ArrayPacket: ...

    @classmethod
    def reallocate(
        cls,
        op_name: str,
    ) -> Callable[[Callable], Callable]: ...

    @classmethod
    def category_check(
        cls,
        q1: Packet,
        q2: Packet,
    ) -> None: ...
    
    
class Operation(Enum):
    """ List of operations that transform dimensions. """
    DIVIDED         = "/"
    MULTIPLICATION  = "*"
    POWER           = "^"
    
    def __repr__(self) -> str: ...
    def __str__(self) -> str: ...
    

@dataclass(slots=True, frozen=True)
class PacketNode:
    """ The operational data behind the packet state """
    unit:       Unit
    operation:  Operation   |   None = None
    primary:    PacketNode  |   None = None
    secondary:  PacketNode  |   None = None