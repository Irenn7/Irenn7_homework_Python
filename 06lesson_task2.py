from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

# Используем Chrome в качестве браузера (не забудьте установить chromedriver!)
driver = webdriver.Chrome()

try:
    # Перейти на нужную страницу
    driver.get("http://uitestingplayground.com/textinput")

    # Найти input field и заполнить его значением "SkyPro"
    input_field = driver.find_element(By.ID, "newButtonName")
    input_field.send_keys("SkyPro")

    # Найти кнопку и кликнуть на неё
    submit_button = driver.find_element(By.XPATH, "//button[@type='submit']")
    submit_button.click()

    # Дождаться изменения текста на кнопке
    time.sleep(1)  # Небольшая задержка для визуального подтверждения изменений

    # Найти обновлённую кнопку и получить её текст
    updated_button_text = driver.find_element(By.XPATH, "//button[@id='updatingButton']").text
    print(updated_button_text)  # Должно напечатать "SkyPro"

finally:
    # Завершаем работу драйвера
    driver.quit()
    