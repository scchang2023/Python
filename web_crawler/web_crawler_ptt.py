import requests
from bs4 import BeautifulSoup
url = 'https://www.ptt.cc/'
# 加入 Cookies 資訊
web = requests.get('https://www.ptt.cc/bbs/Gossiping/index.html', cookies={'over18':'1'})
# print(web.text)
web.encoding='utf-8' # 避免中文亂碼
soup = BeautifulSoup(web.text, "html.parser")
titles = soup.find_all('div', class_='title')     # 取得 class 為 title 的 div 內容
output = '' # 建立 output 變數
#print(titles)
for i in titles:
    if i.find('a') != None: # 判斷如果不為 None
        # print(i.find('a').get_text()) # 取得 div 裡 a 的內容，使用 get_text() 取得文字
        # print(url + i.find('a')['href'], end='\n\n') # 使用 ['href'] 取得 href 的屬性
        # 將資料一次記錄到 output 變數裡
        output = output + i.find('a').get_text() + '\n' + url + i.find('a')['href'] + '\n\n'
print(output)
f = open('./gossip.txt','w') # 建立並開啟純文字文件 ( Colab 才需要 )
f.write(output) # 將資料寫入檔案裡
f.close()