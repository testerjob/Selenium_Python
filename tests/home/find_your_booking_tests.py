from selenium import webdriver
import unittest
from pages.home.find_your_booking_pages import BookingPage
from selenium.common.exceptions import NoSuchElementException
import time

class GuestRaitingSliderTest(unittest.TestCase):

    def test_fing_booking_errow_message(self):

        url = "https://www.hotels.com/profile/findbookings.html"
        driver = webdriver.Firefox()
        driver.implicitly_wait(10)
        driver.maximize_window()
        driver.get(url)
        time.sleep(2)

        bp = BookingPage(driver)
        bp.test_fing_booking_errow_pages('234234', "Alexey")

        message = driver.find_element_by_xpath("//div[@id='empty-result-error']/p").text
        if message == "We couldn’t find your booking. Please check that you entered the confirmation number and last " \
                      "name as they appear in your confirmation.":
            print("TC1 PASSED: "
                  "\nEXPECTED RESULT IS: We couldn’t find your booking. Please check"
                  " that you entered the confirmation number and last name as they appear in your confirmation. "
                  "\nACTUAL  RESULT IS : " + str(message))

            driver.quit()

    def test_find_itinerary_link(self):

        url = "https://www.hotels.com/profile/findbookings.html"
        driver = webdriver.Firefox()
        driver.implicitly_wait(10)
        driver.maximize_window()
        driver.get(url)

        bp = BookingPage(driver)
        bp.test_find_itinerary_link_pages()

        message = driver.find_element_by_xpath("//header[@id='page-header']/h1").text
        if message == "Find your itinerary number":
            print("TC2 PASSED: "
                  "\nEXPECTED RESULT IS: Find your itinerary number"
                  "\nACTUAL  RESULT IS : " + str(message))

        driver.quit()

    def test_request_confirm_email_link(self):
        url = "https://www.hotels.com/profile/findbookings.html"
        driver = webdriver.Firefox()
        driver.implicitly_wait(10)
        driver.maximize_window()
        driver.get(url)

        bp = BookingPage(driver)
        bp.test_request_confirm_email_link_pages("alex.gmobile.test@gmail.com")

        message = driver.find_element_by_xpath("//h2[@id='widget-overlay-title-2']").text
        if message == "Confirmation e-mail resent":
            print("TC3 PASSED: "
                  "\nEXPECTED RESULT IS: Confirmation e-mail resent"
                  "\nACTUAL  RESULT IS : " + str(message))

        driver.quit()

    def test_confirm_email_error_msg(self):
        url = "https://www.hotels.com/profile/findbookings.html"
        driver = webdriver.Firefox()
        driver.implicitly_wait(10)
        driver.maximize_window()
        driver.get(url)

        bp = BookingPage(driver)
        bp.test_confirm_email_error_msg_pages("tralal")

        message = driver.find_element_by_xpath("//small[@class='error-message']").text
        if message == "Please enter a valid email address.":
            print("TC4 PASSED: "
                  "\nEXPECTED RESULT IS: Please enter a valid email address."
                  "\nACTUAL  RESULT IS : " + str(message))

        driver.quit()

    def test_conf_email_close_window_button(self):

        url = "https://www.hotels.com/profile/findbookings.html"
        driver = webdriver.Firefox()
        driver.implicitly_wait(10)
        driver.maximize_window()
        driver.get(url)

        bp = BookingPage(driver)
        bp.test_conf_email_close_window_button_pages("alex.gmobil")
        time.sleep(3)

        try:
            element = driver.find_element_by_xpath("//button[@class='cta widget-overlay-close']")
            print("Is close button visible?:", element.is_displayed())
            element.click()
            element = driver.find_element_by_xpath("//button[@class='cta widget-overlay-close']")
            print("Is close button visible?:", element.is_displayed())
        except NoSuchElementException:
            print("TC5 PASSED: The window closed, Element is not present")

    def test_empty_number_empty_lastName(self):

        url = "https://www.hotels.com/profile/findbookings.html"
        driver = webdriver.Firefox()
        driver.implicitly_wait(10)
        driver.maximize_window()
        driver.get(url)

        bp = BookingPage(driver)
        bp.test_empty_number_lastName_pages()

        m1 = driver.find_element_by_id("conf-num-error").text
        if m1 == "Please enter your confirmation number":
            print("TC6.1 PASSED: "
                  "\nEXPECTED RESULT IS: Please enter your confirmation number"
                  "\nACTUAL  RESULT IS : " + str(m1))

        m2 = driver.find_element_by_id("conf-lastname-error").text
        if m2 == "Please enter your last name":
            print("TC6.2 PASSED: "
                  "\nEXPECTED RESULT IS: Please enter your last name"
                  "\nACTUAL  RESULT IS : " + str(m2))

        driver.quit()





