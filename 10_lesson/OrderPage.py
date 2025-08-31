from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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
        wait = WebDriverWait(self.driver, 10)
        total_element = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "summary_total_label")))
        """Метод получает итоговую сумму заказа.

        Параметры: Нет (кроме self).

        Возвращаемое значение:
            - str: Итоговая сумма заказа, отображаемая на странице."""
        return total_element.text

