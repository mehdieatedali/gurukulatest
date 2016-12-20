# README #

This README would normally document whatever steps are necessary to get your application up and running.

### What is this repository for? gurukulaTest

* AutomationTest for gurukula application with Selenium and Python

### How do I get set up? ###

The application (gurukula) is written in Java and is available at: https://github.com/PA-Reporting/staff
You can launch the application using: java –jar .war (use Java 1.8 to access the application.)

Installing Python: http://python.org/download/
Installing IDE Pycharm: http://www.jetbrains.com/pycharm
Installing Selenium package: pip install -U selenium

* How to run tests

From pycharm IDE:
- Open project in pycharm
- right click on branchtests.py or stafftests.py file on the left projectpanel
- Run 'Unittests in branchtests' or Run 'Unittests in stafftests'
- To execute all tests, you can choose testsuite.py (run testsuite)
- To execute all tests with HTML report, you can choose testsuite_report.py (run testsuite)

From command line:
python testsuite.py

### testresults of the testautomation tool will be saved in output directory
 - Screenshots
 - table text files
 - Test Report

### TestCases:
- TESTCASE_01 login as admin
- TESTCASE_02 add Branch
- TESTCASE_03 add Staff



