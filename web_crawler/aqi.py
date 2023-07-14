import requests
url = 'https://data.epa.gov.tw/api/v2/aqx_p_432?api_key=e8dd42e6-9b8b-43f8-991e-b3dee723a52d&limit=1000&sort=ImportDate%20desc&format=JSON'
data = requests.get(url) # 使用 get 方法透過空氣品質指標 API 取得內容
print(data)
data_json = data.json()
for i in data_json['records']:  # 依序取出 records 內容的每個項目
    print(f"{i['county']}{i['sitename']}, AQI: {i['aqi']}, 空氣品質{i['status']}")
