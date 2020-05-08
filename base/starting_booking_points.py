from selenium.webdriver.support.select import Select
from base.selenium_driver import SeleniumDriver

#from base.starting_points import StartingPoint ### COPY FOR OTHER FILES


class StartingPoint(SeleniumDriver):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    _home_page = "//div[@class='logo-cont']/a"
    _search_field_destination = "qf-0q-destination"
    _date_from = "qf-0q-localised-check-in"
    _date_to = "qf-0q-localised-check-out"
    _close2 = "/html/body/div[8]/div[4]/button"
    _close1 = "//button[@class='cta cta-link']"
    _room_num = "qf-0q-rooms"
    _adult = "qf-0q-room-0-adults"
    _children = "qf-0q-room-0-children"
    _child_age1 = "qf-0q-room-0-child-0-age"
    _child_age2 = "qf-0q-room-0-child-1-age"
    _submit_button = "//div[@class='widget-query-group widget-query-ft']/button"
    _to_do_link = "hdr-things-to-do"

    def clickHomePage(self):
        self.elementClick(self._home_page, locatorType="xpath")

    def enterDestination(self, destination):
        self.elementClick(self._search_field_destination)
        self.sendKeys(destination, self._search_field_destination)

    def clickCloseWindow1(self):
        self.elementClick(self._close1, locatorType="xpath")

    def enterFromDate(self, date_from):
        self.elementClick(self._date_from)
        self.elementClear(self._date_from)
        self.sendKeys(date_from, self._date_from)

    def enterToDate(self, date_to):
        self.elementClick(self._date_to)
        self.elementClear(self._date_to)
        self.sendKeys(date_to, self._date_to)

    def clickCloseWindow2(self):
        self.elementClick(self._close2, locatorType="xpath")

    def clickNumberOfRooms(self):
        num_room = self.getElement(self._room_num)
        sel = Select(num_room)
        sel.select_by_value("1")

    def enterAdultQuantity(self):
        adults = self.getElement(self._adult)
        sel = Select(adults)
        sel.select_by_value("4")

    def enterChildsQuantity(self):
        children = self.getElement(self._children)
        sel = Select(children)
        sel.select_by_value("2")

    def enterChildAge1(self):
        child_age1 = self.getElement(self._child_age1)
        sel = Select(child_age1)
        sel.select_by_value("5")

    def enterChildAge2(self):
        child_age2 = self.getElement(self._child_age2)
        sel = Select(child_age2)
        sel.select_by_value("2")

    def clickSubmitButton(self):
        self.elementClick(self._submit_button, locatorType="xpath")



    def first_case(self, destination, date_from, date_to):
        self.driver.implicitly_wait(10)
        self.clickHomePage()
        self.enterDestination(destination)
        self.clickCloseWindow1()
        self.enterFromDate(date_from)
        self.enterToDate(date_to)
        self.clickCloseWindow2()
        self.clickNumberOfRooms()
        self.enterAdultQuantity()
        self.enterChildsQuantity()
        self.enterChildAge1()
        self.enterChildAge2()
        self.clickSubmitButton()


