from selenium.webdriver.common.by import By

def test_nav_presence(base_url, driver):
    driver.get(base_url)
    # Try common navigation selectors
    selectors = [
        "//nav",
        "//header//nav",
        "//*[@role='navigation']",
        "//*[@id='main-nav']",
        "//*[@class='main-navigation']",
    ]
    found = False
    for sel in selectors:
        try:
            el = driver.find_element(By.XPATH, sel)
            if el.is_displayed():
                found = True
                break
        except Exception:
            continue
    assert found, "Main navigation not found using common selectors."
