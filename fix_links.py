import urllib.request
import re
import glob

# Try to find the correct URLs from earthtrekkers sitemap
url = "https://www.earthtrekkers.com/post-sitemap.xml"
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
try:
    with urllib.request.urlopen(req) as response:
        sitemap = response.read().decode('utf-8')
except Exception as e:
    print(f"Error fetching sitemap: {e}")
    sitemap = ""

urls = re.findall(r'<loc>(https://www.earthtrekkers.com/[^<]+)</loc>', sitemap)
print(f"Found {len(urls)} URLs in sitemap")

# Filter for dolomites
dolomites_urls = [u for u in urls if 'dolomites' in u or 'funes' in u or 'seceda' in u or 'marmolada' in u or 'alpe-di-siusi' in u or 'boe' in u or 'munkel' in u]
for u in dolomites_urls:
    print(u)

