import urllib.request
import re

try:
    url = "https://www.bocra.org.bw/"
    html = urllib.request.urlopen(url, timeout=10).read().decode("utf-8")
    # All internal links
    links = re.findall(r'href="(/[^"]+)"', html)
    print("ALL INTERNAL LINKS FOUND:")
    for l in sorted(set(links)):
        if "univers" in l.lower() or "portab" in l.lower() or "domain" in l.lower() or "project" in l.lower():
            print(f"https://www.bocra.org.bw{l}")
except Exception as e:
    print(e)
