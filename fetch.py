import urllib.request
import re
try:
    url = "https://www.bocra.org.bw/news%26events"
    html = urllib.request.urlopen(url, timeout=10).read().decode("utf-8")
    # Finding title tags inside the news page. Usually <a href="/node/xxx">Title</a> or similar
    articles = re.findall(r'<a href="(/[^"]+)"[^>]*>([^<]+)</a>', html)
    print("Articles:")
    unique_links = set()
    for link, title in articles:
        title = title.strip()
        if len(title) > 20 and link not in unique_links and "bocra" not in link.lower() and "privacy" not in link.lower():
            unique_links.add(link)
            print(f"TITLE: {title}")
            print(f"LINK: https://www.bocra.org.bw{link}\n")
except Exception as e:
    print(e)
