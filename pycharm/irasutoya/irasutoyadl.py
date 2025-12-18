import requests
from bs4 import BeautifulSoup


def getImageUrl(page_url):
    response = requests.get(page_url)
    response.encoding = response.apparent_encoding

    soup = BeautifulSoup(response.text, 'html.parser')

    post_body = soup.find('div', class_='post-body')

    if post_body:
        img_tag = post_body.find('img')

        if img_tag:
            img_url = img_tag.get('src')
            return img_url

    return None


def downloadImage(i_url):
    # 画像データを取得
    response = requests.get(i_url)

    # URLからファイル名を取得 (URLの最後の部分)
    filename = i_url.split('/')[-1]

    # ファイルに保存 (バイナリモードで書き込み)
    with open(filename, 'wb') as f:
        f.write(response.content)

    print(f"ダウンロード完了: {filename}")


if __name__ == "__main__":
    detail_page_url = "https://www.irasutoya.com/2020/09/blog-post_647.html"

    image_url = getImageUrl(detail_page_url)

    print(f"ページURL: {detail_page_url}")
    print(f"画像URL:   {image_url}")

    if image_url:
        downloadImage(image_url)
        print("※ カレントディレクトリに画像ファイルが保存されました")
    else:
        print("画像URLが取得できませんでした")
