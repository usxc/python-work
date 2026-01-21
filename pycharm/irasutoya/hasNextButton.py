from __future__ import annotations

import requests
from bs4 import BeautifulSoup


def hasNextButton(url: str, *, timeout: int = 15) -> bool:
    headers = {
        "User-Agent": "Mozilla/5.0 (compatible; hasNextButton/1.0; +https://example.invalid)",
    }
    r = requests.get(url, headers=headers, timeout=timeout)
    r.raise_for_status()

    soup = BeautifulSoup(r.content, "html.parser")

    # 1) <head> の rel="next" を優先（テーマによって安定）
    if soup.find("link", rel=lambda v: v and "next" in v):
        return True

    # 2) Bloggerのページャ（次ページは older-link 扱いが多い）
    pager = soup.find(id="blog-pager") or soup.find(class_="blog-pager")
    if pager:
        if pager.select_one("a.blog-pager-older-link"):
            return True
        if pager.select_one("#blog-pager-older-link a"):
            return True
        if pager.select_one("a#blog-pager-older-link"):
            return True

    # 3) フォールバック：ページ全体から探す
    if soup.select_one("a.blog-pager-older-link"):
        return True
    if soup.select_one("#blog-pager-older-link a"):
        return True
    if soup.select_one("a#blog-pager-older-link"):
        return True

    return False


if __name__ == "__main__":
    test_url = "https://www.irasutoya.com/search?q=%E5%AF%BF%E5%8F%B8&max-results=20&start=0&by-date=false"
    try:
        print("hasNextButton:", hasNextButton(test_url))
    except Exception as e:
        print("ERROR:", e)
