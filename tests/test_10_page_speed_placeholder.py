import time

def test_homepage_load_time(base_url, driver):
    start = time.time()
    driver.get(base_url)
    end = time.time()
    duration = end - start
    # assert page loaded within 15 seconds (network dependent). Choose conservative threshold for EC2.
    assert duration < 15, f"Homepage load too slow: {duration:.1f}s"
