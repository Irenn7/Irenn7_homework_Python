from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ES
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.common.by import By
from AuthorizationPage import *
from MainPage import *
from OrderPage import *
from CartPage import *

def test_cart_counter():
    browser = webdriver.Firefox()
    authorization_page = AuthorizationPage(browser)
    authorization_page.search_input_field()

    main_page = MainPage(browser)
    main_page.search_product()

    cart_page = CartPage(browser)
    cart_page.shopping_cart()
    order_page = OrderPage(browser)
    order_page.fill_form()

    actual_total = order_page.total_cost().text
    expected_total = "Total: $58.29"
    assert actual_total == expected_total, (
        f"Expected {expected_total}, but got {actual_total}"
    )
    browser.quit()
