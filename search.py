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

    def test_search_in_main_page(self):
        stream_handler.stream = sys.stdout
        driver = self.driver
        logging.getLogger().info("\nGoing to https://www.amazon.de")
        driver.get("https://www.amazon.de")
        self.assertIn("Amazon.de", driver.title)

        elem = driver.find_element_by_id("twotabsearchtextbox")

        # Search for Batman comics
        search_string = "Batman comics"
        logging.getLogger().info('Search for "{0}"'.format(search_string))
        elem.send_keys(search_string)
        elem.send_keys(Keys.RETURN)

        # Check that results number above 0
        logging.getLogger().info("Check that results number above 0")
        self.assertTrue(driver.find_element_by_xpath("//ul[@id='s-results-list-atf']//li[@id='result_0']"))

        title = driver.find_element_by_xpath("//ul[@id='s-results-list-atf']//li[@id='result_0']//"
                                                     "a[@class='a-link-normal s-access-detail-page  "
                                                     "s-color-twister-title-link a-text-normal']")

        title_text = title.text

        # Check that title contains "Batman" word
        logging.getLogger().info('Check that title contains "Batman" word')
        self.assertIn("Batman", str(title_text))

        price_text = driver.find_element_by_xpath("//ul[@id='s-results-list-atf']//li[@id='result_0']//div["
                                             "@class='a-fixed-left-grid-col a-col-right']//div[@class='a-row']//a["
                                             "@class='a-link-normal a-text-normal']//span[@class='a-size-base "
                                             "a-color-price s-price a-text-bold']").text

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
        self.assertTrue(driver.find_element_by_xpath("//ul[@id='s-results-list-atf']//li[@id='result_0']//span["
                                              "@class='a-declarative']//span[@class='a-icon-alt']"))



        # Open 1st item page
        logging.getLogger().info('Open 1st item page')
        title.click()

        title_second_page_text = driver.find_element_by_xpath("//div[@id='centerCol']//div[@id='booksTitle']//span["
                                                         "@id='productTitle']").text
        price_second_page_text = driver.find_element_by_xpath("//div[@id='tmmSwatches']//span[@class='a-size-base "
                                                         "a-color-price a-color-price']").text

        # Check that title and price are equal to the ones in result search
        logging.getLogger().info('Check that title and price are equal to the ones in result search')
        self.assertEqual(str(title_text), str(title_second_page_text))
        self.assertEqual(str_price, str(price_second_page_text))

    def tearDown(self):
        self.driver.close()
