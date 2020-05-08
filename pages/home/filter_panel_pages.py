from base.selenium_driver import SeleniumDriver
import utilities.custom_logger as cl
import logging
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time


class FilterPanel(SeleniumDriver):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    _search_hotel_field = "f-name"
    _search_button = "f-name-cta"
    _sliderMin = "//div[contains(@class,'widget-slider-handle-min')]"
    _slider_to_left = "//fieldset[@id='filter-guest-rating']//div[@class='cta cta-control widget-slider-handle widget-slider-handle-min']"
    _pool_check_box = "f-popular-128"

    def clickPoolCheckbox(self):
        self.elementClick(self._pool_check_box)

    def test_search_hotel_page(self):
        self.clickPoolCheckbox()

    def move_page(self):
        self.driver.execute_script("window.scrollBy(0, 450);")

    def move_page_down(self):
        self.driver.execute_script("window.scrollBy(0, -250);")

    def getSliderLeft(self):
        return self.driver.find_element(By.XPATH, self._slider_to_left)

    def move_slider(self):
        move = ActionChains(self.driver)
        move.click_and_hold(self.getSliderLeft()).move_by_offset(50, 0).release().perform()

    def enterHotelName(self, hotel):
        self.sendKeys(hotel, self._search_hotel_field)

    def clickSearchHotelButton(self):
        self.elementClick(self._search_button)

    def getSliderMin(self):
        return self.getElement(self._sliderMin, locatorType="xpath")

    def movePageDown(self):
        self.driver.execute_script("window.scrollBy(0, -450);")

    def moveSliderMin(self):
        actions1 = ActionChains(self.driver)
        actions1.drag_and_drop_by_offset(self.getSliderMin(), 40, 0).perform()


     #main
    def test_hotel_by_name_pages(self, hotel):

        self.enterHotelName(hotel)
        self.clickSearchHotelButton()

    def test_slider_to_the_left_pages(self):
        self.move_page()
        self.getSliderLeft()
        self.move_slider()


    def test_move_slider_pages(self):
        self.move_page()
        self.getSliderMin()
        self.moveSliderMin()
        self.movePageDown()
        time.sleep(5)

