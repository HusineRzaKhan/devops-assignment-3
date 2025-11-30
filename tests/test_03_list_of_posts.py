from selenium.webdriver.common.by import By

def test_list_of_posts(base_url, driver):
    driver.get(base_url)
    # common article selectors
    candidates = [
        "//article//a",
        "//h2/a",
        "//h1/a",
        "//div[contains(@class,'post')]/a",
        "//a[contains(@href,'/20')]",  # year in URL
    ]
    links = set()
    for sel in candidates:
        try:
            elems = driver.find_elements(By.XPATH, sel)
            for e in elems:
                href = e.get_attribute('href')
                if href:
                    links.add(href)
        except Exception:
            continue
    assert len(links) >= 1, "No post links found on homepage."
