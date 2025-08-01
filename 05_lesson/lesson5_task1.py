from selenium import webdriver
from selenium.webdriver.common.by import By

# Шаг 1: Открываем браузер Google Chrome
driver = webdriver.Chrome()

try:
    # Шаг 2: Переходим на указанную веб-страницу
    driver.get("http://uitestingplayground.com/classattr")
    
    # Шаг 3: Кликнем на синюю кнопку
    blue_button = driver.find_element(By.CSS_SELECTOR, ".btn-primary")  # Используем селектор CSS для выбора кнопки
    blue_button.click()

finally:
    # Закрытие браузера после завершения тестов
    driver.quit()
    