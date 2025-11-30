import requests

def test_homepage_status_and_title(base_url, driver):
    # HTTP status
    resp = requests.get(base_url, timeout=10)
    assert resp.status_code == 200, f"Homepage returned {resp.status_code}"
    # Title check via Selenium
    driver.get(base_url)
    title = driver.title
    assert title and len(title.strip()) > 0, "Page title is empty"
