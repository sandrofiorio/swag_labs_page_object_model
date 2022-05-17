# import sys
from selenium.webdriver.common.by import By
from src.page_objects.locators.locators import Locators


class HomePage(object):
    def __init__(self, driver):
        self.driver = driver
        self.username_input = driver.find_element(By.ID, Locators.username_input)
        self.password_input = driver.find_element(By.ID, Locators.password_input)
        self.submit_button = driver.find_element(By.ID, Locators.submit_button)

    def type_username(self, username):
        self.username_input.send_keys(username)

    def type_password(self, pwd):
        self.password_input.send_keys(pwd)

    def click_submit(self):
        self.submit_button.click()
