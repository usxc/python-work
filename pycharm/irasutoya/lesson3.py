import requests
from bs4 import BeautifulSoup
import urllib.parse
from pathlib import Path
import time


# 検索結果URLから詳細ページURL一覧を作る
def readResultHtml(resultUrl):
    html = requests.get(resultUrl)
    soup = BeautifulSoup(html.content, "html.parser")

    result = soup.find(class_="widget Blog")

    urls = []

    # すべてのaタグを検索して、リンクを表示する
    for element in result.find_all("a"):
        href = element.get("href")
        if href is None:
            continue

        url = urllib.parse.urljoin(resultUrl, href)

        # 正規表現を使えばもっとシンプルに書ける
        if "/blog-post_" in url:
            # if "/blog-post_" in url and not "#comment" in url:
            urls.append(url)  # リストを使う場合の追加
            # urls.add(url) # 重複を除外する セットを使う場合
        else:
            pass
            # print("NG-URL >> " + url)

    # 重複除外（順序維持）
    unique_urls = []
    seen = set()
    for url in urls:
        if url not in seen:
            unique_urls.append(url)
            seen.add(url)

    return unique_urls


# 詳細画面から、最終目的である画像URLを取得する関数
#引数
# url … 詳細画面のURL
#戻り値
# 画像URL
def getImageUrl(url):
    # Webページを取得して解析する
    html = requests.get(url)
    soup = BeautifulSoup(html.content, "html.parser")

    # まとめても書けるけど、わかりやすくするために分割してアクセスする。
    entry = soup.find(class_="entry")
    #print(entry)

    img = entry.find("img")
    #print(img)

    src = img.get("src")
    #print(src)

    # URLにHTTPSがない場合は追加する
    if not "https:" in src:
        src = "https:" + src

    return src


# 入力された画像URLをローカルにダウンロードする
# 引数
# url 画像URL
# dir 保存先URL
# 戻り値 なし
# 画像ファイル名はWebのものを採用するバージョン
def downloadImage(url, dir):
    filename = url.split("/")[-1]
    fullpath = dir.joinpath(filename)

    imgdata = requests.get(url)
    with open(fullpath, mode="wb") as f:
        f.write(imgdata.content)


def main():
    # ※ブラウザから取得した検索結果URL（token削除済み）を使う
    # 例:
    # resultUrl = "https://www.irasutoya.com/search?q=%E3%82%B9%E3%82%A4%E3%82%AB"
    resultUrl = "https://www.irasutoya.com/search?q=%E3%82%B9%E3%82%A4%E3%82%AB"

    # 1) 検索結果 → 詳細ページURL一覧
    detail_urls = readResultHtml(resultUrl)
    print(f"詳細ページURL数: {len(detail_urls)}")

    # 2) 詳細ページURL一覧 → 画像URL一覧
    image_urls = []
    for detail_url in detail_urls:
        try:
            image_url = getImageUrl(detail_url)
            image_urls.append(image_url)
            print("imageUrl =", image_url)
        except Exception as e:
            print("getImageUrl失敗:", detail_url, e)

    # 重複除外（順序維持）
    unique_image_urls = []
    seen = set()
    for u in image_urls:
        if u not in seen:
            unique_image_urls.append(u)
            seen.add(u)

    print(f"画像URL数: {len(unique_image_urls)}")

    # 3) 画像URL一覧 → 全ダウンロード
    downloadDir = Path("download")
    downloadDir.mkdir(exist_ok=True)

    for img_url in unique_image_urls:
        try:
            downloadImage(img_url, downloadDir)
            print("Downloaded:", img_url)
        except Exception as e:
            print("downloadImage失敗:", img_url, e)

        time.sleep(1)  # 負荷回避
