from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Используем хром как браузерный движок
driver = webdriver.Chrome()

try:
    # Переход на страницу
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")

    # Ожидаем загрузки всей страницы и изображений
    wait = WebDriverWait(driver, 10)
    images = wait.until(
        EC.presence_of_all_elements_located((By.TAG_NAME, "img"))
    )

    # Берём третью картинку (учитывая индексацию с нуля)
    third_image = images[0]

    # Получаем значение атрибута src
    image_src = third_image.get_attribute("src")

    # Выводим результат в консоль
    print(image_src)

finally:
    # Завершаем сессию браузера
    driver.quit()
