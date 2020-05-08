from selenium import webdriver
import unittest
from pages.home.login_page import LoginPage
import time

class LoginTest(unittest.TestCase):

    def test_valid_login_hotels(self):
        url = "https://www.hotels.com/"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.set_page_load_timeout(20)
        driver.implicitly_wait(10)
        driver.get(url)

        lp = LoginPage(driver)
        lp.test_valid_login_pages("alex.gmobile.test@gmail.com", "Testdriver1!")

        confirmation = driver.find_element_by_xpath("//h1[@class='cont-hd-alt widget-query-heading']").text
        if confirmation == "Where to, Alexey?":
            print("TC1. PASSED: "
                  "\nEXPECTED RESULT: Where to, Alexey? "
                  "\nACTUAL RESULT : " + confirmation)

        driver.quit()

    def test_invalid_login(self):
        url = "https://www.hotels.com/"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.set_page_load_timeout(20)
        driver.implicitly_wait(10)
        driver.get(url)

        lp = LoginPage(driver)
        lp.test_invalid_login_pages("alex.gmobile.test@gmail.com", "Testdriver")

        time.sleep(5)
        message = driver.find_element_by_xpath("//div[@class='msg-error-icon msg-big mb-spider']/a").text
        if message == "forgotten your password":
            print("TC2. PASSED:: The message for missing password is: " + message)

        driver.close()

    def test_empty_username_message(self):
        url = "https://www.hotels.com/"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.set_page_load_timeout(20)
        driver.implicitly_wait(10)
        driver.get(url)

        time.sleep(3)
        lp = LoginPage(driver)
        lp.test_invalid_login_pages("", "Testdriver1!")

        time.sleep(5)
        message = driver.find_element_by_xpath("//small[@id='email-error']").text
        if message == "Please enter your email address":
            print("TC3. PASSED: The message for missing password is: " + message)

        driver.close()

    def test_empty_password_message(self):
        url = "https://www.hotels.com/"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.set_page_load_timeout(20)
        driver.implicitly_wait(10)
        driver.get(url)

        time.sleep(3)
        lp = LoginPage(driver)
        lp.test_invalid_login_pages("alex.gmobile.test@gmail.com", "")

        time.sleep(5)
        message = driver.find_element_by_xpath("//small[@id='password-error']").text
        if message == "Please enter your password":
            print("TC4. PASSED: The message for missing password is: " + message)

        driver.quit()

    def test_forgot_pssw(self):
        url = "https://www.hotels.com/"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.set_page_load_timeout(20)
        driver.implicitly_wait(10)
        driver.get(url)

        time.sleep(3)
        lp = LoginPage(driver)
        lp.test_forgot_pssw_pages("alex.gmobile.test@gmail.com")

        message = driver.find_element_by_id("reset-pwd-email-submit").text
        if message == "Send request":
            print("TC1. PASSED: "
                  "\nEXPECTED RESULT: Send request "
                  "\nACTUAL RESULT : " + message)

        driver.quit()


    def test_find_your_booking_link(self):
        url = "https://www.hotels.com/"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.set_page_load_timeout(20)
        driver.implicitly_wait(10)
        driver.get(url)

        time.sleep(3)
        lp = LoginPage(driver)
        lp.test_find_booking_link_pages("alex.gmobile.test@gmail.com")

        message = driver.find_element_by_xpath("//div[@class='cont-hd']/h1").text
        if message == "Find your booking":
            print("TC1. PASSED: "
                  "\nEXPECTED RESULT: Find your booking "
                  "\nACTUAL RESULT : " + message)
        driver.quit()






