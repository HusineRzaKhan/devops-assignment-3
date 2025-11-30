from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_nav_presence(base_url, driver):
    driver.get(base_url)
    found = False

    # Updated selectors to match your site
    selectors = [
        "//nav[@class='nekit-nav-mega-menu-container']",
        "//nav"  # fallback
    ]

    for sel in selectors:
        try:
            # wait up to 10 seconds for the element to appear
            WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, sel))
            )
            found = True
            break
        except:
            continue

    assert found, "Main navigation not found using common selectors."
