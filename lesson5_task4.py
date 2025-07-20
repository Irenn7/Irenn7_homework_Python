from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Шаг 1: Установка службы Firefox и запуск браузера
service = FirefoxService(executable_path='./geckodriver')  # Путь к геко-драйверу
driver = webdriver.Firefox(service=service)

try:
    # Шаг 2: Переход на нужную страницу
    driver.get('http://the-internet.herokuapp.com/login')

    # Шаг 3: Заполнение полей формы авторизации
    username_input = driver.find_element(By.ID, 'username')
    username_input.send_keys('tomsmith')

    password_input = driver.find_element(By.ID, 'password')
    password_input.send_keys('SuperSecretPassword!')

    # Шаг 4: Отправляем форму нажатием на кнопку Login
    login_button = driver.find_element(By.XPATH, '//button[@type="submit"]')
    login_button.click()

    # Шаг 5: Ждем появления зеленого уведомления и выводим его текст
    success_message = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, 'flash.success'))
    )
    print(success_message.text.strip())

finally:
    # Шаг 6: Закрываем браузер
    driver.quit()
    