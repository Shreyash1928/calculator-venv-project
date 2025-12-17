import os
import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

@pytest.mark.skipif(
    os.getenv("CI") == "true",
    reason="E2E test skipped in CI (browser not available)"
)
def test_e2e():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--window-size=1920,1080")

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=chrome_options
    )

    # Load local HTML file
    file_path = os.path.abspath("index.html")
    driver.get(f"file:///{file_path}")

    driver.implicitly_wait(5)

    driver.find_element(By.ID, "num1").send_keys("5")
    driver.find_element(By.ID, "num2").send_keys("3")
    driver.find_element(By.TAG_NAME, "button").click()

    result = driver.find_element(By.ID, "result").text
    assert result == "8"

    # Screenshot proof
    driver.save_screenshot("test_result.png")

    time.sleep(1)
    driver.quit()
