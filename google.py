import time
import constants
import unittest
from selenium.webdriver.common.keys import Keys

class GoogleSearch(unittest.TestCase):

    def setUp(self):
        # self.driver = constants.get_firefox_driver()
        self.driver = constants.get_chrome_driver()
        # self.driver = constants.get_phantom_driver()

    def test_search_in_python_org(self):
        driver = self.driver
        driver.get("http://www.google.com")
        self.assertIn("Google", driver.title)
        elem = driver.find_element_by_id("lst-ib")
        elem.send_keys("python")
        elem.send_keys(Keys.RETURN)
        assert "No results found." not in driver.page_source
        time.sleep(5)


    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
