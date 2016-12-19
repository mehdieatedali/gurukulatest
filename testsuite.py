import unittest
import os
from branchtests import BranchTests
from stafftests import StaffTests

### How to create TEST SUITE

# get all tests from HomePageTest Class and more Classes
branch_tests= unittest.TestLoader().loadTestsFromTestCase(BranchTests)
staff_tests=unittest.TestLoader().loadTestsFromTestCase(StaffTests)

# Create test suite :
test_suite=unittest.TestSuite(branch_tests, staff_tests)

# Run the test suite
unittest.TextTestRunner(verbosity=2).run(test_suite)