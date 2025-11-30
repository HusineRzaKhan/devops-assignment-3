from selenium.webdriver.common.by import By

def test_post_has_h1_and_content(base_url, driver):
    driver.get(base_url)
    # open first post like previous test
    try:
        elem = driver.find_element(By.XPATH, "//h2/a")
        href = elem.get_attribute("href")
    except Exception:
        elem = driver.find_element(By.XPATH, "//article//a")
        href = elem.get_attribute("href")
    driver.get(href)
    # h1
    h1 = driver.find_elements(By.TAG_NAME, "h1")
    assert h1 and len(h1[0].text.strip()) > 0, "Post H1 missing or empty"
    # body text
    paragraphs = driver.find_elements(By.XPATH, "//article//p|//div[contains(@class,'entry-content')]//p")
    assert paragraphs and any(p.text.strip() for p in paragraphs), "No readable content paragraphs found in post"
