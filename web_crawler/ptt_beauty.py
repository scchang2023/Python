import requests
from bs4 import BeautifulSoup
web = requests.get('https://www.ptt.cc/bbs/Beauty/M.1638380033.A.7C7.html', cookies={'over18':'1'})
# print(web.text, type(web.text))
soup = BeautifulSoup(web.text, "html.parser")   # 使用 BeautifulSoup 取得網頁結構
# print(soup, type(soup))
imgs = soup.find_all('img')
print(imgs)
name = 0    #  設定圖片編號
for i in imgs:
    print(i['src'])
    jpg = requests.get(i['src'])     # 使用 requests 讀取圖片網址，取得圖片編碼
    print(jpg)
    f = open(f'./test_{name}.jpg', 'wb')    # 使用 open 設定以二進位格式寫入圖片檔案
    f.write(jpg.content)   # 寫入圖片的 content
    f.close()              # 寫入完成後關閉圖片檔案
    name = name + 1        # 編號增加 1
