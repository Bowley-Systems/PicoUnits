# pylint: skip-file
"""
File: runner.py

Description:
    Main script to run all unit test modules within
    the picounits library. This includes unit modelling, 
    parser, dynamic-loader and configurations.
    
    NOTE: Reference commands:
    coverage run src/unit_test/runner.py
    coverage report -m
    
    
    NOTE: Unit Symbols required for this test suite in `.picounits`
    [symbols]
    # Change the name of fundamental dimensions
    time: s
    length: m
    mass: kg
    current: A
    TEMPERATURE: K
    amount: mol
    luminosity: cd
    dimensionless: ∅
"""

import unittest

from picounits.tests.unit.dimensional_algebra import DimensionAlgebra
from picounits.unit.dimensional_construction import DimensionConstruction
from picounits.quantities.quantities_construction import QualityScalingConstruction

from picounits.extensions.core.deserialization import TestParseList, TestDeserialize
from picounits.extensions.utilities.operations import TestOperators

from picounits.extensions.core.construction import (
    TestConstructPrefix, TestConstructUnits, TestConstructQuality
)

from picounits.extensions.core.syntax import (
    TestExtractionState, TestExtractPairs, TestExtractBrackets, TestExtractParentheses,
    TestQualityExtraction
)

loader = unittest.TestLoader()
suite = unittest.TestSuite()

# === Core ===

suite.addTests(loader.loadTestsFromTestCase(DimensionConstruction))
suite.addTests(loader.loadTestsFromTestCase(DimensionAlgebra))
suite.addTests(loader.loadTestsFromTestCase(QualityScalingConstruction))

# === Extensions ===

# Deserialization
suite.addTests(loader.loadTestsFromTestCase(TestParseList))
suite.addTests(loader.loadTestsFromTestCase(TestDeserialize))

# Construction
suite.addTest(loader.loadTestsFromTestCase(TestConstructPrefix))
suite.addTest(loader.loadTestsFromTestCase(TestConstructUnits))
suite.addTest(loader.loadTestsFromTestCase(TestConstructQuality))

# Syntax
suite.addTest(loader.loadTestsFromTestCase(TestExtractPairs))
suite.addTest(loader.loadTestsFromTestCase(TestExtractionState))
suite.addTest(loader.loadTestsFromTestCase(TestExtractBrackets))
suite.addTest(loader.loadTestsFromTestCase(TestExtractParentheses))
suite.addTest(loader.loadTestsFromTestCase(TestQualityExtraction))

# Operators
suite.addTests(loader.loadTestsFromTestCase(TestOperators))

runner = unittest.TextTestRunner(verbosity=2)

if __name__ == "__main__":
    result = runner.run(suite)
