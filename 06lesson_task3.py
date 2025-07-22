from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeServise
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Используем хром как браузерный движок
driver = webdriver.Chrome()
wait = WebDriverWait(driver, 30)
    # Переход на страницу
driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")

    # Ожидаем загрузки всей страницы и изображений
element = wait.until(EC.text_to_be_present_in_element((By.ID, "Loading images"), "Done!"))
images = wait.until(
        EC.text_to_be_present_in_element((By.ID, "avard"))
    )

    # Берём третью картинку (учитывая индексацию с нуля)
third_image = images[2]

    # Получаем значение атрибута src
image_src = third_image.get_attribute("src")

    # Выводим результат в консоль
print(image_src)

    # Завершаем сессию браузера
driver.quit()
