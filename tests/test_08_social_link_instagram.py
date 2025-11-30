from selenium.webdriver.common.by import By

def test_social_link_instagram(base_url, driver):
    driver.get(base_url)
    anchors = driver.find_elements(By.TAG_NAME, "a")
    found = False
    for a in anchors:
        href = a.get_attribute("href") or ""
        if "instagram.com" in href:
            found = True
            break
    # This is allowed to be false if site doesn't link Instagram; we assert presence but if not available mention reason
    assert found, "No Instagram link found on homepage (ok if site has no instagram)."
