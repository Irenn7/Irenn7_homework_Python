from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait


options = Options
driver = webdriver.Firefox(options = Options)

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
# заходим на сайт
driver = get("https://www.saucedemo.com")
#авторизируюсь
username_field =driver.find_element(By.ID, "user_name")
password_field = driver.find_element(By.ID, "password")
login_button = driver.find_element(By.ID, "login-button")

username_field.send_keys("standard_user")
password_field.send_keys("secret_sauce")
login_button.click()

#добавить товары в корзину
driver.find_element(By.GSS_SELECTOR, "Sauce Labs Backpack")
driver.find_element(By.GSS_SELECTOR, "Sauce Labs Bolt T-Shirt")
driver.find_element(By.GSS_SELECTOR, "Sauce Labs Onesie")

for product_name in driver.find_element:
            add_to_cart_button = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located(
                        (By.XPATH, f"//div[text()='{product_name}']/ancestor::div/div/button"))
            )
            add_to_cart_button.click()
# перейти в корзину
cart_link = driver.find_element(By.CLASS_NAME, "shopping_cart_link")
cart_link.click()
#нажать checkout
checkout_button = driver.find_element(By.CLASS_NAME, "checkout")
checkout_button.click()
#заполнить свои данные
first_name_field = driver.find_element(By.ID, "first-name")
last_name_field = driver.find_element(By.ID, "last-name")
postal_code_field = driver.find_element(By.ID, "postal-code")
continue_button = driver.find_element(By.ID, "continue")

first_name_field.send_keys("Ирина")
last_name_field.send_keys("Стаканова")
postal_code_field.send_keys("607190")

#нажать на кнопку
continue_button = driver.find_element(By.CLASS_NAME, "continue")
checkout_button.click()

#читать со страницы итоговую стоимость

total_amount = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "summary_total_label"))
        ).text.split(":")[1].strip()
#закрываем браузер

driver.guit()

#проверяем итоговую сумму
assert float(total_amount.replace("$", "")) == 58.29, f"Итоговая сумма не совпадает. Ожидалось: $58.29, факт: ${total_amount}"

print("Тест успешно выполнен.")





