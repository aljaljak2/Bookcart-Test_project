from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC 
from selenium.common.exceptions import TimeoutException
class HomePage(BasePage):
    """Page Object for the Home/Dashboard page."""

    # Locators
    _USER_AVATAR_BUTTON = (By.CSS_SELECTOR, ".mat-mdc-menu-trigger > mat-icon:nth-child(2)")
    _LOGOUT_BUTTON = (By.XPATH, "//button[contains(., 'Logout')]") # More specific XPath
    _CART_ICON_BUTTON = (By.CSS_SELECTOR, "button.mdc-icon-button:nth-child(2)") 
    _CART_BADGE = (By.CSS_SELECTOR, "#mat-badge-content-0") # Check this ID in browser dev tools
    _FIRST_BOOK_ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, "app-book-card:first-of-type button[color='primary']")
    _SNACKBAR_MESSAGE = (By.XPATH, "//*[contains(text(), 'One item added to cart')]")
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
        print("Clicked on cart icon.")

    def add_first_book_to_cart(self):
        """Clicks add to cart and waits for the snackbar element to be present."""
        self._click(self._FIRST_BOOK_ADD_TO_CART_BUTTON)
        try:
           
            print("Waiting for snackbar presence...")
            self.wait.until(EC.presence_of_element_located(self._SNACKBAR_MESSAGE))
            print("Snackbar element was present.")
        except TimeoutException:
           
            print("Warning: Snackbar element did not become present within timeout.")
            


    def get_cart_badge_count(self) -> int:
        """Gets the number displayed on the cart badge."""
        try:
            # Wait for the badge to potentially appear or update
            self.wait.until(EC.visibility_of_element_located(self._CART_BADGE))
            badge_text = self._get_text(self._CART_BADGE)
            return int(badge_text) if badge_text.isdigit() else 0
        except NoSuchElementException:
            return 0 # Return 0 if badge element isn't found (cart is empty)

    