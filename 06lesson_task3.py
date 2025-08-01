from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService

driver = webdriver.Chrome(service = ChromeService(ChromeDriverManager().install()))
wait = WebDriverWait(driver, 30)

    # Переход на страницу
driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")

    # Ожидаем загрузки всей страницы и изображений
element = wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "#Loading images"), "Done!"))

img_element = driver.find_element(By.CSS_SELECTOR, "#https://bonigarcia.dev/selenium-webdriver-java/img/award.png")
    
    # Берём четвертую картинку с пейзажем
wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#landscape")))

print(driver.find_element(By.CSS_SELECTOR, "#landscape").get_dom_attribute("src"))
    # Завершаем сессию браузера
driver.quit()



