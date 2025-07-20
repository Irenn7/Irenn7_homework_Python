from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# Шаг 1: Настройка и запуск браузера Firefox
service = FirefoxService(executable_path="./geckodriver")  # Укажите путь к вашему geckodriver
driver = webdriver.Firefox(service=service)

try:
    # Шаг 2: Переход на нужную страницу
    driver.get("http://the-internet.herokuapp.com/inputs")

    # Шаг 3: Поиск поля ввода и ввод текста
    input_field = driver.find_element(By.TAG_NAME, "input")
    input_field.send_keys("Sky")

    # Шаг 4: Очистка поля ввода
    input_field.clear()

    # Шаг 5: Повторный ввод нового значения
    input_field.send_keys("Pro")

finally:
    # Шаг 6: Завершаем работу браузера
    driver.quit()
    