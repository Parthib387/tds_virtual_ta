import requests
from bs4 import BeautifulSoup
import json

def scrape_posts():
    base = "https://discourse.onlinedegree.iitm.ac.in"
    url = f"{base}/c/courses/tools-in-data-science/"
    posts = []
    resp = requests.get(url)
    soup = BeautifulSoup(resp.text, "html.parser")
    for link in soup.select(".topic-title"):
        title = link.get_text(strip=True)
        href = link["href"]
        posts.append({
            "title": title,
            "url": base + href,
            "content": ""  # optionally scrape the thread page too
        })
    with open("discourse_data.json", "w") as f:
        json.dump(posts, f, indent=2)

if __name__ == "__main__":
    scrape_posts()
