from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoginPage(BasePage):
    """Page Object for the Login page."""

    # Locators
    _USERNAME_INPUT = (By.CSS_SELECTOR, "input[formcontrolname='username']")
    _PASSWORD_INPUT = (By.CSS_SELECTOR, "input[formcontrolname='password']")
    _LOGIN_BUTTON = (By.CSS_SELECTOR, "button[mat-raised-button][color='primary']")  
    _LOGIN_ERROR_MESSAGE = (By.CSS_SELECTOR, "mat-error.mat-error") # Locator for error messages

    def open(self):
        """Navigates to the login page."""
        self.driver.get(f"{self.base_url}login")

    def enter_username(self, username: str):
        self._send_keys(self._USERNAME_INPUT, username)

    def enter_password(self, password: str):
        self._send_keys(self._PASSWORD_INPUT, password)

    def click_login(self):
        self._click(self._LOGIN_BUTTON)

    def login(self, username: str, password: str):
        """Performs a full login action."""
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()

    def get_login_error_message(self) -> str:
         """Gets the text of the login error message, if present."""
         try:
             return self._get_text(self._LOGIN_ERROR_MESSAGE)
         except NoSuchElementException:
             return "" # Return empty string if no error message is found