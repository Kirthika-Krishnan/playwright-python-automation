# login_page.py
from base_page import BasePage
from playwright.sync_api import expect

class LoginPage(BasePage):
    URL = "https://www.saucedemo.com"

    # Locators as class properties — defined once, used everywhere
    USERNAME_INPUT = "#user-name"
    PASSWORD_INPUT = "#password"
    LOGIN_BUTTON = "#login-button"
    ERROR_MESSAGE = "[data-test='error']"

    def load(self):
        self.navigate(self.URL)

    def login(self, username: str, password: str):
        self.page.fill(self.USERNAME_INPUT, username)
        self.page.fill(self.PASSWORD_INPUT, password)
        self.page.click(self.LOGIN_BUTTON)

    def get_error_message(self):
        return self.page.locator(self.ERROR_MESSAGE).text_content()
