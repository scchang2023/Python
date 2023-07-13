import requests
url = 'https://data.epa.gov.tw/api/v2/aqx_p_432?api_key=e8dd42e6-9b8b-43f8-991e-b3dee723a52d&limit=1000&sort=ImportDate%20desc&format=JSON'
data = requests.get(url) # 使用 get 方法透過空氣品質指標 API 取得內容
print(data)
data_json = data.json()
for i in data_json['records']:  # 依序取出 records 內容的每個項目
    print(i['county'] + ' ' + i['sitename'], end='，')  # 印出城市與地點名稱
    print('AQI:' + i['aqi'], end='，')                  # 印出 AQI 數值
    print('空氣品質' + i['status'])                         # 印出空氣品質狀態
