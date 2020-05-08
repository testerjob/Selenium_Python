import time
from base.selenium_driver import SeleniumDriver
import utilities.custom_logger as cl
import logging


class LoginPage(SeleniumDriver):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    _signin_link = "header-sign-in"
    _email_field = "sign-in-email"
    _password_field = "sign-in-password"
    _login_button = "//button[@class='cta']"
    _log_out_dropdown = "//label[contains(@class,'icon-avatar')]"
    _sign_out_link = "hdr-signout"
    _auto_signin_checkbox = "sign-in-persistant"
    _forgot_yourPssw_link = "sign-in-forgot-password"
    _resset_pssw_field = "reset-pwd-email"
    _send_request_button = "reset-pwd-email-submit"
    _find_bookin_link = "rpw-findbooking"


    def clickFindBookingLink(self):
        self.elementClick(self._find_bookin_link)

    def isPresentSendRequestButton(self):
        self.getElement(self._send_request_button)

    def enterForgetEmail(self,email):
        self.sendKeys(email, self._resset_pssw_field, locatorType="id")

    def clickForgotPswLink(self):
        self.elementClick(self._forgot_yourPssw_link, locatorType="id")

    def clickCheckBox(self):
        self.elementClick(self._auto_signin_checkbox, locatorType="id")

    def clickSigninLink(self):
        self.elementClick(self._signin_link, locatorType="id")

    def enterEmail(self, email):
        self.sendKeys(email, self._email_field, locatorType="id")
    def enterPassword(self, password):
        self.sendKeys(password, self._password_field, locatorType="id")

    def clickLoginButton(self):
        self.elementClick(self._login_button, locatorType="xpath")

    #logout click
    def clickLogOutDroDown(self):
        self.elementClick(self._log_out_dropdown, locatorType="xpath")

    def clickSignOutLink(self):
        self.elementClick(self._sign_out_link, locatorType="id")

        #function it self
    def test_valid_login_pages(self, email, password):
        self.driver.implicitly_wait(10)
        self.clickSigninLink()
        self.enterEmail(email)
        self.enterPassword(password)
        time.sleep(4)
        self.clickLoginButton()
        time.sleep(5)
        self.clickLogOutDroDown()
        self.clickSignOutLink()

    def test_invalid_login_pages(self, email, password):
        self.driver.implicitly_wait(10)
        self.clickSigninLink()
        self.enterEmail(email)
        self.enterPassword(password)
        time.sleep(2)
        self.clickLoginButton()

    def test_forgot_pssw_pages(self,email):
        self.driver.implicitly_wait(10)
        self.clickSigninLink()
        self.clickForgotPswLink()
        self.enterForgetEmail(email)
        self.isPresentSendRequestButton()

    def test_find_booking_link_pages(self,email):
        self.driver.implicitly_wait(10)
        self.clickSigninLink()
        self.clickForgotPswLink()
        self.enterForgetEmail(email)
        self.isPresentSendRequestButton()
        self.clickFindBookingLink()























