from urllib.parse import urlparse

import requests
from lxml import html

tor_socks = "socks5://127.0.0.1:9050"

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; rv:45.0) Gecko/20100101 Firefox/45.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Connection': 'keep-alive',
}

if __name__ == "__main__":
    onion_urls = []
    try:
        resp = requests.get('http://zqktlwi4fecvo6ri.onion/wiki/index.php/Main_Page',
                            proxies=dict(http=tor_socks, https=tor_socks), headers=headers)
        webpage = html.fromstring(resp.content)
        hrefs = webpage.xpath('//a/@href')
        onion_urls = []
        for ref in hrefs:
            tmp_url = urlparse(ref)
            if tmp_url.scheme in ["http", "https"] and tmp_url.hostname.endswith(".onion"):  # is onion link
                onion_urls.append(ref)
    except requests.exceptions.ConnectionError:
        print("Wiki connection failed")

    if onion_urls:
        print("Wiki scraping ended")
        active_onion_urls = []
        for onion_url in onion_urls:
            try:
                resp = requests.get(onion_url, proxies=dict(http=tor_socks, https=tor_socks), headers=headers)
                if resp.status_code == 200:
                    active_onion_urls.append(onion_url)
                    print(onion_url)
            except requests.exceptions.ConnectionError:
                pass
        if active_onion_urls:
            pass  # TODO
