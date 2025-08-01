from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

def test_cart_counter():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    driver.guit()
