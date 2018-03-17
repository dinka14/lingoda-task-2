import unittest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


class SearchItem(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Remote(command_executor='http://127.0.0.1:4444/wd/hub',
                                       desired_capabilities=DesiredCapabilities.CHROME)

    def test_search_in_main_page(self):
        driver = self.driver
        driver.get("https://www.amazon.de")
        self.assertIn("Amazon.de", driver.title)
        elem = driver.find_element_by_id("twotabsearchtextbox")
        elem.send_keys("hfjdrnjkdernfjkernfjkernjerkn")
        elem.send_keys(Keys.RETURN)
        self.assertTrue(driver.find_element_by_xpath("//ul[@id='s-results-list-atf']//li[@id='result_0']"))



    def tearDown(self):
        self.driver.close()
