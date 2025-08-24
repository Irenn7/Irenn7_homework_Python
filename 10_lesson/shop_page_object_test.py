from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
import allure

from AuthorizationPage import *
from MainPage import *
from OrderPage import *
from CartPage import *


@allure.title("Тестирование подсчета суммы в корзине")
@allure.description("Проверяется правильная работа добавления товаров в корзину и расчет общей суммы.")
@allure.feature("Корзина покупок")
@allure.severity(allure.severity_level.NORMAL)
def test_cart_counter():
    with allure.step("Создание экземпляра веб-драйвера"):
        browser = webdriver.Firefox()

    @allure.step("Авторизация пользователя")
    def perform_authorization():
        authorization_page = AuthorizationPage(browser)
        authorization_page.search_input_field()

    @allure.step("Добавление товаров в корзину")
    def add_products_to_cart():
        main_page = MainPage(browser)
        main_page.search_product()

    @allure.step("Переход в корзину")
    def open_shopping_cart():
        cart_page = CartPage(browser)
        cart_page.shopping_cart()

    @allure.step("Оформление заказа и проверка итоговой стоимости")
    def check_order_total():
        order_page = OrderPage(browser)
        order_page.fill_form()

    actual_total = order_page.total_cost().text
    expected_total = "Total: $58.29"
    assert actual_total == expected_total, (
        f"Expected {expected_total}, but got {actual_total}"
    )
    f"Ожидалось '{expected_total}', фактически получено '{actual_total}'"

    # Выполнение шагов
    perform_authorization()
    add_products_to_cart()
    open_shopping_cart()
    check_order_total()

    with allure.step("Закрытие браузера"):

        browser.quit()

