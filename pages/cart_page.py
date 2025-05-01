from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class CartPage(BasePage):
    """Page Object for the Shopping Cart page."""

    # Locators
    _CHECKOUT_BUTTON = (By.XPATH, "//button[contains(., 'CheckOut')]")
    _CART_ITEMS_ROWS = (By.CSS_SELECTOR, "tr.mat-mdc-row")
    _EMPTY_CART_MESSAGE = (By.XPATH, "//mat-card-title[contains(text(), 'Shopping cart is empty')]") # Adjust if needed
    _CART_TOTAL = (By.CSS_SELECTOR, "td > strong") # Might need more specific locator

    def click_checkout(self):
        self._click(self._CHECKOUT_BUTTON) 

    def is_cart_empty(self) -> bool:
        """Checks if the 'empty cart' message is displayed."""
        return self._is_element_displayed(self._EMPTY_CART_MESSAGE)

    def get_number_of_items(self) -> int:
        """Returns the number of distinct items (rows) in the cart."""
        return len(self._find_elements(self._CART_ITEMS_ROWS))

    def get_cart_total(self) -> str:
         """Gets the displayed cart total."""
         # It might take a moment for the total to update
         self.wait.until(EC.visibility_of_element_located(self._CART_TOTAL))
         return self._get_text(self._CART_TOTAL)