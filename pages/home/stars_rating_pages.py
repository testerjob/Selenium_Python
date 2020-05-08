import time
from pages.home.searchHotel_forBooking_pages import SearchHotels
from base.starting_booking_points import StartingPoint
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from base.selenium_driver import SeleniumDriver


class StarRatingPage(SeleniumDriver):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

# HOTELS STARS RATINGS --------------------------------------------------------------------------------------
    #locators
    _check5 = "//input[@id='f-star-rating-5']"
    _check4 = "//input[@id='f-star-rating-4']"
    _check3 = "//input[@id='f-star-rating-3']"
    _check2 = "//input[@id='f-star-rating-2']"
    _check1 = "//input[@id='f-star-rating-1']"
    _five_star_sign = "//li[@id='f-star-rating-5-cont']/a"
    _four_star_sign = "//li[@id='f-star-rating-4-cont']/a"
    _three_star_sign = "//li[@id='f-star-rating-3-cont']/a"
    _two_star_sign = "//li[@id='f-star-rating-2-cont']/a"
    _one_star_sign = "//li[@id='f-star-rating-1-cont']/a"


    def getCheckBox5(self):
        return self.getElement(self._check5, locatorType="xpath")
    def getCheckBox4(self):
        return self.getElement(self._check4, locatorType="xpath")
    def getCheckBox3(self):
        return self.getElement(self._check3, locatorType="xpath")
    def getCheckBox2(self):
        return self.getElement(self._check2, locatorType="xpath")
    def getCheckBox1(self):
        return self.getElement(self._check1, locatorType="xpath")

    def clickCheckBox5(self):
        self.elementClick(self._check5, locatorType="xpath")
    def clickCheckBox4(self):
        self.elementClick(self._check4, locatorType="xpath")
    def clickCheckBox3(self):
        self.elementClick(self._check3, locatorType="xpath")
    def clickCheckBox2(self):
        self.elementClick(self._check2, locatorType="xpath")
    def clickCheckBox1(self):
        self.elementClick(self._check1, locatorType="xpath")
    def move_page(self):
        self.driver.execute_script("window.scrollBy(0, 430);")


    def getOneStarSign(self):
        return self.getElement(self._five_star_sign, locatorType="xpath")

    def verifyOneStarSign(self):
        message = self.getOneStarSign().text
        if message == "1.5-star":
            print("TC5 PASSED: "
                  "\nEXPECTED RESULT: 1.5-star "
                  "\nACTUAL RESULT:  " + str(message))

    # PAGE BEGINNER --------------------------------------------------------------------------------------

    def test_PageBeginner(self, destination, date_from, date_to):
        sh = SearchHotels(self.driver)
        sh.enterDestination(destination)
        time.sleep(1)
        sh.clickCloseWindow1()
        sh.enterFromDate(date_from)
        sh.enterToDate(date_to)
        sh.clickCloseWindow2()
        sh.clickNumberOfRooms()
        sh.enterAdultQuantity()
        sh.enterChildsQuantity()
        sh.enterChildAge1()
        sh.enterChildAge2()
        sh.clickSubmitButton()

    def test_FiveStarsPages(self, destination, date_from, date_to):
        sh = SearchHotels(self.driver)
        sh.enterDestination(destination)
        self.test_PageBeginner(destination, date_from, date_to)
        self.move_page()
        self.getCheckBox5().click()

    def test_FourStarsPages(self, destination, date_from, date_to):
        sh = SearchHotels(self.driver)
        sh.enterDestination(destination)
        self.test_PageBeginner(destination, date_from, date_to)
        self.move_page()
        self.getCheckBox4().click()


    def test_ThreeStarsPages(self, destination, date_from, date_to):
        sh = SearchHotels(self.driver)
        sh.enterDestination(destination)
        self.test_PageBeginner(destination, date_from, date_to)
        self.move_page()
        self.getCheckBox3().click()


    def test_TwoStarsPages(self, destination, date_from, date_to):
        sh = SearchHotels(self.driver)
        sh.enterDestination(destination)
        self.test_PageBeginner(destination, date_from, date_to)
        self.move_page()
        self.getCheckBox2().click()

    def test_OneStarsPages(self, destination, date_from, date_to):
        sh = SearchHotels(self.driver)
        sh.enterDestination(destination)
        self.test_PageBeginner(destination, date_from, date_to)
        self.move_page()
        self.getCheckBox1().click()


# FREE CANCELLATION--------------------------------------------------------------------------------------

    _cancel_dropdown = "//fieldset[@id='filter-payment-preference']/legend/h3"
    _free_cancellation_checkbox = "f-pay-pref-fc"
    _verification_Xbutton = "//li[@id='f-pay-pref-fc-cont']/a"

    def getCancelDropdown(self):
        return self.driver.find_element(By.XPATH, self._cancel_dropdown)

    def clickCancelDropdown(self):
        self.getCancelDropdown().click()

    def getFreeCancellationBox(self):
        return self.driver.find_element(By.ID, self._free_cancellation_checkbox)

    def clickFreeCancellationBox(self):
        self.getFreeCancellationBox().click()

    def getFreeCancellationVerificationSign(self):
        return self.driver.find_element(By.XPATH, self._verification_Xbutton).text

    def verifyFreeCancellationSign(self):
        message = self.getFreeCancellationVerificationSign()
        if message == "Free cancellation":
            print("TC6 PASSED:"
                  "\nEXPECTED RESULT: Free cancellation"
                  "\nACTUAL RESULT : " + str(message))

    def is_selected_checkBox(self):
        print("Is check box for free cancelation selected: " + str(self.getFreeCancellationBox().is_selected()))


#main
    def test_free_cancelationPages(self, destination, date_from, date_to):
        self.test_PageBeginner(destination, date_from, date_to)
        self.move_page()
        self.getCheckBox3().click()
        time.sleep(3)
        #self.verifyThreeStarSign()
        #element
        self.move_page()
        self.getCancelDropdown().click()
        self.getFreeCancellationBox().click()
        time.sleep(3)
        self.verifyFreeCancellationSign()
        self.is_selected_checkBox()

# GUEST RATING slider move slider to the right--------------------------------------------------------------------------

    _slider_to_left = "//fieldset[@id='filter-guest-rating']//div[contains(@class,'widget-slider-handle-min')]"
    _verify_that_moved = "//li[@class='applied-filter-cont']//a[contains(text(), 'Guest rating: ')]//span"

    def getSliderLeft(self):
        return self.driver.find_element(By.XPATH, self._slider_to_left)

    def move_slider(self):
        move = ActionChains(self.driver)
        move.click_and_hold(self.getSliderLeft()).move_by_offset(50, 0).release().perform()

    def movingElement(self):
        return self.driver.find_element(By.XPATH, self._verify_that_moved).text

    def validationOfElement(self):
        if self.movingElement() == '4':
            print("TC6 PASSED: "
                  "\nEXPECTED RESULT:Guess rating starts from: 4 "
                  "\nACTUAL RESULT : Guess rating starts from: 4 ")
    # main
    def test_slider_to_the_leftPages(self, destination, date_from, date_to):
        self.test_PageBeginner(destination, date_from, date_to)
        self.move_page()
        self.getSliderLeft()
        self.move_slider()
        self.movingElement()
        self.validationOfElement()
        self.takeScreenShot(self.driver)






