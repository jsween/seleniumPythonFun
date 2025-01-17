import constants
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class SeleniumCrawler(unittest.TestCase):
    """This class provides the web crawler logic"""

    def __init__(self):
        self.driver = constants.get_chrome_driver()
        self.driver.implicitly_wait(10)
        self.country_list = ["Canada"]#, "Germany", "Iceland", "Pakistan",
                             #"Singapore", "South Africa"]
        self.driver.get("http://international.o2.co.uk/internationaltariffs/" +
                        "calling_abroad_from_uk")

    def get_tariff_information(self, country):
        """Finds the country input element and searches for the given
        country
        """
        input_element = self.driver.find_element_by_id("countryName")
        input_element.click()
        input_element.send_keys(country)
        input_element.send_keys(Keys.RETURN)
        monthly_element = self.driver.find_element_by_id("paymonthly")
        monthly_element.click()

    def get_table_data(self):
        """Gets the table with the pricing information and prints the landline
        tariff value
        """
        table = self.driver.find_element_by_id("standardRatesTable")
        child_elements = table.find_elements_by_xpath('.//td')
        print(child_elements[1].text)


if __name__ == '__main__':
    crawler = SeleniumCrawler()
    for country in crawler.country_list:
        crawler.get_tariff_information(country)
        crawler.get_table_data()
