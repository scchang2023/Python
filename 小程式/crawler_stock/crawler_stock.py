import requests
import threading
alert_condtions = [
    {'ch':'t00.tw',
     'down_point':[10, True],
     'up_point':[10, True]},
    {'ch':'2891.tw',
     'down_point':[0.01, True],
     'up_point':[0.01, True]},     
    ]
def download_stock():
    url = "https://mis.twse.com.tw/stock/api/getStockInfo.jsp?json=1&delay=0&ex_ch=tse_t00.tw|tse_2891.tw"
    response = requests.get(url)
    if response.status_code == 200:
        stock = response.json()
        return stock
    else:
        return False
def check_stock_alert(stock):
    print(stock)
    for i in stock['msgArray']:
        if not ('y' in i and 'z' in i):
            print("less some stock keys")
            continue
        n = i['n']
        ch = i['ch']        
        if i['z'] == '-':
            print(f"{n}: There is no z value")
            continue
        y = float(i['y'])
        z = float(i['z'])
        for j in alert_condtions:
            if ch == j['ch']:
                if z <= y and y-z >= j['down_point'][0] and j['down_point'][1] == True:
                    print(f"{n}: 目前 {z}, 大跌 {y-z}")
                elif z >= y and z-y >= j['up_point'][0] and j['up_point'][1] == True:
                    print(f"{n}：目前 {z}, 大漲 {z-y}")

def dowload_stock_tmr():
    stock = download_stock()
    if stock!= False:
        print("下載成功")
        check_stock_alert(stock)
    else:
        print("下載失敗")
    t = threading.Timer(5, dowload_stock_tmr)
    t.start()

def main():
    dowload_stock_tmr()

if __name__ == "__main__":
    main()







