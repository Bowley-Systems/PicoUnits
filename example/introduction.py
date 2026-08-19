# pylint: skip-file
"""
Filename: Introduction.py

Descriptions:
    Introduces the mechanics of picounits via a few examples

    NOTE: Assumes your base dimensions are SI metric for (notation)
"""

def next_step(title: str, first: bool = False):
    """ Helper functions for examples (Doesn't relate to library) """
    notation = "" if first else "\n"
    print(f"{notation}{'='*10} {title} {'='*10}")
    input(">>> Press Enter to see this example...")


# ============ Set a value:unit pair ============

next_step("0a: How to set a prefix(value:unit) pair", True)

# Import the dimension & prefix you want to use
from picounits import LENGTH, MILLI

# Define a value:unit pair as (value, prefix, length)
william_height_m = 1.75 * LENGTH
william_height_mm = 1750 * MILLI * LENGTH

print(f"William (defined as m):  {william_height_m}")
print(f"William (defined as mm): {william_height_mm}")
print("Result: Picounits normalized both to 1.75 meters.")


next_step("0b: Due to prefix(value:unit) prefixes don't carry")

# Import the dimension & prefix you want to use
from picounits import LENGTH, MILLI

# Square with length and height
square_length = 10 * MILLI * LENGTH
square_width = 10 * MILLI * LENGTH

# Calculates width
square_area = square_width * square_length

print(f"Square length: {square_length:.3f}, Square width: {square_width:.3f}")
print(f"Square Area: {square_area:.3f}")


# ============ Math Operations with value:units ============
next_step("1: Math Operations with value:units")

# Import the dimension & prefix you want to use
from picounits import MASS, FORCE, KILO

lily_mass = 62.5 * MASS
car_mass = 1.5 * KILO * MASS

force_on_lily = 100 * FORCE
force_on_car = -force_on_lily

lily_acceleration = force_on_lily / lily_mass
car_acceleration = force_on_car / car_mass

print(f"Lily Acceleration: {lily_acceleration:.3f}")
print(f"Car Acceleration:   {car_acceleration:.3f}")


# ============ Validation functions ============
next_step("2: Validates the output is the correct dimension")

# Import the quantity for type hinting, the validator for checking and dimensions to use
from picounits import Q, expects, CURRENT, VOLTAGE, RESISTANCE

@expects(RESISTANCE)
def calculate_voltage(current: Q, resistance: Q) -> Q:
    """ Calculates the voltage across an element based on v=ir (ohm's relation) """
    return current * resistance

try:
    print("Attempting calculate_voltage(10 A, 10 V)....")
    calculate_voltage(10 * CURRENT, 10 * VOLTAGE)

except Exception as err:
    print(f"`expects` catches dimension errors before they propagate: {err}")

print("Re-entry with calculate_voltage(10 A, 10 Ω)....")
print(f"Element voltage: {calculate_voltage(10 * CURRENT, 10 * RESISTANCE)}")


# ============ Example 4: Complex Numbers & SUVAT ============
next_step("4: Physics with Complex Numbers (SUVAT)")

from picounits import Q, expects, VELOCITY, TIME

@expects(VELOCITY)
def suvat(initial_velocity: Q, acceleration: Q, distance: Q) -> Q:
    """" Calculates the velocity after accelerating for a specific distance """
    square = initial_velocity ** 2 + 2 * acceleration * distance
    return square ** 0.5

# Variables with complex components
initial_velocity = (10+100j) * VELOCITY
acceleration = 2.5 * LENGTH / TIME ** 2
displacement = (10+12j) * KILO * LENGTH

final_v = suvat(initial_velocity, acceleration, displacement)
print(f"Complex Velocity Result: {final_v:.3f}")


# ============ Example 5: Scaling Collections ============
next_step("5: Scaling Lists/Arrays with Units")

from picounits import VOLTAGE, KILO, VOLTAGE

# You can scale a list of values directly by a unit
voltages = [1, 2, 3] * VOLTAGE
high_voltages = [10, 20, 30] * KILO * VOLTAGE

print(f"Standard Voltages: {voltages}")
print(f"High Voltages (kV scaled): {high_voltages}")


# ============ Example 6: Kinetic Energy ============
next_step("6: Derived Energy Calculation")

from picounits import Q, expects, ENERGY

@expects(ENERGY)
def kinetic_energy(mass: Q, velocity: Q) -> Q:
    """ Calculates the kinetic energy of the projectile """
    return 0.5 * mass * velocity ** 2

Projectile_Mass = 12 * MASS
energy = kinetic_energy(Projectile_Mass, final_v)
print(f"Final Kinetic Energy: {energy:.3f}")


# ============ Example 7: Parser (introduction.uiv) ============
next_step("7: Parser (introduction.uiv)")

from math import pi
from pathlib import Path

from picounits.extensions import Parser

BASE_DIR = Path(__file__).parent
library = BASE_DIR / "introduction.uiv"

parameters = Parser.open(library)
parameters.info("library")

axial_length = parameters.pole.axial_length
outer_radius = parameters.pole.outer_radius
volume = pi * outer_radius ** 2 * axial_length

print("Calculating pole volume using parameters")
print(f"Pole Volume: {volume:.3f}")


# ============ Example 8: Parser Derived (derived.ut) ============
next_step("8: Parser (derived.ut)")

from pathlib import Path

from picounits import VOLTAGE, CURRENT, TIME
from picounits.extensions import Parser
from picounits.configuration.management import get_derived_units

BASE_DIR = Path(__file__).parent
derived_units = BASE_DIR / "derived.ut"

# Imports and displays derived units
Parser.import_derived(derived_units)
print(f"Derived Units: {get_derived_units()}")

voltage = 10 * VOLTAGE
current = 10 * CURRENT
power = 10 * VOLTAGE * CURRENT
energy = power * 1 * TIME

# The notion now has the derived units within `derived.ut` instead of fundamental notion
print(f"power: {power:.3f}, energy: {energy:.3f}")


# ============ Example 9: Debugging features ============
next_step("9: Debugging with derived units")

from picounits import KILO, POWER, TIME

# Defines some constants
power = 10 * KILO * POWER
energy = power * 1 * TIME

# Shows the different print outs
print(f"Derived Notion: {power:.3f}, {energy:.3f}")
print(f"Fundamental (.fundamental): {power.fundamental}, {energy.fundamental}")
print(f"Stripped (.stripped): {power.stripped}, {energy.stripped}")


# ============ Example 10: Validation Boundary ============
next_step("10: Validation Boundary Class")

from picounits import Q, strip_quantity
from picounits import VELOCITY, LENGTH, TIME, KILO

# Defines some constants
initial_velocity = 10 * VELOCITY
acceleration = 2.5 * LENGTH / TIME ** 2

print("[NOTE]: Recommend Review the implementation for this example: Line 185-222")
print(f"Qualities for `MyClass`: {initial_velocity:.3f}, {acceleration:.3f}")

class MyClass:
    def __init__(self, velocity: Q, acceleration: Q) -> None:
        """ Initializes the class and validates and strips units """
        # Constant variables
        self.velocity = strip_quantity(velocity, VELOCITY)
        self.acceleration = strip_quantity(acceleration, LENGTH / TIME ** 2)
        
    def calculate_vel(self, time: Q) -> Q:
        """ Calculates the velocity in raw floats """
        time = strip_quantity(time, TIME)
        
        # Raw floats (Intended for numerically heavy tasks)
        velocity = self.velocity + time * self.acceleration
    
        # Re-attach quality after computation
        return velocity * VELOCITY

Example = MyClass(initial_velocity, acceleration)

# Calculates the velocity at 10 units of time
time = 10 * TIME
output = Example.calculate_vel(time)

print(f"MyClass.velocity (Validated): {Example.velocity:.3f}, {Example.acceleration:.3f})")
print(f"Output of MyClass.calculate_vel(time): {output:.3f} @ {time:.3f}")

print("\n" + "="*30)
print("Tutorial Complete!")