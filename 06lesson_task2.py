from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Используем Chrome в качестве браузера (не забудьте установить chromedriver!)
driver = webdriver.Chrome()

    # Перейти на нужную страницу
driver.get("http://uitestingplayground.com/textinput")

element = WebDriverWait (driver, 10).until(
    EC.presence_of_element_located((By.ID, '#text'))
    )

input_field = driver.find_element(By.ID, "newButtonName")
input_field.send_keys("SkyPro")

submit_button = driver.find_element(By.XPATH, "//button[@type='submit']")
submit_button.click()

updated_button_text = driver.find_element(By.XPATH, "//button[@id='updatingButton']").text
print(updated_button_text)

driver.quit()
