from selenium import webdriver
import unittest
from pages.home.find_your_itinerary_num_pages import ItineraryNumberPages
import time


class ItineraryNumberTests(unittest.TestCase):

    def test_no_itirenary_errow_message(self):

        url = "https://travel.hotels.com/user/forgotitin"
        driver = webdriver.Firefox()
        driver.implicitly_wait(10)
        driver.maximize_window()
        driver.get(url)
        time.sleep(2)

        bp = ItineraryNumberPages(driver)
        bp.test_no_itirenary_errow_message_pages("alex.gmobile.test@gmail.com")

        message = driver.find_element_by_xpath("//a[@class='errorLink']").text
        if message == "Sorry, there are no itineraries associated with this email address.":
            print("TC1 PASSED: "
                  "\nEXPECTED RESULT: Sorry, there are no itineraries associated with this email address. "
                  "\nACTUAL RESULT :  " + str(message))
            driver.quit()

    def test_wrong_email_errow_message(self):

        url = "https://travel.hotels.com/user/forgotitin"
        driver = webdriver.Firefox()
        driver.implicitly_wait(10)
        driver.maximize_window()
        driver.get(url)
        time.sleep(2)

        bp = ItineraryNumberPages(driver)
        bp.test_wrong_email_errow_message_pages("alex.gmobile.test@gm")

        message = driver.find_element_by_xpath("//p[@id='userEmailidError']").text
        if message == "Please provide a valid email address.":
            print("TC2 PASSED: "
                  "\nEXPECTED RESULT: Please provide a valid email address. "
                  "\nACTUAL RESULT :  " + str(message))
            driver.quit()





