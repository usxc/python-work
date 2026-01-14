import requests
from bs4 import BeautifulSoup
import urllib.parse
from pathlib import Path


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


# detailPageUrl = "https://www.irasutoya.com/2018/03/blog-post_83.html" 
detailPageUrl = "https://www.irasutoya.com/2020/08/blog-post_112.html"

imageUrl = getImageUrl(detailPageUrl)
print("imageUrl = " + imageUrl)

downloadDir = Path(f"download")
downloadDir.mkdir(exist_ok=True)

downloadImage(imageUrl, downloadDir)
