from lxml import html
from multiprocessing.pool import Pool
from typing import Optional
from urllib.parse import urlparse

import json
import os
import requests


class OnionLink:
    def __init__(self, url, name, desc):
        self.url = url
        self.name = name
        self.desc = desc

    def __str__(self):
        return json.dumps(self.__dict__)


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; rv:45.0) Gecko/20100101 Firefox/45.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Connection': 'keep-alive',
}

tor_socks = "socks5h://127.0.0.1:9050"


def check_link(url: str, title: str, desc: str) -> Optional[OnionLink]:
    try:
        resp = requests.get(url, proxies=dict(http=tor_socks, https=tor_socks), headers=headers)
        if resp.status_code == 200:
            ol = OnionLink(url, title, desc)
            print(ol)
            return ol
    except requests.exceptions.ConnectionError:
        pass
    return None


if __name__ == "__main__":
    onion_links = []
    try:
        resp = requests.get('http://zqktlwi4fecvo6ri.onion/wiki/index.php/Main_Page',
                            proxies=dict(http=tor_socks, https=tor_socks), headers=headers)
        webpage = html.fromstring(resp.content)
        hrefs = webpage.xpath('//a/@href')
        onion_links = set()
        for ref in hrefs:
            tmp_url = urlparse(ref)
            if tmp_url.scheme in ["http", "https"] and tmp_url.hostname.endswith(".onion"):  # it is an onion link
                for a in webpage.xpath("//a[@href='{}']".format(ref)):
                    title = a.text
                    desc = a.tail
                    if desc is not None:
                        desc = desc.replace(" - ", "")
                    onion_links.add((ref, title, desc))
    except requests.exceptions.ConnectionError as e:
        print("Wiki connection failed! Exception: ", str(e))

    if onion_links:
        with Pool(processes=os.cpu_count()) as pool:
            active_onion_links = pool.starmap(check_link, onion_links)
