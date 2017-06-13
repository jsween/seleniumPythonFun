#!/usr/bin/python
# chmod +x <file_name>
# http://selenium-python.readthedocs.io/navigating.html
import time
import constants
import unittest
from selenium.webdriver.common.keys import Keys

class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        # self.driver = constants.get_firefox_driver()
        self.driver = constants.get_chrome_driver()
        # self.driver = constants.get_phantom_driver()

    def test_search_in_python_org(self):
        driver = self.driver
        driver.get("http://www.python.org")
        self.assertIn("Python", driver.title)
        elem = driver.find_element_by_name("q")
        elem.send_keys("pycon")
        elem.send_keys(Keys.RETURN)
        assert "No results found." not in driver.page_source


    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
