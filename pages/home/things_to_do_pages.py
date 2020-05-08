from selenium.webdriver.common.by import By
import time


class ThingsToDo():

    def __init__(self, driver):
        self.driver = driver

    _to_do_link = "hdr-things-to-do"
    _city_field = "activity-destination-alp"
    _close_drop_down = "aria-option-3"
    _footer_close = "//footer[@class='footer']/a"
    _date_from = "activity-start-alp"
    _left_calendar = "//tbody[@class='datepicker-cal-dates'][1]/tr[5]/td[4]/button"
    _date_to = "//input[@id='activity-end-alp']"
    _close2 = "//button[@class='datepicker-close-btn close btn-text']"
    _submit_button = "//button[@class='btn-primary btn-action gcw-submit']"

    def getSubmitButton(self):
        return self.driver.find_element(By.XPATH, self._submit_button)

    def clickSubmitButton(self):
        self.getSubmitButton().click()

    def getClose2(self):
        return self.driver.find_element(By.XPATH, self._close2)

    def clickClose2(self):
        self.getClose2().click()

    def getDateTo(self):
        return self.driver.find_element(By.XPATH, self._date_to)

    def clickDateTo(self):
        self.getDateTo().click()

    def getLeftCalendar(self):
        return self.driver.find_element(By.XPATH, self._left_calendar)

    def clickLeftCalendar(self):
        self.getLeftCalendar().click()

    def getDateFrom(self):
        return self.driver.find_element(By.ID, self._date_from)

    def clickDateFrom(self):
        self.getDateFrom().click()

    def getFooterClose(self):
        return self.driver.find_element(By.XPATH, self._footer_close)

    def clickFooterClose(self):
        self.getFooterClose().click()

    def getCloseDropDown(self):
        return self.driver.find_element(By.ID, self._close_drop_down)

    def clickCloseDropDown(self):
        self.getCloseDropDown().click()

    def getToDoLink(self):
        return self.driver.find_element(By.ID, self._to_do_link)

    def clickToDoLink(self):
        self.getToDoLink().click()

    def getCityField(self):
        return self.driver.find_element(By.ID, self._city_field)

    def enterCityName(self, city):
        self.getCityField().send_keys(city)




    def hendle(self, city):

        parent_handel = self.driver.current_window_handle
        self.getToDoLink().click()

        handles = self.driver.window_handles

        for handle in handles:
            if handle not in parent_handel:
                self.driver.switch_to.window(handle)
                t = self.driver.current_window_handle
                print(t)
                time.sleep(2)
                self.getCityField().send_keys(city)
                time.sleep(2)

                self.getCloseDropDown().click()
                self.getFooterClose().click()
                self.getDateFrom().click()
                self.getLeftCalendar().click()
                time.sleep(2)

                self.getDateTo().click()
                self.getClose2().click()

                self.getSubmitButton().click()

                message = self.driver.find_element(By.XPATH, "//h3[@class='category-type-header']").text
                if message == "Recommendations":
                    print("TC PASSED: The message is 'Recommendations' == to: " + "'" + str(message) + "'")

                time.sleep(3)
                self.driver.close()
                break

        self.driver.switch_to.window(parent_handel)



