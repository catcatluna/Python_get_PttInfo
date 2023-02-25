import urllib.request as req
# 目標網址 ptt 電影版
url = "https://www.ptt.cc/bbs/movie/index.html"
# 加入header資訊 避免被網頁檔下
request = req.Request(url, headers={
    "User-Agent":"Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Mobile Safari/537.36"
})
# 獲取網頁資訊
with req.urlopen(request) as response:
    data = response.read().decode("utf-8")

print(data)
