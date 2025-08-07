from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ES
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from pages.AuthorizationPage import Authorization
from pages.MainPage import MainPage
from pages.CartPage import CartPage
from pages.OrderPage import OrderPage

cookie = {
    "name": "cookie_policy",
    "value": "1"
}

def test_cart_counter(self):
    browser = webdriver.Chrome(service = Service(ChromeDriverManager().install()))
    self._driver.get("https://www.saucedemo.com/")
    self._driver.implicitly(4)
    self._driver.maximize_window()
    self._driver.add_cookie(cookie)

    main_page = MainPage(browser)
    main_page.set_cookie_policy()
    authorization_page = Authorization(browser)
    authorization_page.search_input_field()
    cart_page = CartPage(browser)
    cart_page.get()
    order_page = OrderPage(browser)
    order_page.find_element()


    browser.guit()

