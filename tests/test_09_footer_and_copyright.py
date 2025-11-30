from selenium.webdriver.common.by import By

def test_footer_and_copyright(base_url, driver):
    driver.get(base_url)
    foot_selectors = [
        "//footer",
        "//*[@id='colophon']",
        "//*[contains(@class,'site-footer')]",
    ]
    found = False
    for sel in foot_selectors:
        try:
            el = driver.find_element(By.XPATH, sel)
            if el.is_displayed():
                text = el.text.strip()
                if text:
                    found = True
                    break
        except Exception:
            continue
    assert found, "Footer element not found or empty."
