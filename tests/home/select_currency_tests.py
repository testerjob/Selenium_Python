from selenium import webdriver
from pages.home.select_curency_pages import SelectCurrencyPages
import unittest
import time


class SelectCurrency(unittest.TestCase):

    def test_check_currency(self):
        url = "https://hotels.com"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.set_page_load_timeout(20)
        driver.implicitly_wait(10)
        driver.get(url)

        scps = SelectCurrencyPages(driver)
        scps.check_currency_pages()

        time.sleep(3)
        element = driver.find_element_by_id("header-toggle-currency").text
        if element.upper() == "PLN":
            print("TC1 PASSED: "
                  "\nEXPECTED RESULT IS: PLN"
                  "\nACTUAL  RESULT IS : " + str(element.upper()))

        driver.quit()

