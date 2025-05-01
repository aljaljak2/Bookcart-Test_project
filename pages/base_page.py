      
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from typing import List

class BasePage:
    """Base class for all Page Objects"""

    def __init__(self, driver: WebDriver, base_url="https://bookcart.azurewebsites.net/"):
        self.driver = driver
        self.base_url = base_url
        self.wait = WebDriverWait(driver, 10) 

    def _find_element(self, locator: tuple) -> WebElement:
        """Finds a single element, waiting until it's visible."""
        try:
            # print(f"Finding element: {locator}") # Debug print
            element = self.wait.until(EC.visibility_of_element_located(locator))
            # print("Element found and visible.") # Debug print
            return element
        except TimeoutException:
            # print(f"Timeout finding element: {locator}") # Debug print
            raise NoSuchElementException(f"Element with locator {locator} not found or not visible within timeout.")

    def _find_elements(self, locator: tuple) -> List[WebElement]:
        """Finds multiple elements, waiting until at least one is visible."""
        try:
            # Wait for presence first, then visibility might be too strict if some are hidden
            self.wait.until(EC.presence_of_element_located(locator))
            return self.driver.find_elements(*locator)
        except TimeoutException:
             # Return empty list if no elements are found after waiting
            return []


    def _click(self, locator: tuple):
        """Waits for an element to be clickable and then clicks it."""
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()

    def _send_keys(self, locator: tuple, text: str):
        """Finds an element, waits for it to be clickable, clears it, and sends keys."""
        try:
            element = self.wait.until(EC.element_to_be_clickable(locator))
            element.clear()
            element.send_keys(text)
        except TimeoutException:
            raise NoSuchElementException(f"Element with locator {locator} not interactable for send_keys within timeout.")
        
    def _get_text(self, locator: tuple) -> str:
        """Finds an element and returns its text."""
        element = self._find_element(locator)
        return element.text

    def _get_current_url(self) -> str:
        """Returns the current URL."""
        return self.driver.current_url

    def _wait_for_url_contains(self, url_substring: str):
        """Waits until the current URL contains the given substring."""
        self.wait.until(EC.url_contains(url_substring))

    def _is_element_displayed(self, locator: tuple) -> bool:
        """Checks if an element is displayed without throwing an error."""
        try:
            return self._find_element(locator).is_displayed()
        except NoSuchElementException:
            return False

    