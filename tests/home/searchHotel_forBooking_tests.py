from pages.home.searchHotel_forBooking_pages import SearchHotels
from selenium.webdriver.common.by import By
from selenium import webdriver
import unittest
import time


class SearchHotelDestination(unittest.TestCase):

    def test_search_hotels_pasitive(self):
        url = "https://www.hotels.com/"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.set_page_load_timeout(20)
        driver.implicitly_wait(10)
        driver.get(url)

        sh = SearchHotels(driver)
        sh.test_search_hotel_page("san francisco", "5/28/20", "5/30/20")

        message_text = driver.find_element(By.XPATH, "//span[@class='disclaimer-text']").text
        if message_text == "How much we get paid influences your sort order":
            print("TC1 PASSED:"
                  "\nEXPECTED RESULT: How much we get paid influences your sort order "
                  "\nACTUAL RESULT:   " + message_text + "\n")
        else:
            print("TC1 Failed.")

        time.sleep(3)
        driver.quit()


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

    def test_no_destination_error_message(self):
        url = "https://www.hotels.com/"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.set_page_load_timeout(20)
        driver.implicitly_wait(10)
        driver.get(url)

        sh = SearchHotels(driver)
        sh.test_destination_error_message("05/28/20", "05/30/20")

        message = driver.find_element_by_xpath("//div[@class='form-error']/span").text
        if message == "Please tell us the destination, hotel or landmark you’re looking for":
            print("\nTC3 PASSED: "
                  "\nEXPECTED RESULT: Please tell us the destination, hotel or landmark you’re looking for"
                  + "\nACTUAL RESULT:   " + str(message)+ "\n")
        else:
            print("TC3 Failed.")

        time.sleep(3)
        driver.quit()

    def test_no_checkin_date_error_message(self):
        url = "https://www.hotels.com/"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.set_page_load_timeout(20)
        driver.implicitly_wait(10)
        driver.get(url)

        sh = SearchHotels(driver)
        sh.test_missing_checkin_date("Las Vegas", " ", "05/30/20")

        message = driver.find_element_by_xpath("//div[@class='form-error']/span").text
        if message == "Please tell us your check-in date":
            print("\nTC4 PASSED: "
                  "\nEXPECTED RESULT: Please tell us your check-in date"
                  + "\nACTUAL RESULT:   " + str(message)+ "\n")
        else:
            print("TC4 Failed.")

        time.sleep(3)
        driver.quit()

    def test_no_checkout_date_error_message(self):
        url = "https://www.hotels.com/"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.set_page_load_timeout(20)
        driver.implicitly_wait(10)
        driver.get(url)

        sh = SearchHotels(driver)
        sh.test_missing_checkout_date("Las Vegas", "05/30/20", " ")

        message_no = driver.find_element_by_xpath("//div[@class='form-error']/span").text
        if message_no == "Please tell us your check-out date":
            print("\nTC5 PASSED: "
                  "\nEXPECTED RESULT: Please tell us your check-out date"
                  + "\nACTUAL RESULT:   " + str(message_no)+ "\n")
        else:
            print("TC5 Failed.")

        time.sleep(3)
        driver.quit()














