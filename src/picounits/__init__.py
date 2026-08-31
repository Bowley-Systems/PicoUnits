# pylint: skip-file
# picounits/__init__.py

from typing import Any

from picounits.extensions.parser import Parser
from picounits.extensions.loader import DynamicLoader

from picounits.constants import *
from picounits.core.quantities.validator import expects
from picounits.core.quantities.packet import Packet as Quantity

from picounits.configuration.management import reload_config

# Reloads the users .picounits configuration file.
reload_config()

# References for quantities when doing type hinting.
Q = Quantity
q = Quantity

_ = expects 

# LEGACY API - keep the old name for backward compatibility before 1.0.6
unit_validator = expects

# Parser & Loader import
_ = Parser
_ = DynamicLoader


class UnitError(TypeError):
    """ Exception for Unit Error """
    def __init__(self, error: str, messenger: str |  None = None):
        """ Returns a custom error message """
        if messenger:
            msg = f"{messenger!r} raised error: {error}."
        else:
            msg = f"Unit error occurred: {error}."
        super().__init__(msg)


def check_quantity(quantity: Quantity, ref: Quantity) -> None:
    """ Checks if the quantity has the correct reference unit """
    if not isinstance(quantity, Quantity):
        msg = f"{type(quantity)!r} is not a physical quantity object"
        raise UnitError(msg)

    if not isinstance(ref, (Unit, Quantity)):
        msg = f"Reference unit must be either a quantity or unit, not {type(ref)}"
        raise UnitError(msg)

    if isinstance(ref, Quantity):
        if quantity.unit != ref.unit:
            msg = f"Expected {ref.unit!r}, got {quantity.unit!r}"
            raise UnitError(msg)

    if isinstance(ref, Unit):
        if quantity.unit != ref:
            msg = f"Expected {ref!r}, got {quantity.unit!r}"
            raise UnitError(msg)


def strip_quantity(quantity: Quantity, reference: Quantity) -> Any:
    """ Strips quantity from value returns raw value """
    check_quantity(quantity, reference)

    return quantity.value


# API Promises
__all__ = [
    # API
    "UnitError",
    "DynamicLoader",
    "strip_quantity",
    "check_quantity",
    "Parser",
    "Quantity",
    "Q",
    "q",
    "expects"
    
    # Scales
    "GIGA", "giga",
    "MEGA", "mega",
    "KILO", "kilo",
    "CENTI", "centi",
    "MILLI", "milli",
    "MICRO", "micro",
    "NANO", "nano",
    "PICO", "pico",
    
    # Fundamental dimensions
    "TIME", "time",
    "LENGTH", "length",
    "MASS", "mass",
    "CURRENT", "current",
    "TEMPERATURE", "temperature",
    "AMOUNT", "amount",
    "LUMINOSITY", "luminosity",
    "DIMENSIONLESS", "dimensionless",
    "NULLSET", "nullset",
    
    # Geometric quantities
    "AREA", "area",
    "VOLUME", "volume",
    
    # Kinematics
    "DISPLACEMENT", "displacement",
    "DISTANCE", "distance",
    "VELOCITY", "velocity",
    "SPEED", "speed",
    "ACCELERATION", "acceleration",
    "FREQUENCY", "frequency",
    "PERIOD", "period",
    "WAVENUMBER", "wavenumber",
    "ANGULAR_FREQUENCY", "angular_frequency",
    "PHASE", "phase",
    
    # Classical mechanics
    "FORCE", "force",
    "MOMENTUM", "momentum",
    "ANGULAR_MOMENTUM", "angular_momentum",
    "TORQUE", "torque",
    "ENERGY", "energy",
    "POWER", "power",
    "PRESSURE", "pressure",
    "DENSITY", "density",
    "WEIGHT", "weight",
    
    # Thermodynamics
    "ENTROPY", "entropy",
    "HEAT_CAPACITY", "heat_capacity",
    "SPECIFIC_HEAT", "specific_heat",
    "THERMAL_CONDUCTIVITY", "thermal_conductivity",
    "CONVECTION_COEFFICIENT", "convection_coefficient",
    "VOLUMETRIC_HEAT_CAPACITY", "volumetric_heat_capacity",
    "VOLUMETRIC_HEATING", "volumetric_heating",
    "DIFFUSIVITY", "diffusivity",
    
    # Electromagnetism
    "CHARGE", "charge",
    "ELECTRIC_FIELD", "electric_field",
    "ELECTRIC_POTENTIAL", "electric_potential",
    "VOLTAGE", "voltage",
    "RESISTANCE", "resistance",
    "CONDUCTANCE", "conductance",
    "CAPACITANCE", "capacitance",
    "IMPEDANCE", "impedance",
    "INDUCTANCE", "inductance",
    "MAGNETIC_FIELD", "magnetic_field",
    "MAGNETIC_FLUX", "magnetic_flux",
    "PERMEABILITY", "permeability",
    "FLUX_DENSITY", "flux_density",
    "COERCIVITY", "coercivity",
    "CONDUCTIVITY", "conductivity",
    
    # Waves & radiation
    "INTENSITY", "intensity",
    "LUMINANCE", "luminance",
    "RADIANT_FLUX", "radiant_flux",
    
    # Dimensionless quantities
    "STRAIN", "strain",
    "REFRACTIVE_INDEX", "refractive_index",
    "EFFICIENCY", "efficiency",
    "COEFFICIENT", "coefficient",
    "PROBABILITY", "probability",
]