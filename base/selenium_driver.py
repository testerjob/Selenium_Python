from selenium import webdriver
from selenium.webdriver.common.by import By
from traceback import print_stack
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import*
import utilities.custom_logger as cl
import logging
import time
#after i added custome logger I removed all print statments with [self.log.infor]


class SeleniumDriver():

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        self.driver = driver

    def getByType(self, locatorType):
        locatorType = locatorType.lower()
        if locatorType == "id":
            return By.ID
        elif locatorType == "name":
            return By.NAME
        elif locatorType == "xpath":
            return By.XPATH
        elif locatorType == "css":
            return By.CSS_SELCTOR
        elif locatorType == "class":
            return By.CLASS_NAME
        elif locatorType == "link":
            return By.LINK_TEXT
        else:
            self.log.info("Locator type" + locatorType + " is not supported ")
        return False


    def getElement(self, locator, locatorType = "id"):
        element = None
        try:
            locatorType = locatorType.lower()
            byType = self.getByType(locatorType)
            element = self.driver.find_element(byType, locator)
            #print("Element found with locator " + locator +
                           #"locatorType: " + locatorType)
            self.log.info("Element found with locator "  + locator +
                           "locatorType: " + locatorType)
        except:
            self.log.info("FAILED: Element not found with locator  " + locator +
                           "locatorType: " + locatorType)
        return element


    def elementClick(self, locator, locatorType="id"):
        try:
            element = self.getElement(locator, locatorType)
            element.click()
            self.log.info("Clicked on the element with locator: " + locator + "locatorType: " + locatorType)
        except:
            self.log.info("FAILED: Cannot click on the element :" + locator + "locatorType: " + locatorType)
           # print_stack()


    def elementClear(self,locator, locatorType="id"):
        try:
            element = self.getElement(locator, locatorType)
            element.clear()
            self.log.info("Cleared the element with locator: " + locator + "locatorType: " + locatorType)
        except:
            self.log.info("FAILED: Cannot clear the element :" + locator + "locatorType: " + locatorType)


    def sendKeys(self, data, locator, locatorType="id"):
        try:
            element = self.getElement(locator, locatorType)
            element.send_keys(data)
            self.log.info("Sent data on the element with locator: " + locator + "locatorType: " + locatorType)
        except:
            self.log.info("FAILED: Cannot send click on the element :" + locator + "locatorType: " + locatorType)
            print_stack()

    def isElementPresent(self, locator, locatorType="id"):
        element = None
        try:
            element = self.getElement(locator, locatorType) #byType is By.ID BY.XPATH
            if element is not None:
                self.log.info("Element found")
                return True
            else:
                self.log.info("FAILED: Element not found")
                return False
        except:
            self.log.info("FAILED: Element not found")
            return False

    def elementPresenceCheck(self, locator, byType):
        try:
            elementList = self.driver.find_elements(byType, locator) #return the list of elements, # byType is By.ID BY.XPATH
            if len(elementList) > 0:
                self.log.info("Element found")
                return True
            else:
                self.log.info("FAILED: Element not found")
                return False

        except:
            self.log.info("FAILED: Element not found")
            return False


    def waitForElement(self, locator, locatorType="id",
                       timeout=10, pollFrequency=0.5):

        element = None
        try:
            byType = self.getByType(locatorType)
            self.log.info("Waiting for maximum :: " + str(timeout) + " :: seconds for element to be clickable ")

            wait = WebDriverWait(self.driver, 20, poll_frequency=1,
                                 ignored_exceptions=[NoSuchElementException,
                                                     ElementNotVisibleException,
                                                     ElementNotSelectableException])
            # this element we are going to wait to be present befor to click
            element = wait.until(EC.element_to_be_clickable((byType, "stopFilter_stop-0")))

            self.log.info("Element appeared on the web page")

        except:
            self.log.info("FAILED: Element not appeared on the page")
            print_stack()
        return element

    def takeScreenShot(self, driver):

        file_name = str(round(time.time() * 1000)) + ".png"
        screen_location = "/Users/alexeyzaytsev/Documents/workspace_fraimwork/Fraim_work/screenshots/test_screenshot.png"
        new_file = screen_location + file_name

        try:
            driver.save_screenshot(new_file)
            print("Screen shot saved to location:: " + new_file)
        except NotADirectoryError:
            print("FAILED: Not a directory path issue")
