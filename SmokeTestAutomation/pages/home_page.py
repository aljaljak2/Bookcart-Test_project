from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class HomePage(BasePage):
    """Page Object for the Home/Dashboard page."""

    # Locators
    _USER_AVATAR_BUTTON = (By.CSS_SELECTOR, "button .mat-icon[svgicon='account-circle']") # User icon indicator
    _LOGOUT_BUTTON = (By.XPATH, "//button[contains(., 'Logout')]") # More specific XPath
    _CART_ICON_BUTTON = (By.CSS_SELECTOR, "button[routerlink='/shopping-cart']")
    _CART_BADGE = (By.CSS_SELECTOR, "#mat-badge-content-0") # Check this ID in browser dev tools
    _FIRST_BOOK_ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, "app-book-card:first-of-type button[color='primary']")
    _SNACKBAR_MESSAGE = (By.CSS_SELECTOR, "simple-snack-bar > span") # Common locator for Angular Material snackbars

    def is_user_logged_in(self) -> bool:
        """Checks if the user avatar is displayed, indicating login."""
        return self._is_element_displayed(self._USER_AVATAR_BUTTON)

    def click_logout(self):
        # Sometimes requires clicking the avatar first if it's a dropdown
        # self._click(self._USER_AVATAR_BUTTON) # Uncomment if needed
        # self.wait.until(EC.visibility_of_element_located(self._LOGOUT_BUTTON)) # Wait if dropdown
        self._click(self._LOGOUT_BUTTON)

    def click_cart_icon(self):
        self._click(self._CART_ICON_BUTTON)

    def add_first_book_to_cart(self):
        self._click(self._FIRST_BOOK_ADD_TO_CART_BUTTON)
        # Wait for the confirmation snackbar
        self.wait.until(EC.visibility_of_element_located(self._SNACKBAR_MESSAGE))


    def get_cart_badge_count(self) -> int:
        """Gets the number displayed on the cart badge."""
        try:
            # Wait for the badge to potentially appear or update
            self.wait.until(EC.visibility_of_element_located(self._CART_BADGE))
            badge_text = self._get_text(self._CART_BADGE)
            return int(badge_text) if badge_text.isdigit() else 0
        except NoSuchElementException:
            return 0 # Return 0 if badge element isn't found (cart is empty)

    