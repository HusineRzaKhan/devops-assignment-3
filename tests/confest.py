import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

BASE_URL = os.getenv("TARGET_URL", "https://factaccount.blog")

@pytest.fixture(scope="session")
def base_url():
    return BASE_URL

@pytest.fixture(scope="session")
def chrome_options():
    options = Options()
    # Run headless for Jenkins/EC2
    options.add_argument("--headless=new")  # use new headless mode
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1920,1080")
    # avoid detection
    options.add_argument("--disable-blink-features=AutomationControlled")
    return options

@pytest.fixture(scope="function")
def driver(chrome_options, request):
    # Chromedriver path can be provided by env CHROMEDRIVER_PATH inside container or system PATH
    chromedriver_path = os.getenv("CHROMEDRIVER_PATH", None)
    if chromedriver_path:
        driver = webdriver.Chrome(service=webdriver.chrome.service.Service(chromedriver_path), options=chrome_options)
    else:
        driver = webdriver.Chrome(options=chrome_options)
    yield driver
    try:
        driver.quit()
    except Exception:
        pass
