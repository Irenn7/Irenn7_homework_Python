from selenium import webdriver
from selenium.webdriver.common.by import By

# Шаг 1: Открываем браузер Google Chrome
driver = webdriver.Chrome()

try:
    # Шаг 2: Переходим на указанную веб-страницу
    driver.get("http://uitestingplayground.com/dynamicid")
    
    # Шаг 3: Нажимаем на синюю кнопку без ID
    button_without_id = driver.find_element(By.CSS_SELECTOR, 'button.btn.btn-primary')
    button_without_id.click()

finally:
    # Закрытие браузера после завершения тестов
    driver.quit()
    