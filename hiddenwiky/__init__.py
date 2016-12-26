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


class OnionLink:
    def __init__(self, url, name):
        self.url = url
        self.name = name

    def __str__(self):
        return "{} {}".format(self.url, self.name)


if __name__ == "__main__":
    onion_links = []
    try:
        resp = requests.get('http://zqktlwi4fecvo6ri.onion/wiki/index.php/Main_Page',
                            proxies=dict(http=tor_socks, https=tor_socks), headers=headers)
        webpage = html.fromstring(resp.content)
        hrefs = webpage.xpath('//a/@href')
        onion_links = []
        for ref in hrefs:
            tmp_url = urlparse(ref)
            if tmp_url.scheme in ["http", "https"] and tmp_url.hostname.endswith(".onion"):  # is onion link
                desc = webpage.xpath("//a[@href='{}']/text()".format(ref))
                if desc:
                    onion_links.append(OnionLink(ref, desc[0]))
    except requests.exceptions.ConnectionError:
        print("Wiki connection failed")

    if onion_links:
        print("Active links:")
        active_onion_links = []
        for onion_link in onion_links:
            try:
                resp = requests.get(onion_link.url, proxies=dict(http=tor_socks, https=tor_socks), headers=headers)
                if resp.status_code == 200:
                    active_onion_links.append(onion_link)
                    print(onion_link)
            except requests.exceptions.ConnectionError:
                pass
        if active_onion_links:
            pass  # TODO
