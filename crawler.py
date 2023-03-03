import urllib.request as req
import bs4
# 目標網址 ptt 電影版 (取得前5頁的資訊)
url = "https://www.ptt.cc/bbs/movie/index.html"
# header 資訊
header = {
    "User-Agent":"Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Mobile Safari/537.36"
}
data = ""
# 取得前5個目標網頁
for index in range(5):
    # 建立request物件, 加入header資訊 避免被網頁檔下
    request = req.Request(url, headers=header)
    # 獲取網頁資訊
    with req.urlopen(request) as response:
        data += response.read().decode("utf-8")

    # 取得上一頁的 url (透過html text 尋找到 a標籤的連結href)
    thisPageHtml = bs4.BeautifulSoup(data, "html.parser")
    lastPageHref = thisPageHtml.find("a", string="‹ 上頁")
    url = "https://www.ptt.cc"+lastPageHref["href"]

# 解析HTML原始碼 取得文章標題
# 使用 BeautifulSoup 來做HTML的解析
root = bs4.BeautifulSoup(data, "html.parser")
# 文章標題是在class=title div標籤 中的 a標籤中的文字
titles = root.find_all("div", class_="title")  # 尋找class="title" 的 所有 div 標籤 回傳一個列表
# 將標題存至txt檔案
with open("titledata.txt", mode="w", encoding="utf-8") as file:
    for title in titles:
        if title.a != None:  # 有些標題已經被刪除 要先檢查
            file.write(title.a.string + "\n")

