# pylint: skip-file
"""
File: runner.py

Description:
    Reference commands:
    coverage run src/tests/runner.py
    coverage report -m
    
    
    Unit Symbols required for this test suite in `.picounits`:
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

from tests.unit.dimensional_algebra import DimensionAlgebra
from tests.unit.dimensional_construction import DimensionConstruction
from tests.quantities.quantities_construction import QualityScalingConstruction

from tests.extensions.core.deserialization import TestParseList, TestDeserialize
from tests.utilities.operations import TestOperators
from tests.utilities.attributes import TestAttributes

from tests.extensions.core.construction import (
    TestConstructPrefix, 
    TestConstructUnits, 
    TestConstructQuality
)

from tests.extensions.core.syntax import (
    TestExtractionState, 
    TestExtractPairs, 
    TestExtractBrackets, 
    TestExtractParentheses,
    TestQualityExtraction
)

from tests.extensions.parser import (
    TestParseLines,
    TestParseLinesHelpers,
    TemporaryDirectory,
    TestParserImportDerived,
    TestParserOpen,
    TestParserReadLines,
)

from tests.extensions.loader import (
    TestLoaderContext,
    TestDynamicLoader,
    TestLoader
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

# Operators & attributes
suite.addTests(loader.loadTestsFromTestCase(TestOperators))
suite.addTests(loader.loadTestsFromTestCase(TestAttributes))

# Parser
suite.addTests(loader.loadTestsFromTestCase(TestParseLines))
suite.addTests(loader.loadTestsFromTestCase(TestParseLinesHelpers))
suite.addTests(loader.loadTestsFromTestCase(TemporaryDirectory))
suite.addTests(loader.loadTestsFromTestCase(TestParserImportDerived))
suite.addTests(loader.loadTestsFromTestCase(TestParserOpen))
suite.addTests(loader.loadTestsFromTestCase(TestParserReadLines))

# Loader
suite.addTests(loader.loadTestsFromTestCase(TestLoaderContext))
suite.addTests(loader.loadTestsFromTestCase(TestDynamicLoader))
suite.addTests(loader.loadTestsFromTestCase(TestLoader))


runner = unittest.TextTestRunner(verbosity=2)

if __name__ == "__main__":
    result = runner.run(suite)
