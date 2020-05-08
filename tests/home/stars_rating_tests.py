from selenium import webdriver
from pages.home.stars_rating_pages import StarRatingPage
import unittest


class StarsRating(unittest.TestCase):

    def test_5stars_rating(self):
        url = "https://www.hotels.com/"
        driver = webdriver.Firefox()
        driver.set_page_load_timeout(20)
        driver.implicitly_wait(10)
        driver.maximize_window()
        driver.get(url)

        sr = StarRatingPage(driver)
        sr.test_FiveStarsPages("Chicago", "06/25/2020", "07/10/2020")

        stars5 = driver.find_element_by_xpath("//li[@id='f-star-rating-5-cont']/a").text
        if stars5 == "5-star":
            print("TC1 PASSED: "
                  "\nEXPECTED RESULT: 5-star "
                  "\nACTUAL RESULT:  " + str(stars5))
        driver.quit()

    def test_4stars_rating(self):
        url = "https://www.hotels.com/"
        driver = webdriver.Firefox()
        driver.set_page_load_timeout(20)
        driver.implicitly_wait(10)
        driver.maximize_window()
        driver.get(url)

        sr = StarRatingPage(driver)
        sr.test_FourStarsPages("Chicago", "06/25/2020", "07/10/2020")

        stars4 = driver.find_element_by_xpath("//li[@id='f-star-rating-4-cont']/a").text
        if stars4 == "4-star":
            print("TC2 PASSED: "
                  "\nEXPECTED RESULT: 4-star "
                  "\nACTUAL RESULT:  " + str(stars4))
        driver.quit()

    def test_3stars_rating(self):
        url = "https://www.hotels.com/"
        driver = webdriver.Firefox()
        driver.set_page_load_timeout(20)
        driver.implicitly_wait(10)
        driver.maximize_window()
        driver.get(url)

        sr = StarRatingPage(driver)
        sr.test_ThreeStarsPages("Chicago", "06/25/2020", "07/10/2020")

        stars3 = driver.find_element_by_xpath("//li[@id='f-star-rating-3-cont']/a").text
        if stars3 == "3-star":
            print("TC3 PASSED: "
                  "\nEXPECTED RESULT: 3-star "
                  "\nACTUAL RESULT:  " + str(stars3))
        driver.quit()

    def test_2stars_rating(self):
        url = "https://www.hotels.com/"
        driver = webdriver.Firefox()
        driver.set_page_load_timeout(20)
        driver.implicitly_wait(10)
        driver.maximize_window()
        driver.get(url)

        sr = StarRatingPage(driver)
        sr.test_TwoStarsPages("Chicago", "06/25/2020", "07/10/2020")

        stars2 = driver.find_element_by_xpath("//li[@id='f-star-rating-2-cont']/a").text
        if stars2 == "2-star":
            print("TC3 PASSED: "
                  "\nEXPECTED RESULT: 2-star "
                  "\nACTUAL RESULT:  " + str(stars2))
        driver.quit()

    def test_1stars_rating(self):
        url = "https://www.hotels.com/"
        driver = webdriver.Firefox()
        driver.set_page_load_timeout(20)
        driver.implicitly_wait(10)
        driver.maximize_window()
        driver.get(url)

        sr = StarRatingPage(driver)
        sr.test_OneStarsPages("Chicago", "06/25/2020", "07/10/2020")

        stars1 = driver.find_element_by_xpath("//li[@id='f-star-rating-1-cont']/a").text
        if stars1 == "1-star":
            print("TC5 PASSED: "
                  "\nEXPECTED RESULT: 1-star "
                  "\nACTUAL RESULT:  " + str(stars1))
        driver.quit()

    def test_slider_to_left(self):
        url = "https://hotels.com"
        driver = webdriver.Firefox()
        driver.implicitly_wait(10)
        driver.maximize_window()
        driver.get(url)

        sr = StarRatingPage(driver)
        sr.test_slider_to_the_leftPages("Atlanta", "06/25/2020", "07/10/2020")

        driver.quit()

    def test_free_cancellation(self):
        url = "https://hotels.com"
        driver = webdriver.Firefox()
        driver.implicitly_wait(10)
        driver.maximize_window()
        driver.get(url)

        sr = StarRatingPage(driver)
        sr.test_free_cancelationPages("Atlanta", "06/25/2020", "07/10/2020")

        driver.quit()














