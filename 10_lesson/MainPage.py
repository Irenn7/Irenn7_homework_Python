from selenium.webdriver.common.by import By

class MainPage:

    def __init__(self, browser):
        """Конструктор класса Главная страница.
           Параметры:
        - browser (WebDriver): Объект браузера Selenium.

           Возвращаемое значение: None."""
        self._driver = browser

    @allure.step("Поиск товара")
    def search_product(self):
        """Метод ищет товары по заданному списку ID и добавляет их в корзину.

        Параметры: Нет (кроме self).

        Возвращаемое значение: None."""

        products = [
                       "add-to-cart-sauce-labs-backpack",
                       "add-to-cart-sauce-labs-bolt-t-shirt"
                       "add-to-cart-sauce-labs-onesie",
        ]

        for product_id in products:
            self._driver.find_element(By.ID, product_id).click()




