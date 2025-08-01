import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#from webdriver_manager.chrome import ChromeDriverManager
#from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager

browser = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
#browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
browser.maximize_window()
driver = webdriver()
browser.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html") 

fields_to_check = ["First name", "Last name", "Address", "E-mail", "Phone number", 
"City", "Country", "Job position", "Company"]

green_color = "bs-success-rgb(25, 135, 84)"

for field_name in fields_to_check:


    field = WebDriverWait(driver, 30).until(
    EC.presence_of_element_located((By.NAME, "First name")))

expected_green_color = input.value_of_css_property("color")

expected_green_color = "bs-success-rgb(25, 135, 84)"

if expected_green_color == expected_green_color:
    assert True

zip_code_input = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.NAME, "Zip code")))

expected_red_color = zip_code_input.value_of_css_property("color")

expected_red_color = "bs-danger-rgb(220,53,69)"

if expected_red_color == expected_red_color:
    assert True


driver.quit()



