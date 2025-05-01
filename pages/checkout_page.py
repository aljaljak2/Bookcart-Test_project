from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class CheckoutPage(BasePage):
    """Page Object for the Checkout page."""

    # Locators
    _NAME_INPUT = (By.CSS_SELECTOR, "mat-form-field.mat-mdc-form-field:nth-child(1) input")
    _ADDRESS_LINE1_INPUT = (By.CSS_SELECTOR, "mat-form-field.mat-mdc-form-field:nth-child(2) input")
    _ADDRESS_LINE2_INPUT = (By.CSS_SELECTOR, "mat-form-field.mat-mdc-form-field:nth-child(3) input")
    _PINCODE_INPUT = (By.CSS_SELECTOR, "mat-form-field.mat-mdc-form-field:nth-child(4) input")
    _STATE_INPUT = (By.CSS_SELECTOR, "mat-form-field.mat-mdc-form-field:nth-child(5) input")
    _PLACE_ORDER_BUTTON = (By.XPATH, "//button[contains(., 'Place Order')]")
    _CANCEL_BUTTON = (By.XPATH, "//button[contains(., 'Cancel')]")
    # Order Confirmation - Can be on a separate page or handled here
    _ORDER_SUCCESS_MESSAGE = (By.XPATH, "//h1[contains(text(), 'Order placed successfully')]")

    def enter_name(self, name: str):
        self._send_keys(self._NAME_INPUT, name)

    def enter_address_line1(self, address: str):
        self._send_keys(self._ADDRESS_LINE1_INPUT, address)

    def enter_address_line2(self, address: str):
        self._send_keys(self._ADDRESS_LINE2_INPUT, address)

    def enter_pincode(self, pincode: str):
        self._send_keys(self._PINCODE_INPUT, pincode)

    def enter_state(self, state: str):
        self._send_keys(self._STATE_INPUT, state)

    def fill_address_form(self, name: str, addr1: str, addr2: str, pincode: str, state: str):
        """Fills the entire shipping address form."""
        self.enter_name(name)
        self.enter_address_line1(addr1)
        self.enter_address_line2(addr2)
        self.enter_pincode(pincode)
        self.enter_state(state)

    def click_place_order(self):
        self._click(self._PLACE_ORDER_BUTTON)

    def click_cancel(self):
        self._click(self._CANCEL_BUTTON)

    def is_order_successful(self) -> bool:
        """Checks if the order success message is displayed."""
        # Wait specifically for the success message
        self.wait.until(EC.visibility_of_element_located(self._ORDER_SUCCESS_MESSAGE))
        return self._is_element_displayed(self._ORDER_SUCCESS_MESSAGE)