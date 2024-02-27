import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import time

class Task1(unittest.TestCase):

    def setUp(self):
        # driver = webdriver.Firefox()
        self.driver = webdriver.Chrome()  #basic run

    # Scenario: Positive case
    # Accepted user can login
    def test(self):
        driver = self.driver
        driver.get("http://www.saucedemo.com")
        self.assertIn("Swag Labs", driver.title)

        user_box = driver.find_element_by_id('user-name')
        user_box.send_keys('standard_user')
        pass_box = driver.find_element_by_id('password')
        pass_box.send_keys('secret_sauce')
        pass_box.send_keys(Keys.RETURN)
        self.assertNotIn("Epic sadface: Password is required", driver.page_source)
        self.assertNotIn("Epic sadface: Username is required", driver.page_source)
        self.assertNotIn("Epic sadface: Username and password do not match any user in this service", driver.page_source)
        # assert "Epic sadface: Password is required" not in driver.page_source
        # assert "Epic sadface: Username is required" not in driver.page_source
        # assert "Epic sadface: Username and password do not match any user in this service" not in driver.page_source


    # Scenario: Negative case
    # Accepted user cant login with wrong password
    def test2(self):
        driver = self.driver
        driver.get("http://www.saucedemo.com")
        self.assertIn("Swag Labs", driver.title)
        user_box = driver.find_element_by_id('user-name')
        user_box.send_keys('standard_user')
        pass_box = driver.find_element_by_id('password')
        pass_box.send_keys('secret_sauce1111')  # invalid password
        pass_box.send_keys(Keys.RETURN)
        self.assertNotIn("Epic sadface: Password is required", driver.page_source)
        self.assertNotIn("Epic sadface: Username is required", driver.page_source)
        self.assertIn("Epic sadface: Username and password do not match any user in this service", driver.page_source)
# assert "Epic sadface: Password is required" not in driver.page_source
# assert "Epic sadface: Username is required" not in driver.page_source
# assert "Epic sadface: Username and password do not match any user in this service" in driver.page_source

#
# # Scenario: Negative case
# # Not accepted user cant login with correct password
    def test3(self):
        driver = self.driver
        driver.get("http://www.saucedemo.com")
        self.assertIn("Swag Labs", driver.title)
        user_box = driver.find_element_by_id('user-name')
        user_box.send_keys('standard_user111')  # invalid username
        pass_box = driver.find_element_by_id('password')
        pass_box.send_keys('secret_sauce')
        pass_box.send_keys(Keys.RETURN)
        self.assertNotIn("Epic sadface: Password is required", driver.page_source)
        self.assertNotIn("Epic sadface: Username is required", driver.page_source)
        self.assertIn("Epic sadface: Username and password do not match any user in this service", driver.page_source)
# assert "Epic sadface: Password is required" not in driver.page_source
# assert "Epic sadface: Username is required" not in driver.page_source
# assert "Epic sadface: Username and password do not match any user in this service" in driver.page_source
#
#
# # Scenario:Positive case
# # Accepted user can login after login failed
# #
# # Scenario: Security
# # Not accepted user cant login
# # Access denied with empty credentials-> missing username
# # Access denied with empty credentials-> missing password
# #
# # Scenario:Page view/functionality
# # Login by enter or button
# driver.find_element(By.ID, "submit").click()
#


# elem.clear()

# assert "Epic sadface: Password is required" in driver.page_source
# assert "Epic sadface: Username is required" in driver.page_source
# assert "Epic sadface: Username and password do not match any user in this service" in driver.page_source


#     def tearDown(self):
#         self.driver.close()

if __name__ == "__main__":
    unittest.main()