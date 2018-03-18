import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import sys
import logging

logging.getLogger().level = logging.INFO
stream_handler = logging.StreamHandler(sys.stdout)
logging.getLogger().addHandler(logging.StreamHandler(sys.stdout))


class SearchItem(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Remote(command_executor='http://127.0.0.1:4444/wd/hub',
                                       desired_capabilities=DesiredCapabilities.CHROME)

    def locators(self):
        self.find_search_field = "twotabsearchtextbox"
        self.search_string = "Batman comics"
        self.find_first_item = "//ul[@id='s-results-list-atf']//li[@id='result_0']"
        self.find_title = "//ul[@id='s-results-list-atf']//li[@id='result_0']//a[@class='a-link-normal " \
                          "s-access-detail-page  s-color-twister-title-link a-text-normal']"
        self.find_price = "//ul[@id='s-results-list-atf']//li[@id='result_0']//div[@class='a-fixed-left-grid-col " \
                          "a-col-right']//div[@class='a-row']//a[@class='a-link-normal a-text-normal']//span[" \
                          "@class='a-size-base a-color-price s-price a-text-bold']"
        self.find_rating = "//ul[@id='s-results-list-atf']//li[@id='result_0']//span[@class='a-declarative']//span[" \
                           "@class='a-icon-alt']"
        self.find_title_second_page = "//div[@id='centerCol']//div[@id='booksTitle']//span[@id='productTitle']"
        self.find_price_second_page = "//div[@id='tmmSwatches']//span[@class='a-size-base a-color-price a-color-price']"

    def test_search_in_main_page(self):
        stream_handler.stream = sys.stdout
        driver = self.driver
        self.locators()

        logging.getLogger().info("\nGoing to https://www.amazon.de")
        driver.get("https://www.amazon.de")
        self.assertIn("Amazon.de", driver.title)

        elem = driver.find_element_by_id(self.find_search_field)

        # Search for Batman comics
        logging.getLogger().info('Search for "{0}"'.format(self.search_string))
        elem.send_keys(self.search_string)
        elem.send_keys(Keys.RETURN)

        # Check that results number above 0
        logging.getLogger().info("Check that results number above 0")
        self.assertTrue(driver.find_element_by_xpath(self.find_first_item))

        title = driver.find_element_by_xpath(self.find_title)
        title_text = title.text

        # Check that title contains "Batman" word
        logging.getLogger().info('Check that title contains "Batman" word')
        self.assertIn("Batman", str(title_text))

        price_text = driver.find_element_by_xpath(self.find_price).text
        str_price = str(price_text)
        float_price = float(str_price[str_price.index("EUR") + len("EUR"):].replace(",", "."))

        # Check that price is above 0
        logging.getLogger().info('Check that price is above 0')
        self.assertGreater(float_price, 0)

        # Check that price has EUR postfix
        logging.getLogger().info('Check that price has EUR postfix')
        self.assertIn("EUR", str_price)

        # Check that item has rating
        logging.getLogger().info('Check that item has rating')
        self.assertTrue(driver.find_element_by_xpath(self.find_rating))

        # Open 1st item page
        logging.getLogger().info('Open 1st item page')
        title.click()

        title_second_page_text = driver.find_element_by_xpath(self.find_title_second_page).text
        price_second_page_text = driver.find_element_by_xpath(self.find_price_second_page).text

        # Check that title and price are equal to the ones in result search
        logging.getLogger().info('Check that title and price are equal to the ones in result search')
        self.assertEqual(str(title_text), str(title_second_page_text))
        self.assertEqual(str_price, str(price_second_page_text))

    def tearDown(self):
        self.driver.close()
