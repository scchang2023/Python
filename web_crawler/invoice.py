import requests
from bs4 import BeautifulSoup
url = 'https://invoice.etax.nat.gov.tw/index.html'
web = requests.get(url)    # 取得網頁內容
web.encoding='utf-8'       # 因為該網頁編碼為 utf-8，加上 .encoding 避免亂碼
# print(web.text)
soup = BeautifulSoup(web.text, "html.parser") # 轉換成標籤樹
print(soup)