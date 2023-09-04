import requests
import threading
alert_condtions = [
    {
        'ch':'t00.tw',
        'th_max':[[300, 200, 100, 50],[False, False, False, False]],
        'th_max_en':True,
        'th_min':[[-300, -200, -100, -50],[False, False, False, False]],
        'th_min_en':True,
        'th_type':'point'
    },
    {
        'ch':'00878.tw',
        'th_max':[[2, 1],[False, False]],
        'th_max_en':False,
        'th_min':[[-2, -1],[False, False]],
        'th_min_en':False,
        'th_type':'percent'
    }
]

def reset_alert_conditions(cond:dict):
    print("reset_alert_conditions")
    for i in cond:
        j = 0
        for _ in i['th_max'][1]:
            i['th_max'][1][j] = False
            j=j+1
        j = 0
        for _ in i['th_min'][1]:
            i['th_min'][1][j] = False
            j=j+1            

def download_stock():
    url = "https://mis.twse.com.tw/stock/api/getStockInfo.jsp?json=1&delay=0&ex_ch=tse_t00.tw"
    response = requests.get(url)
    if response.status_code == 200:
        stock = response.json()
        return stock
    else:
        return False

def check_stock_alert(stock:dict)->str:
    #print(stock)
    msg = ''
    for i in stock['msgArray']:
        if not ('y' in i and 'z' in i):
            print("There is no key 'y' or 'z'")
            continue
        n = i['n']
        ch = i['ch']
        if i['z'] == '-':
            print(f"{n}: There is no 'z' value")
            continue
        y = float(i['y'])
        z = float(i['z'])
        for j in alert_condtions:
            if ch == j['ch']:
                if j['th_type'] == 'percent':
                    val = round((z-y)/y*100, 2)
                else:
                    val = round(z-y,2)
                print(f"ch = {ch}, val = {val}, {j['th_type']}, th_min_en = {j['th_min_en']}, th_max_en = {j['th_max_en']}")
                if j['th_max_en'] == True:
                    k = 0
                    if val>0:
                        for th in j['th_max'][0]:
                            alerted = j['th_max'][1][k]
                            print(f"th = {th}, alerted = {alerted}")
                            if alerted == True:
                                break
                            if val > th:
                                if j['th_type'] == 'percent':
                                    str = f"{n}: 目前 {z} 點, 大漲 {val} 趴\n"
                                else:
                                    str = f"{n}: 目前 {z} 點, 大漲 {val} 點\n"
                                #print(str)
                                msg+=str
                                j['th_max'][1][k] = True
                                break
                            k = k+1
                if j['th_min_en'] == True:
                    k = 0
                    if val<0:
                        for th in j['th_min'][0]:
                            alerted = j['th_min'][1][k]
                            print(f"th = {th}, alerted = {alerted}")
                            if alerted == True:
                                break
                            if val < th:
                                if j['th_type'] == 'percent':
                                    str = f"{n}: 目前 {z} 點, 大跌 {abs(val)} 趴\n"
                                else:
                                    str = f"{n}: 目前 {z} 點, 大跌 {abs(val)} 點\n"
                                #print(str)
                                msg+=str
                                j['th_min'][1][k] = True
                                break
                            k = k+1
    return msg

def is_in_trade_datetime(stock:dict)->bool:
    sys_date = stock['queryTime']['sysDate']
    sys_time = stock['queryTime']['sysTime']
    trade_date = stock['msgArray'][0]['d']
    print(f"system datetime [{sys_date} {sys_time}]")
    if sys_date == trade_date and sys_time >= "09:00:00" and sys_time <= "13:30:00":
        print("股市交易時間內")
        return True
    print("非股市交易時間內")
    return False

def send_line_notify(msg:str)->requests.Response:
    url = 'https://notify-api.line.me/api/notify'
    # 個人測試
    # token = 'r0OHCGAS0B06PrOPEudaMFk2ugFIQAcqDYDHazRiJxF'
    # FISS
    token = 'yqB6couCMQlCtBDJpJb2nEw8yRepyeo8SWjQZJDDsqD'
    headers = {
        'Authorization': 'Bearer ' + token, # 設定權杖
    }
    params = {
        'message': msg # 設定要發送的訊息
    }
    return requests.post(url, headers=headers, params=params) # 使用 post 方法

def send_stock_msg_line_notify(msg:str)->requests.Response:
    msg = "\n" + msg
    return send_line_notify(msg)

pre_state_in_stock = False
def dowload_stock_tmr():
    stock = download_stock()
    if stock!= False:
        print("下載成功")
        cur_state_in_stock = is_in_trade_datetime(stock)
        global pre_state_in_stock
        if cur_state_in_stock == True:
            if  pre_state_in_stock == False:
                reset_alert_conditions(alert_condtions)
            msg = check_stock_alert(stock)
            print(msg)
            if msg != '':
                send_stock_msg_line_notify(msg)
        pre_state_in_stock = cur_state_in_stock
    else:
        print("下載失敗")
    t = threading.Timer(30, dowload_stock_tmr)
    t.start()

def main():
    dowload_stock_tmr()

if __name__ == "__main__":
    main()