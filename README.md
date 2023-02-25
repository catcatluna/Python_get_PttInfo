# Python_get_PttInfo
[python] 使用內建urllib函式庫 獲得ptt 電影版資訊

## Code 說明
### import
* urllib  
```
import urllib.request as request
```
python 內建函式庫 用來獲得網頁資料
  
### Headers 
* User-Agent  
```
request = req.Request(url, headers={
    "User-Agent":"Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Mobile Safari/537.36"
})
```
開發人員工具 (或是直接按F12) - Network - 重新開啟網頁後 找到index.html - 尋找到Request Headers 的user-agent   
為了要向目標網頁模擬我們使用的裝置 所以要將代表裝置的user-agent代入參數 這樣才不會被網頁拒絕



## 資料來源
[Python 網路連線程式、公開資料串接 By 彭彭](Python 網路爬蟲 Web Crawler 基本教學 By 彭彭)
