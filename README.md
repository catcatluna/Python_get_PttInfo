# Python_get_PttInfo
[python] 使用內建urllib函式庫及BeautifulSoup 獲得ptt 電影版標題資訊

## Code 說明
### import
* urllib  
```
import urllib.request as request
```
python 內建函式庫 用來獲得網頁資料  
* BeautifulSoup
```
import bs4
```  
bs4 是用來方便解析HTML原始碼 取得我們想要的資訊

### Headers 
* User-Agent  
```
request = req.Request(url, headers={
    "User-Agent":"Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Mobile Safari/537.36"
})
```
開發人員工具 (或是直接按F12) - Network - 重新開啟網頁後 找到index.html - 尋找到Request Headers 的user-agent   
為了要向目標網頁模擬我們使用的裝置 所以要將代表裝置的user-agent代入參數 這樣才不會被網頁拒絕  
<img src="https://user-images.githubusercontent.com/107610680/222087210-6a58fb4f-88f0-4b08-b502-0b7664a99e02.png" width="80%">




## 資料來源
[Python 網路連線程式、公開資料串接 By 彭彭](Python 網路爬蟲 Web Crawler 基本教學 By 彭彭)