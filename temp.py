from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.select import Select
import time

url ='https://cip.asia.edu.tw/login.php'

browser=webdriver.Chrome('D:\webdriver\chromedriver')
browser.get(url) 

try:
# login
    time.sleep(1)
    element = browser.find_element_by_xpath("//*[@id=\"main\"]/div[1]/input") # 定位學號
    time.sleep(1)
    element.send_keys('105021007') # 輸入學號
    time.sleep(1)
    element = browser.find_element_by_xpath("//*[@id=\"main\"]/div[2]/input")  # 定位密碼
    element.send_keys('*******') # 輸入密碼
    time.sleep(1)
    browser.find_element_by_xpath("//*[@id=\"main\"]/ul[1]/li[1]/a").click() # 按下確認鍵
    print("登入成功")
    time.sleep(5)
# dosomething
    browser.find_element_by_xpath("//*[@id=\"main_table\"]/div[2]/div/div[2]/a/font").click()
    time.sleep(6)
    try:
        browser.find_element_by_xpath("//input[@value='查詢(Query)']").click() # 按下查詢
        time.sleep(60)
    finally:
        print("抓取按鈕錯誤")

finally:
    browser.quit()