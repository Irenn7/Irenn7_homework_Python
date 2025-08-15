from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from calculator import Calculator

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

def test_calculator():
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
    delay_field = driver.find_element(By.CSS_SELECTOR, "#delay")
    delay_field.clear()
    delay_field.send_keys("45")

    buttons = {
            "seven": driver.find_element(By.CSS_SELECTOR, "#7"),
            "plus": driver.find_element(By.CSS_SELECTOR, "#+"),
            "eight": driver.find_element(By.CSS_SELECTOR, "#8"),
            "equals": driver.find_element(By.CSS_SELECTOR, "#=")
        }
        
    for btn in ["seven", "plus", "eight", "equals"]:
            buttons[btn].click()
            calculator = Calculator()

result = WebDriverWait(driver, 50).until(
            EC.text_to_be_present_in_element((By.CSS_SELECTOR, "#screen", "15"))
        )
res = Calculator.sum(4, 5)
assert result is True

print("Тест прошел успешно!")

driver.quit()





