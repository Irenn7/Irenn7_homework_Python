from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Создаем экземпляр веб-драйвера (используем Chrome)
driver = webdriver.Chrome()

try:
    # Переходим на тестовую страницу
    driver.get('http://uitestingplayground.com/ajax')
    
    # Ждем загрузки страницы
    wait = WebDriverWait(driver, 10)
    
    # Находим синюю кнопку и нажимаем её
    button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button.btn-primary')))
    button.click()
    
    # Ожидаем появление зеленого блока с текстом
    green_box = wait.until(EC.visibility_of_element_located((By.ID, 'ajax-data')))
    
    # Получаем текст из блока и выводим в консоль
    text = green_box.text.strip()
    print(text)
finally:
    # Закрываем браузер
    driver.quit()