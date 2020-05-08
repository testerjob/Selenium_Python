from base.selenium_driver import SeleniumDriver


class BookingPage(SeleniumDriver):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    _confirmation_number_field = "fb-conf-num"
    _last_name_field = "fb-conf-lastname"
    _find_booking_button = "//button[@class='cta']"
    _req_confirm_email_link = "resend-confirmation-trigger"
    _find_your_itinerary_link = "//div[@class='col-half']//a"
    _request_confirm_email_link = "//button[@id='resend-confirmation-trigger']"
    _confirm_email_field = "conf-email"
    _resent_email_button = "fb-send-email"
    _close_resend_conf_window_button = "//button[@class='cta widget-overlay-close']"


    def clickCloseResendWindowButton(self):
        self.elementClick(self._close_resend_conf_window_button, "xpath")

    def clickResendEmailButton(self):
        self.elementClick(self._resent_email_button)

    def enterConfirmEmail(self, email):
        self.sendKeys(email, self._confirm_email_field)

    def enterConfirmNumber(self, number):
        self.sendKeys(number, self._confirmation_number_field)

    def enterLastName(self, last):
        self.sendKeys(last, self._last_name_field)

    def clickFindBookingButton(self):
        self.elementClick(self._find_booking_button, "xpath")

    def clickFindItineraryLink(self):
        self.elementClick(self._find_your_itinerary_link, "xpath")

    def clickRequestConfEmailLink(self):
        self.elementClick(self._request_confirm_email_link, "xpath")




    def test_fing_booking_errow_pages(self, number, last):
        self.enterConfirmNumber(number)
        self.enterLastName(last)
        self.clickFindBookingButton()

    def test_find_itinerary_link_pages(self):
        self.clickFindItineraryLink()

    def test_request_confirm_email_link_pages(self, email):
        self.clickRequestConfEmailLink()
        self.enterConfirmEmail(email)
        self.clickResendEmailButton()

    def test_confirm_email_error_msg_pages(self, email):
        self.clickRequestConfEmailLink()
        self.enterConfirmEmail(email)
        self.clickResendEmailButton()

    def test_conf_email_close_window_button_pages(self, email):
        self.clickRequestConfEmailLink()
        self.enterConfirmEmail(email)
        self.clickResendEmailButton()
        #self.clickCloseResendWindowButton()

    def test_empty_number_lastName_pages(self):
        self.clickFindBookingButton()


