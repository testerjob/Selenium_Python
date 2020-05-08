from pages.home.things_to_do_pages import ThingsToDo
from selenium import webdriver
import unittest
import time


class SearchThingsToDo(unittest.TestCase):

    def test_things_to_do(self):
        url = "https://www.hotels.com/"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.set_page_load_timeout(20)
        driver.implicitly_wait(10)
        driver.get(url)
        time.sleep(5)

        td = ThingsToDo(driver)
        td.hendle("Chicago")

        driver.quit()





