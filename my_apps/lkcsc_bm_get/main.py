# ====== use with chrome and selenium 4 ===
# 參考 https://pypi.org/project/webdriver-manager/
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
# =========================================

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

USER_NAME = "Fxxxxxx"
USER_PASSWORD = "xxxxxx"

import time
# https://pypi.org/project/webdriver-manager/
# chromedriver 去這下載
# https://googlechromelabs.github.io/chrome-for-testing/
def create_chrome_driver()->webdriver:
    options = Options()
    # options.add_argument("--headless")
    # use with chrome
    dr = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))
    return dr

def close_chrome_driver(dr:webdriver)->None:
    dr.close()

def login_lkcsc_page(dr:webdriver)->None:
    print("連線至會員登入頁面")
    # dr.get("https://scr.cyc.org.tw/tp17.aspx?module=login_page&files=login")
    dr.get("https://scr.cyc.org.tw/tp17.aspx#")
    member_login = dr.find_element(By.ID, "member_login")
    time.sleep(3)
    print("======== 1")
    member_login.click()
    time.sleep(3)
    print("======== 2")
    dr.switch_to.alert.accept()
    time.sleep(3)
    print("======== 3")
    dr.switch_to.alert.accept()
    time.sleep(3)
    print("======== 4")
    ok_btn = dr.find_element(By.CLASS_NAME, "swal2-confirm swal2-styled")
    ok_btn.click()
    time.sleep(3)
  
    # print("自動輸入帳密並登入")
    # username_input = dr.find_element(By.ID, "ContentPlaceHolder1_loginid")
    # password_input = dr.find_element(By.ID, "loginpw")
    # username_input.send_keys(USER_NAME)
    # password_input.send_keys(USER_PASSWORD)
    # btn_singin = dr.find_element(By.ID, "login_but")
    # btn_singin.send_keys(Keys.ENTER)



# def get_meters_management(dr:webdriver)->list:
#     print("連線至水錶管理頁面")
#     dr.get("http://www.cnyiot.com/MMpublicw.aspx")
#     time.sleep(3)
#     print("取得水錶管理")
#     meter_element = dr.find_element(By.ID, "table1")
#     time.sleep(3)
#     # print(meter_element.text)
#     meter_element_list = meter_element.text.splitlines()
#     meter_element_list = meter_element_list[9:]
#     # print(meter_element_list)
#     data = []
#     for i in meter_element_list:
#         meter_item={}
#         i = i.replace("在线 （通水 )","在线(通水)")
#         i = i.split(' ')
#         meter_item['水錶名稱'] = i[0]
#         meter_item['水錶號碼'] = i[1]
#         meter_item['總水量'] = i[5]
#         meter_item['狀態'] = i[6]
#         meter_item['供電方式'] = i[7]
#         data.append(meter_item)
#     print(data)
#     return data


def main():
    driver = create_chrome_driver()
    login_lkcsc_page(driver)
    # meters_management = get_meters_management(driver)
    # close_chrome_driver(driver)

if __name__ == "__main__":
    main()