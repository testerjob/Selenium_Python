from base.selenium_driver import SeleniumDriver


class ItineraryNumberPages(SeleniumDriver):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    _email_field = "forgot-itin-unregistered-emailId"
    _send_button = "//button[@id='forgot-itin-unregistered-submit-button']"


    def enterEmailField(self, email):
        self.sendKeys(email, self._email_field)

    def getElementSendButton(self):
        return self.getElement(self._send_button, locatorType="xpath")

    def clickSendButton(self):
        self.elementClick(self._send_button, locatorType="xpath")



    def test_no_itirenary_errow_message_pages(self, email):
        self.enterEmailField(email)
        self.clickSendButton()

    def test_wrong_email_errow_message_pages(self, email):
        self.enterEmailField(email)
        self.clickSendButton()


















