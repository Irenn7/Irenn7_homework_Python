from selenium.webdriver.common.by import By
import allure

class OrderPage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Оформление заказа")
    def fill_form(self):
        """Метод заполняет форму заказа."""
        self.driver.find_element(By.ID, "first-name").send_keys("Ирина")
        self.driver.find_element(By.ID, "last-name").send_keys("Стаканова")
        self.driver.find_element(By.ID, "postal-code").send_keys("607190")
        self.driver.find_element(By.ID, "continue").click()

    @allure.step("Проверка итоговой стоимости товаров")
    def total_cost(self):
        total_element = self.driver.find_element(By.CSS_SELECTOR, ".summary_total_label")
        """Метод получает итоговую сумму заказа.

        Параметры: Нет (кроме self).

        Возвращаемое значение:
            - str: Итоговая сумма заказа, отображаемая на странице."""
        return total_element.text

