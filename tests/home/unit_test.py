from pages.home.searchHotel_forBooking_pages import SearchHotels
from selenium.webdriver.common.by import By
from selenium import webdriver
import unittest
import time


class SearchHotelDestination(unittest.TestCase):

    def test_quantity_staying_days(self):

        url = "https://www.hotels.com/"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.set_page_load_timeout(20)
        driver.implicitly_wait(10)
        driver.get(url)

        sh = SearchHotels(driver)
        sh.test_correct_quantity_staying_days("Las Vegas", "06/01/20", "06/16/20")

        quantity_text = driver.find_element(By.XPATH, "//span[@class='widget-query-num-nights']").text
        if quantity_text == "15":
            print("TC2 PASSED: "
                  "\nEXPECTED RESULT: 15 "
                  "\nACTUAL RESULT:   " + quantity_text + "\n")
        else:
            print("TC2 Failed.")

        time.sleep(3)
        driver.quit()

