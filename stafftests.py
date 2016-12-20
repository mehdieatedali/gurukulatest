import unittest
from selenium import webdriver
import re

class StaffTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # create a new Firefox session
        cls.driver = webdriver.Firefox()
        cls.driver.implicitly_wait(30)
        cls.driver.maximize_window()

        # navigate to the gurukula application home page
        cls.driver.get('http://127.0.0.1:8080/#/')


    '''
    TESTCASE_01 login as admin
    Given: I am in homepage
    When:  I click to login button
    and I type in the fields: user=admin / password=admin
    and press Authenticate button
    Then I shoud see the message You are logged in as user admin'''

    def testcase_01_login_as_admin(self):
        # pre/given condition
        homepage_welcome=self.driver.find_element_by_xpath('html/body/div[3]/div[1]/div/div/div[2]/h1')
        homepage_welcome_text=homepage_welcome.text
        self.assertEquals('Welcome to Gurukula!',homepage_welcome_text)

        # When: click on login
        login_field = self.driver.find_element_by_xpath('html/body/div[3]/div[1]/div/div/div[2]/div/div[1]/a')
        login_field.click()
        self.driver.implicitly_wait(30)
        #and type username and password
        username_field = self.driver.find_element_by_id('username')
        username_field.send_keys('admin')
        password_field = self.driver.find_element_by_id('password')
        password_field.send_keys('admin')
        #and click on authenticate button
        authenticate_button = self.driver.find_element_by_xpath('//button[@type="submit"]')
        authenticate_button.click()

        #Then : assert the message : You are logged in as user "admin".
        logged_as_admin=self.driver.find_element_by_xpath('html/body/div[3]/div[1]/div/div/div[2]/div/div')
        logged_as_admin_text= logged_as_admin.text
        self.assertEquals('You are logged in as user "admin".',logged_as_admin_text)
        # Make screenshot for Visual test
        self.driver.save_screenshot('output/logged_as_admin.png')

    '''TESTCASE_03 add staff
    Given: I logged in as user admin
    When: I click on Entities / staff
    and click on Create new branch item
    and type values for the fields: name, code
    and press save
    Then I should see the name / code displayed in the list
    '''
    def testcase_02_add_staff(self):

        # When: I choose Entities / staff
        entities_dropdown = self.driver.find_element_by_css_selector('span.hidden-tablet')
        entities_dropdown.click()
        staff_dropdown=self.driver.find_element_by_xpath('html/body/div[2]/nav/div/div[2]/ul/li[2]/ul/li[2]/a')
        staff_dropdown.click()
        # And click Create new branch
        create_staff_button=self.driver.find_element_by_css_selector('button.btn')
        create_staff_button.click()
        # And type values for the fields: name, branch
        self.driver.implicitly_wait(3)
        name_field = self.driver.find_element_by_css_selector("input[ng-model='staff.name']")
        name_field.clear()
        name_field.send_keys('jeroen')
        branch_select=self.driver.find_element_by_xpath('html/body/div[3]/div[1]/div/div[2]/div/div/form/div[2]/div[3]/select')
        branch_select.send_keys('Telecom')

        # And save
        save_button=self.driver.find_element_by_css_selector("div.modal-footer > button.btn.btn-primary")
        save_button.click()
        self.driver.implicitly_wait(3)
        # Then I should see the staff name / branch displayed in the list
        table_tbody_staff=self.driver.find_element_by_tag_name("tbody")
        # Extract table text information
        table_tbody_staff_text=str(table_tbody_staff.text)
        # Write table information into a file for data analysis
        f = open('output/tablestaff.txt', 'w')
        f.write(table_tbody_staff_text)
        f.close
        # find name and Branch in the table list
        namestaff=re.findall('jeroen Telecom', table_tbody_staff_text)
        for item in namestaff:
            self.assertEquals('jeroen Telecom', item)
        # Make screenshot for Visual test
        self.driver.save_screenshot('output/add_staff.png')


    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2)
