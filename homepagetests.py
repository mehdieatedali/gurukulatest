import unittest
from selenium import webdriver
import re

class HomePageTest(unittest.TestCase):
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

    '''TESTCASE_02 add Branches
    Given: I logged in as user admin
    When: I click on Entities / branche
    and click on Create new branch item
    and type values for the fields: name, code
    and press save
    Then I should see the name / code displayed in the list
    '''
    def testcase_02_add_branch(self):

        # When: I choose Entities / branche
        entities_dropdown = self.driver.find_element_by_css_selector('span.hidden-tablet')
        entities_dropdown.click()
        branche_dropdown=self.driver.find_element_by_xpath('html/body/div[2]/nav/div/div[2]/ul/li[2]/ul/li[1]/a/span[2]')
        branche_dropdown.click()
        # And click Create new branch
        create_branche_button=self.driver.find_element_by_css_selector('button.btn')
        create_branche_button.click()
        # And type values for the fields: name, code
        name_field=self.driver.find_element_by_css_selector("input[ng-model='branch.name']")
        name_field.send_keys('jeroen')
        code_field=self.driver.find_element_by_css_selector("input[ng-model='branch.code']")
        code_field.send_keys('100')
        # And save
        save_button=self.driver.find_element_by_css_selector("div.modal-footer > button.btn.btn-primary")
        save_button.click()

        # Then I should see the name / code displayed in the list
        table_tbody=self.driver.find_element_by_tag_name("tbody")
        # Extract table text information
        table_tbody_text=str(table_tbody.text)
        # Write table information into a file for data analysis
        f = open('output/table.txt', 'w')
        f.write(table_tbody_text)
        f.close
        # find name and code in the table list
        name=re.findall('jeroen 100', (table_tbody_text))
        for item in name:
            self.assertEquals('jeroen 100', item)
        # Make screenshot for Visual test
        self.driver.save_screenshot('output/add_branches.png')


    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2)
