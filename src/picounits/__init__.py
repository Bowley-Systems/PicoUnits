# pylint: skip-file
# picounits/__init__.py

from picounits.extensions.parser import Parser, resolve_derived
from picounits.extensions.loader import DynamicLoader

from picounits.constants import *
from picounits.utilities.validation import expects, strip_quantity, check_quantity
from picounits.core.quantities.packet import Packet as Quantity

from picounits.configuration.management import inject_unit_frame
from picounits.utilities.errors import UnitError

# Configuration / Management for forcing a unit frame at the application level.
_ = inject_unit_frame

# References for quantities when doing type hinting.
Q = Quantity
q = Quantity

# Validation
_, _ = strip_quantity, check_quantity
_ = UnitError

# LEGACY API - keep the old name for backward compatibility before 1.0.6
unit_validator = expects

# Parser & Loader import
_ = Parser
_ = DynamicLoader
_ = resolve_derived


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
    "expects",
    "inject_unit_frame",
    "ResolveDerived"
    
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