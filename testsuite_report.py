import unittest
import HTMLTestRunner
import os
from branchtests import BranchTests
from stafftests import StaffTests


# get current directory
result_dir = os.getcwd()

# load all tests from classes
branch_tests= unittest.TestLoader().loadTestsFromTestCase(BranchTests)
staff_tests=unittest.TestLoader().loadTestsFromTestCase(StaffTests)

# create a test suite
test_suite=unittest.TestSuite([branch_tests,staff_tests])

# open file
repfile = open(result_dir + '/output/TestReport.html', 'w')

# HTMLTestRunner
runner = HTMLTestRunner.HTMLTestRunner(stream=repfile,
                                       title='Test Report',
                                       description='Test suite')
# run the suite using HTMLTestRunner
# download : https://pypi.python.org/pypi/HTMLTestRunner
runner.run(test_suite)
