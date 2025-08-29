from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from AuthorizationPage import AuthorizationPage
from MainPage import MainPage
from OrderPage import OrderPage
from CartPage import CartPage
import allure
import pytest

@allure.title("Тестирование подсчета суммы в корзине")
@allure.description("Проверяется правильная работа добавления товаров в корзину и расчет общей суммы.")
@allure.feature("Корзина покупок")
@allure.severity(allure.severity_level.NORMAL)

@pytest.fixture
def driver():
    """Фикстура для инициализации и закрытия драйвера."""
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()
    yield driver
    driver.quit()

@allure.story('Автоматическое тестирование корзины')
def test_cart_counter(driver):
    with allure.step("Авторизация пользователя"):
        authorization_page = AuthorizationPage(driver)
        authorization_page.search_input_field()

    with allure.step("Добавление товаров в корзину"):
        main_page = MainPage(driver)
        main_page.search_product()

    with allure.step("Переход в корзину"):
        cart_page = CartPage(driver)
        cart_page.shopping_cart()

    with allure.step("Оформление заказа и проверка итоговой стоимости"):
        order_page = OrderPage(driver)
        order_page.fill_form()

        actual_total = order_page.total_cost()
        expected_total = "$58.29"  # Форматируйте ожидание аналогично факту
        assert actual_total == expected_total, (f"Ожидалось '{expected_total}',"
                                                f" фактически получено '{actual_total}'")




