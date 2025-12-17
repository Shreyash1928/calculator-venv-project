from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

def test_e2e():
    chrome_options = Options()
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--start-maximized")

    # Auto-detect Chrome version
    driver = webdriver.Chrome(
    service=Service("C:/chromedriver/chromedriver.exe"),
    options=chrome_options
    )

    driver.get("file:///C:/Users/shrey/OneDrive/Desktop/Devops PWS/Assignments/calculator-venv-project/index.html")
    
    driver.implicitly_wait(5)

    driver.find_element(By.ID, "num1").send_keys("5")
    driver.find_element(By.ID, "num2").send_keys("3")
    driver.find_element(By.TAG_NAME, "button").click()

    result = driver.find_element(By.ID, "result").text
    assert result == "8"

        # 📸 Screenshot as proof
    driver.save_screenshot("test_result.png")

    time.sleep(3)  # Keep window visible
    driver.quit()
