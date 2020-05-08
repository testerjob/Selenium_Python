from selenium import webdriver
import unittest
from pages.home.filter_panel_pages import FilterPanel
from base.starting_booking_points import StartingPoint
from selenium.webdriver.common.by import By


class SearchHotel(unittest.TestCase):

    def test_search_hotels_by_nmae(self):
        url = "https://www.hotels.com/"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.set_page_load_timeout(20)
        driver.implicitly_wait(10)
        driver.get(url)

        spt = StartingPoint(driver)
        spt.first_case("Los Angeles", "05/25/2020", "05/30/2020")

        shp = FilterPanel(driver)
        shp.test_hotel_by_name_pages("Marriott")

        hotel_name = driver.find_element_by_xpath("//li[@class='applied-filter-cont']/a/strong").text
        if hotel_name.lower() == "marriott":
            print("TC1 PASSED: "
                  "\nEXPECTED RESULT IS: marriott"
                  "\nACTUAL  RESULT IS : " + str(hotel_name.lower())+"\n")
        else:
            print("TC1 Failed.")

        driver.quit()

    def test_nighty_price_favorites(self):
        url = "https://www.hotels.com/"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.set_page_load_timeout(20)
        driver.implicitly_wait(10)
        driver.get(url)

        spt = StartingPoint(driver)
        spt.first_case("Atlanta, GA", "05/25/2020", "05/30/2020")

        sl = FilterPanel(driver)
        sl.test_move_slider_pages()

        price = driver.find_element_by_xpath("//a[@class='remove-filter']/strong/span").text
        if price == "130":
            print("TC2 PASSED: "
                  "\nEXPECTED RESULT: 130"
                  "\nACTUAL RESULT :  " + str(price)+"\n")
        else:
            print("TC2 Failed.")

        driver.quit()


    def test_slider_to_left(self):
        url = "https://www.hotels.com/"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.set_page_load_timeout(20)
        driver.implicitly_wait(10)
        driver.get(url)

        spt = StartingPoint(driver)
        spt.first_case("Los Angeles", "05/25/2020", "05/30/2020")

        sl = FilterPanel(driver)
        sl.test_slider_to_the_left_pages()

        element = driver.find_element_by_xpath("//div[@class='widget-slider-current-values']"
                                               "//span[contains(text(),'4')]").text
        if element == '4':
            print("TC3 PASSED: "
                  "\nEXPECTED RESULT: 4 "
                  "\nACTUAL RESULT :  " + str(element)+"\n")
        else:
            print("TC3 Failed.")

        driver.quit()


    def test_search_hotel(self):

        url = "https://www.hotels.com/"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.set_page_load_timeout(20)
        driver.implicitly_wait(10)
        driver.get(url)

        spt = StartingPoint(driver)
        spt.first_case("Los Angeles", "05/25/2020", "05/30/2020")

        sl = FilterPanel(driver)
        sl.test_search_hotel_page()

        pool_asser = driver.find_element_by_xpath("//a[@class='remove-filter']").text
        if pool_asser == "Pool":
            print("TC4 PASSED: "
                  "\nEXPECTED RESULT IS: Pool"
                  "\nACTUAL  RESULT IS : " + str(pool_asser.title())+"\n")
        else:
            print("TC4 Failed.")

        driver.quit()



        driver.quit()






