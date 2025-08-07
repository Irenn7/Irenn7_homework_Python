from selenium.webdriver.common.by import By

class OrderPage:

    def __init__(self, browser):
        self._driver = browser
        self._driver.get("https://www.saucedemo.com/checkout-step-one.html")
        self._driver.implicitly_wait(4)
        self._driver.maximize_window()
    #заполнение формы своими данными
    def find_element(self):
        self._driver.find_element(By.CSS_SELECTOR, "first-name").send_keys("Ирина")
        self._driver.find_element(By.CSS_SELECTOR, "last-name").send_keys("Стаканова")
        self._driver.find_element(By.CSS_SELECTOR, "Zip").send_keys("607190")
        self._driver.find_element(By.CSS_SELECTOR, "continue").click()
#проверить итоговую стоимость
    def total_cost(self):
        total_element = self._driver.find_element(By.CLASS_NAME, "#summary_total_label")
        actual_total = total_element.text
        expected_total = "Total: $58.29"

        assert actual_total == expected_total, (
            f"Expected {expected_total}, but got {actual_total}"
        )











