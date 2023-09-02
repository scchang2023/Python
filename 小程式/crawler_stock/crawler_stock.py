import requests
import threading
alert_condtions = [
    {'ch':'t00.tw',
     'down_point':[10, True],
     'up_point':[10, True]},
    {'ch':'2891.tw',
     'down_percent':[0.1, False],
     'up_percent':[0.1, False]},
    {'ch':'00878.tw',
     'down_percent':[0.1, False],
     'up_percent':[0.1, False]},       
    ]
def download_stock():
    url = "https://mis.twse.com.tw/stock/api/getStockInfo.jsp?json=1&delay=0&ex_ch=tse_t00.tw|tse_2891.tw|tse_00878.tw"
    response = requests.get(url)
    if response.status_code == 200:
        stock = response.json()
        return stock
    else:
        return False
def check_stock_alert(stock):
    #print(stock)
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
                if 'down_point' in j:
                    val = abs(z-y)
                    if z < y and val > j['down_point'][0] and j['down_point'][1] == True:
                        print(f"{n}: 目前 {z} 點, 大跌 {round(val,2)} 點")
                if 'up_point' in j:
                    val = abs(z-y)
                    if z > y and val > j['up_point'][0] and j['up_point'][1] == True:
                        print(f"{n}: 目前 {z} 點, 大漲 {round(val,2)} 點")
                if 'down_percent' in j:
                    val = abs((y-z)/y*100)
                    if z < y and val > j['down_percent'][0] and j['down_percent'][1] == True:
                        print(f"{n}: 目前 {z} 點, 大跌 {round(val,2)} 趴")
                if 'up_percent' in j:
                    val = abs((y-z)/y*100)
                    if z > y and val > j['up_percent'][0] and j['up_percent'][1] == True:
                        print(f"{n}：目前 {z} 點, 大漲 {round(val,2)} 趴")

def is_in_trade_datetime(stock:dict)->bool:
    sys_date = stock['queryTime']['sysDate']
    sys_time = stock['queryTime']['sysTime']
    trade_date = stock['msgArray'][0]['d']
    if sys_date == trade_date and sys_time >= "09:00:00" and sys_time <= "13:30:00":
        print("在交易時間內")
        return True
    print("非交易時間內")
    return False

def dowload_stock_tmr():
    stock = download_stock()
    if stock!= False:
        print("下載成功")
        if is_in_trade_datetime(stock) == True:
            check_stock_alert(stock)
    else:
        print("下載失敗")
    t = threading.Timer(5, dowload_stock_tmr)
    t.start()

def main():
    dowload_stock_tmr()

if __name__ == "__main__":
    main()







