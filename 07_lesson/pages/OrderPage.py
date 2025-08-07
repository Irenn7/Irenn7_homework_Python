from selenium.webdriver.common.by import By

class OrderPage:

    def __init__(self, browser):
        self._driver = browser

    #заполнение формы своими данными
    def fill_form(self):
        self._driver.find_element(By.ID, "first-name").send_keys("Ирина")
        self._driver.find_element(By.ID, "last-name").send_keys("Стаканова")
        self._driver.find_element(By.ID, "postal-code").send_keys("607190")
        self._driver.find_element(By.ID, "continue").click()
#проверить итоговую стоимость
    def total_cost(self):
        total_element = self._driver.find_element(By.CSS_SELECTOR, ".summary_total_label")
        return total_element












