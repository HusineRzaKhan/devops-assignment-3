from selenium.webdriver.common.by import By
import requests

def test_open_first_post(base_url, driver):
    driver.get(base_url)
    # find first post link via H2 or article anchor
    selectors = ["//h2/a", "//article//a", "//h1/a", "//a[contains(@href,'/20')]"]
    first_href = None
    for sel in selectors:
        try:
            elem = driver.find_element(By.XPATH, sel)
            href = elem.get_attribute("href")
            if href:
                first_href = href
                break
        except Exception:
            continue
    assert first_href, "Could not find a post link to open."
    # verify reachable
    resp = requests.get(first_href, timeout=10)
    assert resp.status_code == 200, f"Post URL returned {resp.status_code}"
    # navigate there with Selenium
    driver.get(first_href)
    assert "404" not in driver.title, "Opened page looks like 404."
