import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC 


# Import Page Objects
from pages.login_page import LoginPage
from pages.home_page import HomePage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage

@pytest.fixture(scope="function") # Use "function" scope for clean state per test
def driver():
    """Sets up and tears down the WebDriver."""
    chrome_options = Options()
    # chrome_options.add_argument("--headless") # Uncomment for headless execution
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    service = ChromeService(ChromeDriverManager().install())
    web_driver = webdriver.Chrome(service=service, options=chrome_options)
    web_driver.implicitly_wait(5) # Implicit wait as a fallback
    yield web_driver
    web_driver.quit()

def test_smoke_flow(driver):
    """
    Executes the E2E Smoke Test based on SMK_TC01.
    Login -> Add to Cart -> Checkout -> Cancel -> Re-Checkout -> Place Order -> Logout
    """
    # Test Data (from your smoke test definition)
    USERNAME = "jack123" # Corrected from john123 based on doc
    PASSWORD = "Password1"
    TEST_NAME = "John Doe"
    TEST_ADDR1 = "Street 123"
    TEST_ADDR2 = "Apt 4B"
    TEST_PINCODE = "123456"
    TEST_STATE = "Maharashtra"

    # --- 1. Navigate & Login ---
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login(USERNAME, PASSWORD)

   # --- 2. Verify Login Success ---
    home_page = HomePage(driver)

    try:
        print("Waiting for user avatar button...")
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(home_page._USER_AVATAR_BUTTON)
        )
        print("User avatar button found.")
    except TimeoutException:
        
        pytest.fail("Login verification failed: User avatar button did not appear within 10 seconds.")

    assert home_page.is_user_logged_in(), "User should be logged in (avatar visible)"
    assert "login" not in home_page._get_current_url(), "URL should not contain 'login' after successful login"
    print("Login Successful")
    # --- 3. Add Book to Cart ---
    initial_cart_count = home_page.get_cart_badge_count()
    home_page.add_first_book_to_cart()
    # Assert cart badge updated (wait might be needed if badge update is slow)
    try:
         home_page.wait.until(lambda d: home_page.get_cart_badge_count() > initial_cart_count)
    except TimeoutException:
        pytest.fail("Cart badge did not update after adding item")

    final_cart_count = home_page.get_cart_badge_count()
    assert final_cart_count > initial_cart_count, f"Cart count should increase (was {initial_cart_count}, now {final_cart_count})"
    print(f"Book added to cart. Cart count: {final_cart_count}")


    # --- 4. Start Checkout Process ---
    home_page.click_cart_icon()
    cart_page = CartPage(driver)
    cart_page._wait_for_url_contains("shopping-cart")
    assert "shopping-cart" in cart_page._get_current_url(), "Should be on the shopping cart page"
    assert cart_page.get_number_of_items() > 0, "Cart should have items"

    cart_page.click_checkout()
    checkout_page = CheckoutPage(driver)
    checkout_page._wait_for_url_contains("checkout")
    assert "checkout" in checkout_page._get_current_url(), "Should be on the checkout page"
    print("Checkout process started")

    # --- 5. Cancel Checkout Flow ---
    checkout_page.click_cancel()
    cart_page._wait_for_url_contains("shopping-cart") # Should return to cart
    assert "shopping-cart" in cart_page._get_current_url(), "Should return to shopping cart after cancelling checkout"
    assert cart_page.get_number_of_items() > 0, "Cart should still have items after cancelling checkout"
    print("Checkout Cancelled Successfully, returned to cart")

    # --- 6. Re-Start Checkout and Fill Valid Form ---
    cart_page.click_checkout() # Go back to checkout
    checkout_page._wait_for_url_contains("checkout")
    assert "checkout" in checkout_page._get_current_url(), "Should be back on the checkout page"

    checkout_page.fill_address_form(
        name=TEST_NAME,
        addr1=TEST_ADDR1,
        addr2=TEST_ADDR2,
        pincode=TEST_PINCODE,
        state=TEST_STATE
    )
    print("Checkout form filled")

    # --- 7. Place Order ---
    checkout_page.click_place_order()

    # --- 8. Verify Order Placement ---
    # The confirmation might stay on the checkout URL or redirect. Adjust assertion accordingly.
    # We check for the success message defined in CheckoutPage
    assert checkout_page.is_order_successful(), "Order success message should be displayed"
    print("Order Placed Successfully")
    # Optional: Check if cart becomes empty after order (depends on app logic)
    # home_page.click_cart_icon()
    # assert cart_page.is_cart_empty(), "Cart should be empty after placing order"

    # --- 9. Log Out ---
    home_page.click_logout() # Assuming logout button is accessible after order confirmation

    # --- 10. Verify Logout ---
    login_page._wait_for_url_contains("login") # Wait for redirect to login page
    assert "login" in login_page._get_current_url(), "Should be redirected to login page after logout"
    # Optional: assert login_page._is_element_displayed(login_page._LOGIN_BUTTON)
    print("Logout Successful")