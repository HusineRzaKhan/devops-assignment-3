import requests

def test_rss_feed_available(base_url):
    for feed_path in ["/feed", "/rss", "/feeds/posts/default"]:
        url = base_url.rstrip("/") + feed_path
        try:
            r = requests.get(url, timeout=10)
            if r.status_code == 200 and ("<rss" in r.text.lower() or "<feed" in r.text.lower()):
                assert True
                return
        except Exception:
            continue
    pytest.fail("No RSS feed found at common endpoints (/feed, /rss)")
