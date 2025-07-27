from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("http://uitestingplayground.com/textinput")

element = WebDriverWait (driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, 'updatingButton'))
    )

input = driver.find_element(By.ID, "updatingButton")
input.send_keys("SkyPro")

click = driver.find_element(By.CSS_SELECTOR, "updatingButton").click()
text = driver.find_element(By.CSS_SELECTOR, "updatingButton").text

print(text)

driver.quit()

