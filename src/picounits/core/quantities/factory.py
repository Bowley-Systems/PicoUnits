"""
Filename: factory.py

Description:
    Defines the Quantity Factory Class, acts
    as a type caster for quantities within
    the agnostic functional endpoint methods.
    
    It also allows for operation chain analysis.
"""

from __future__ import annotations

from enum import Enum
from typing import Any, Callable
from dataclasses import dataclass
from numpy import ndarray, integer, floating, complexfloating
from picounits.core.quantities.packet import Packet

from picounits.utilities.lazy_imports import lazy_import
from picounits.core.unit import Unit
from picounits.core.scales import PrefixScale


class Factory:
    """ Packet type casing factory for usage in agnostic functional methods """
    @classmethod
    def create(cls, value: Any, unit: Unit, prefix: PrefixScale = PrefixScale.BASE) -> Packet:
        """ Finds the type of the value and returns a casted packet """
        match value:
            case complex() | complexfloating():
                complex_packet = lazy_import(
                    "picounits.core.quantities.scalars.types.complex", 
                    "ComplexPacket", "Factory.create"
                )

                return complex_packet(value, unit, prefix)

            case float() | int() | integer() | floating():
                real_packet = lazy_import(
                    "picounits.core.quantities.scalars.types.real", 
                    "RealPacket", "Factory.create"
                )
                return real_packet(value, unit, prefix)

            case tuple() | list() | ndarray():
                array_packet = lazy_import(
                    "picounits.core.quantities.vectors.types.array",
                    "ArrayPacket", "Factory.create"
                )
                return array_packet(value, unit, prefix)

            case _:
                msg = f"No Packet for this value type: {type(value)}"
                raise TypeError(msg)

    @classmethod
    def reallocate(cls, op_name: str) -> Callable:
        """ Reallocate arithmetic or transcendental methods when packets are not similar types. """

        def decorator(method: Callable) -> Callable:
            def wrapper(q1: Packet, q2: Packet) -> Callable:
                """ Promotes methods if they dont have the same parents """
                q1_parents = q1.__class__.__bases__[0]
                q2_parents = q2.__class__.__bases__[0]
                if q1_parents == q2_parents:
                    # Simple pass through if same class has the same parent
                    return method(q1, q2)

                # Initialization due to circular import of literals
                domain_priority = lazy_import(
                    "picounits.core.quantities.priority",
                    "DOMAIN_PRIORITY", "Factory.reallocate"
                )

                # Gets priority of each packet_type
                p1 = domain_priority.get(q1_parents, 0)
                p2 = domain_priority.get(q2_parents, 0)

                # Finds the native operator for these packets
                winner = q1 if p1 >= p2 else q2
                loser = q2 if winner is q1 else q1

                if q1.__class__ == winner.__class__:
                    # If winner is q1 than return the method
                    return method(q1, q2)

                # Reallocate this result to another arithmetic router
                return getattr(winner, op_name)(loser)
            return wrapper
        return decorator

    @classmethod
    def category_check(cls, q1: Packet, q2: Packet) -> None:
        """ Checks if two packets are from the same category """
        q1_parents = q1.__class__.__bases__[0]
        q2_parents = q2.__class__.__bases__[0]

        if q1_parents == q2_parents:
            return

        msg = f"{q1!r} is not in the same quality category as {q2!r}"
        raise TypeError(msg)

    @classmethod
    def chain(cls, operation: Operation) -> Packet:
        """ A decorator; it maps operation chains. """
        def decorator(func: Callable[[Packet, Packet], Packet]) -> Callable:
            def wrapper(q1: Packet, q2: Packet) -> Packet:
                # Extracts the pre-operation state from metadata
                primary, secondary = q1.meta, q2.meta

                # Runs the wrapped function & applies state
                result = func(q1, q2)
                result.meta = PacketNode(result.unit, operation, primary, secondary)
                return result

            return wrapper
        return decorator

    @classmethod
    def packet_info(cls, packet: Packet) -> None:
        """ Displays the packet construction history """
        node = packet.meta
        print(node)

    @classmethod
    def _print_node(cls, node: PacketNode, prefix: str = "", is_last: bool = True) -> None:
        """ Prints the node information in a structured tree """
        if not node:
            # if last node had either no primary or secondary nodes.
            return

        # Choose the branch connector & formats/print entry
        connector = "└── " if is_last else "├── "

        op_str = f"[{node.operation}]" if node.operation else "[Base Unit]"
        print(f"{prefix}{connector} Unit: {node.unit}{op_str}")

        # Collect child nodes (primary and secondary)
        children = [c for c in (node.primary, node.secondary) if c is not None]

        # Recursively print children with proper indentation lines
        for index, child in enumerate(children):
            child_is_last = index == len(children) - 1
            extension = "    " if is_last else "│   "
            cls.node_info(child, prefix + extension, child_is_last)


class Operation(Enum):
    """ List of operations that transform dimensions. """
    DIVIDED         = "/"
    MULTIPLICATION  = "*"
    POWER           = "^"

    def __repr__(self) -> str: return self.value
    def __str__(self) -> str: return self.value


@dataclass(slots=True, frozen=True)
class PacketNode:
    """ The operational data behind the packet state """
    unit:       Unit
    operation:  Operation   |   None = None
    primary:    PacketNode  |   None = None
    secondary:  PacketNode  |   None = None

    @property
    def name(self) -> str:
        """ Constructs a name based on attributes """
        primary = True if isinstance(self.primary, PacketNode) else False
        secondary = True if isinstance(self.secondary, PacketNode) else False

        return f"<[{self.unit}, {self.operation}], Primary: {primary}, Secondary: {secondary}>"

    def __repr__(self) -> str: return self.name
    def __str__(self) -> str: return self.name
