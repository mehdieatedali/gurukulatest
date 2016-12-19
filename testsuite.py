import unittest
import HTMLTestRunner
import os
from homepagetests import HomePageTest

### How to create TEST SUITE

# get all tests from HomePageTest Class and more Classes
homepage_tests= unittest.TestLoader().loadTestsFromTestCase(HomePageTest)

# Create test suite :
test_suite=unittest.TestSuite(homepage_tests)

# Run the test suite
unittest.TextTestRunner(verbosity=2).run(test_suite)