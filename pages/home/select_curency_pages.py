from base.selenium_driver import SeleniumDriver
from selenium.webdriver import ActionChains


class SelectCurrencyPages(SeleniumDriver):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    _currency_dropdown = "header-toggle-currency"
    _poland_link = "//a[contains(text(),'Poland, Zlotych')]"


    def clickPolandLink(self):
        self.elementClick(self._poland_link, "xpath")

    def clickCurrencyDropdown(self):
        self.elementClick(self._currency_dropdown)


    def mouse_over_try_blok(self):
        element1 = self.driver.find_element_by_id("header-toggle-currency")
        try:
            actions = ActionChains(self.driver)
            actions.move_to_element(element1).perform()
            print("PASSED: Mouse Hovered on element")
        except:
            print("FAILED: Mouse Hover failed on element")



#main
    def check_currency_pages(self):
        self.clickCurrencyDropdown()
        self.clickPolandLink()
        self.mouse_over_try_blok()
        self.takeScreenShot(self.driver)














