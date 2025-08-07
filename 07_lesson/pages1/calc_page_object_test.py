from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MainPage:

    def __init__(self, browser):
        self._driver = browser
        self._driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
        self._driver.implicitly_wait(4)
        self._driver.maximize_window()


    def opening_delay(self, delay):
        delay_field = self._driver.find_element(By.CSS_SELECTOR, "#delay")
        delay_field.clear()
        delay_field.send_keys(delay)

    def calculator_buttons(self):
        self._driver.find_element(By.XPATH, "//span[text()='7']").click()
        self._driver.find_element(By.XPATH, "//span[text()='+']").click()
        self._driver.find_element(By.XPATH, "//span[text()='8']").click()
        self._driver.find_element(By.XPATH, "//span[text()='=']").click()

    def result_output_field(self):
        result_locator = (By.CSS_SELECTOR, ".screen")
        result = WebDriverWait(self._driver, 45).until(
            EC.text_to_be_present_in_element(result_locator, "15")
        )
        return result




def test_calculator():
    browser = webdriver.Chrome()

    main_page = MainPage(browser)
    main_page.opening_delay(45)
    main_page.calculator_buttons()
    result = main_page.result_output_field()

    assert result == True, "Результат 15 не появился после ожидания"
    browser.quit()
