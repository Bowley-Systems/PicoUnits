# pylint: skip-file
# picounits\configuration\picounits.py

DEFAULT_CONFIG = """
# ==============================================================
# PicoUnits project configuration
#
# Drop this file or run `picounits generate` in your project root.
#
# NOTE:
#   PicoUnits uses a fixed set of fundamental dimensions.
#   Dimensions cannot be added or removed, but their symbols and
#   ordering may be customized.
# ==============================================================

[symbols]
# Change the symbol used to represent each fundamental dimension.
TIME: s
LENGTH: m
MASS: kg
CURRENT: A
TEMPERATURE: K
AMOUNT: mol
LUMINOSITY: cd
DIMENSIONLESS: ∅

[order]
# Change the order in which dimensions are represented.
TIME: 0
LENGTH: 1
MASS: 2
CURRENT: 3
TEMPERATURE: 4
AMOUNT: 5
LUMINOSITY: 6
DIMENSIONLESS: 7
""".lstrip()


# Package defaults symbols and order (SI)
DEFAULT_SYMBOLS = {
    "TIME":                 "s",
    "LENGTH":               "m",
    "MASS":                 "kg",
    "CURRENT":              "A",
    "TEMPERATURE":          "K",
    "AMOUNT":               "mol",
    "LUMINOSITY":           "cd",
    "DIMENSIONLESS":        "∅",
}


DEFAULT_ORDER = {
    "MASS":             0,
    "LENGTH":           1,
    "TIME":             2,
    "CURRENT":          3,
    "TEMPERATURE":      4,
    "AMOUNT":           5,
    "LUMINOSITY":       6,
    "DIMENSIONLESS":    7,
}


# Dimension maximum exponent size
MAX_EXPONENT = 10
DEFAULT_SIGNIFICANT_FIGURES = 3
