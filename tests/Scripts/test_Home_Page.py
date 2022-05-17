from time import sleep

from driver_base.test_base.web_driver_setup import WebDriverSetup
from src.page_objects.pages.home_page import HomePage


class SwagLab_HomePage(WebDriverSetup):
    def test_HomePage(self):
        self.driver.get("https://www.saucedemo.com/")
        #sleep(30000)
        home_page = HomePage(self.driver)
        home_page.type_username("Arnaldo")
        home_page.type_password("123456")
        home_page.click_submit()
