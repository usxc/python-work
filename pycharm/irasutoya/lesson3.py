import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin


def readResultHtml(targetUrl, urls):
    html = requests.get(targetUrl)
    soup = BeautifulSoup(html.content, "html.parser")

    result = soup.find(class_="widget Blog")

    # すべてのaタグを検索して、リンクを表示する
    for a_tag in result.find_all("a"):
        url = urljoin(targetUrl, a_tag.get("href"))

        # 正規表現を使えばもっとシンプルに書ける
        if "/blog-post_" in url:
            # if "/blog-post_" in url and not "#comment" in url:
            urls.append(url)  # リストを使う場合の追加
            # urls.add(url) # 重複を除外する セットを使う場合
        else:
            pass
            # print("NG-URL >> " + url)


def main():
    # Webページを取得して解析する
    targetUrl = "https://www.irasutoya.com/search?q=%E3%82%B9%E3%82%A4%E3%82%AB"

    urls = []  # リスト

    # 詳細画面一覧のURLリストが作成されます
    readResultHtml(targetUrl, urls)

    print(urls)
