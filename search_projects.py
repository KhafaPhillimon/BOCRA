import urllib.request
import re

def find_links(keywords):
    try:
        url = "https://www.bocra.org.bw/"
        html = urllib.request.urlopen(url, timeout=10).read().decode("utf-8")
        links = re.findall(r'href="(/[^"]+)"', html)
        found = {}
        for link in links:
            for kw in keywords:
                if kw.lower().replace(" ", "-") in link.lower() or kw.lower().replace(" ", "") in link.lower():
                    found[kw] = "https://www.bocra.org.bw" + link
        return found
    except Exception as e:
        return str(e)

keywords = ["Number Portability", "Digital Switchover", "DSO", "Domain", ".bw", "UASF"]
print(find_links(keywords))
