from selenium.webdriver.common.by import By


class OrderPage:

    def __init__(self, browser):
        self._driver = browser

    """Конструктор класса Заказ товара.
    Параметры:
        - browser (WebDriver): Объект браузера Selenium.

        Возвращаемое значение: None."""

    # заполнение формы своими данными
    @allure.step("Заполнение формы личными данными пользователя")
    def fill_form(self):
        """Метод заполняет форму заказа персональными данными клиента и переходит дальше.

        Параметры: Нет (кроме self).

        Возвращаемое значение: None."""

        self._driver.find_element(By.ID, "first-name").send_keys("Ирина")
        self._driver.find_element(By.ID, "last-name").send_keys("Стаканова")
        self._driver.find_element(By.ID, "postal-code").send_keys("607190")
        self._driver.find_element(By.ID, "continue").click()

        # проверить итоговую стоимость

    @allure.step("Проверка итоговой стоимости товаров")
    def total_cost(self):
        total_element = self._driver.find_element(By.CSS_SELECTOR, ".summary_total_label")
        """Метод получает итоговую сумму заказа.

        Параметры: Нет (кроме self).

        Возвращаемое значение:
        - str: Итоговая сумма заказа, отображаемая на странице."""
        return total_element












