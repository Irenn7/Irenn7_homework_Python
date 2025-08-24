from selenium.webdriver.common.by import By


class CartPage:
    def __init__(self, browser):
        self._driver = browser
        """Конструктор класса корзина.
         Параметры: - browser (WebDriver): Объект браузера Selenium.

         Возвращаемое значение: None."""

    @allure.step("Открытие страницы Корзина")
    def shopping_cart(self):
        """Проверяет содержимое корзины,нажимает на кнопку,
           параметры кнопки: строка - текст на кнопке, которую нужно нажать """
        self._driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

        """Метод открывает страницу корзины.

        Параметры: Нет (кроме self).

        Возвращаемое значение: None."""

