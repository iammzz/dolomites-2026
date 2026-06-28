import requests
import re
import glob
import sys

def get_urls_from_files():
    urls = set()
    for file in glob.glob("*.md"):
        with open(file, 'r') as f:
            content = f.read()
            # Extract URLs
            found = re.findall(r'https?://[^\s)\]"\']+', content)
            urls.update(found)
    return sorted(list(urls))

broken = []
urls = get_urls_from_files()
print(f"Testing {len(urls)} URLs...")

headers = {'User-Agent': 'Mozilla/5.0'}

for url in urls:
    try:
        res = requests.get(url, headers=headers, timeout=5, allow_redirects=True)
        if res.status_code >= 400:
            broken.append((url, res.status_code))
    except Exception as e:
        broken.append((url, str(e)))

print("\n--- BROKEN LINKS ---")
for url, err in broken:
    print(f"{err}: {url}")
