from selenium.webdriver.common.by import By
from selenium import webdriver
import time
import json
from bs4 import BeautifulSoup
import csv
import os
import re
import requests
import json
import pandas as pd
import numpy as np
import time, datetime
import random
from lxml import etree
import csv
data_list = []  # 设置全局变量来存储数据
html = ""
def get_first(page_star,page_end):
    if not os.path.exists('taishiji1.html'):
        driver = webdriver.Chrome()
        # 初次建立连接，随后方可修改cookie
        driver.get('https://www.jd.com/')
        # 删除第一次建立连接时的cookie
        driver.delete_all_cookies()
        # 读取登录时存储到本地的cookie
        with open('cookies.txt', 'r') as f:
            cookies_list = json.load(f)
            for cookie in cookies_list:
                if isinstance(cookie.get('expiry'), float):
                    cookie['expiry'] = int(cookie['expiry'])
                driver.add_cookie(cookie)
        # 再次访问页面，便可实现免登陆访问
        driver.refresh()
        # kw  搜索关键字
        kw = ['台式机']
        # selenium 元素查找find_element_by_id方法，找到元素后输入信息
        search_block = driver.find_element(By.ID, 'key')
        time.sleep(3)
        search_block.send_keys(kw)
        ##su点击搜索~
        enter_button = driver.find_element(By.CLASS_NAME, 'button')
        enter_button.click()
        time.sleep(3)

        driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
        time.sleep(5)
        kw1 = [str(page_star - 1)]
        # selenium 元素查找find_element_by_id方法，找到元素后输入信息
        search_block = driver.find_element(By.XPATH, '//*[@id="J_bottomPage"]/span[2]/input')
        time.sleep(3)
        try:
            search_block.clear()
            print('成功清空输入框')
        except Exception as e:
            print('fail清空输入框')
        search_block.send_keys(kw1)
        time.sleep(5)
        ##su点击搜索~
        enter_button1 = driver.find_element(By.XPATH, '//*[@id="J_bottomPage"]/span[2]/a')
        print(enter_button1)
        enter_button1.click()
        time.sleep(3)
        driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
        time.sleep(5)
        element = driver.find_element(By.XPATH, '//*[@id="J_bottomPage"]/span[1]/a[6]')
        driver.execute_script("arguments[0].click();", element)
        time.sleep(3)
        driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
        time.sleep(10)
        for i in range(page_star,page_end+1):
            element = driver.find_element(By.XPATH, '//*[@id="J_bottomPage"]/span[1]/a[9]')
            driver.execute_script("arguments[0].click();", element)
            time.sleep(3)
            driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
            time.sleep(10)
            # print(driver.current_url)
            html = driver.page_source
            with open('taishiji1.html', 'a', encoding='utf-8') as f:
                f.write(html)
                f.flush()
        html = open('taishiji1.html', encoding='utf-8').read()
        driver.quit()
    else:
        html = open('taishiji1.html', encoding='utf-8').read()
    return html
def get_info(href):
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.56",
        "referer": "https://item.jd.com/",
        "cookie": "__jdu=16591170929141554292632; shshshfpa=07db6877-b40f-0fcb-d992-f957c6d56b70-1666282711; shshshfpb=raKDDLO9C0GGt6MQsAnfVHw; unpl=JF8EALRnNSttXR9RAUkFHBVHTQ9dWw1cQx4Ab25QBwoLGFJVHgpPGhR7XlVdXhRLFx9vZBRXXlNIVw4aAisSEXteU11bD00VB2xXVgQFDQ8WUUtBSUt-SV5RXF4AQhQKam8BZG1bS2QFGjIbFRRDXVRYXABIHwNqZwFQWFtDVwIZASsTIExtZG5VCUgUAmpXBGRcaAkAWRMCHRcSShBUWVkASxcFbm8GXF1dS1ABHgETERdJXmRfbQs; __jdv=122270672|direct|-|none|-|1668930231242; areaId=6; PCSYCityID=CN_140000_140100_0; ipLoc-djd=6-303-305-5328; user-key=05170692-4648-4b5a-a8bc-55629bf64173; jsavif=0; __jda=122270672.16591170929141554292632.1659117092.1669727485.1669738803.12; __jdc=122270672; shshshfp=1436668152a28896b8229436931a05b5; token=e3364f4741b59587d1145477ab395989,2,927633; __tk=448744a36542f1d5a945422485a8d80d,2,927633; jsavif=0; shshshsID=a3b6e568133e39b2b3ca2d3cbe1f896b_4_1669739897797; __jdb=122270672.4.16591170929141554292632|12.1669738803; ip_cityCode=303; 3AB9D23F7A4B3C9B=OPKKSNI6BBCYTM7G6A3AO76MMA5YXCJJ56BENAXQZP644VSVBXCYGJQAHVWYNF2SDEMVAJQF2HAGBJ2EWGTLAHBF7Q"}
    response = requests.get(href, headers=headers)
    replies = response.text
    # print(replies)
    html = etree.HTML(replies)
    try:
        brand = html.xpath('//*[@id="parameter-brand"]/li/@title')[0]
    except:
        brand = ''
    try:
        name = html.xpath('//*[@id="detail"]/div[2]/div[1]/div[1]/ul[2]/li[1]/@title')[0]
    except:
        name = ''
    try:
        id = html.xpath('//*[@id="detail"]/div[2]/div[1]/div[1]/ul[2]/li[2]/@title')[0]
    except:
        id = ''
    try:
        message1 = html.xpath('//*[@id="detail"]/div[2]/div[1]/div[1]/ul[2]/li[3]/@title')[0]
    except:
        message1 = ''
    try:
        message2 = html.xpath('//*[@id="detail"]/div[2]/div[1]/div[1]/ul[2]/li[4]/@title')[0]
    except:
        message2 = ''
    try:
        message3 = html.xpath('//*[@id="detail"]/div[2]/div[1]/div[1]/ul[2]/li[5]/@title')[0]
    except:
        message3 = ''
    try:
        message4 = html.xpath('//*[@id="detail"]/div[2]/div[1]/div[1]/ul[2]/li[6]/@title')[0]
    except:
        message4 = ''
    try:
        message5 = html.xpath('//*[@id="detail"]/div[2]/div[1]/div[1]/ul[2]/li[7]/@title')[0]
    except:
        message5 = ''
    try:
        message6 = html.xpath('//*[@id="detail"]/div[2]/div[1]/div[1]/ul[2]/li[8]/@title')[0]
    except:
        message6 = ''
    try:
        message7 = html.xpath('//*[@id="detail"]/div[2]/div[1]/div[1]/ul[2]/li[9]/@title')[0]
    except:
        message7 = ''
    try:
        message8 = html.xpath('//*[@id="detail"]/div[2]/div[1]/div[1]/ul[2]/li[10]/@title')[0]
    except:
        message8 = ''
    try:
        message9 = html.xpath('//*[@id="detail"]/div[2]/div[1]/div[1]/ul[2]/li[11]/@title')[0]
    except:
        message9 = ''
    try:
        message10 = html.xpath('//*[@id="detail"]/div[2]/div[1]/div[1]/ul[2]/li[12]/@title')[0]
    except:
        message10 = ''
    try:
        message11 = html.xpath('//*[@id="detail"]/div[2]/div[1]/div[1]/ul[2]/li[13]/@title')[0]
    except:
        message11 = ''
    try:
        message12 = html.xpath('//*[@id="detail"]/div[2]/div[1]/div[1]/ul[2]/li[14]/@title')[0]
    except:
        message12 = ''
    try:
        message13 = html.xpath('//*[@id="detail"]/div[2]/div[1]/div[1]/ul[2]/li[15]/@title')[0]
    except:
        message13 = ''
    try:
        message14 = html.xpath('//*[@id="detail"]/div[2]/div[1]/div[1]/ul[2]/li[16]/@title')[0]
    except:
        message14 = ''
    try:
        message15 = html.xpath('//*[@id="detail"]/div[2]/div[1]/div[1]/ul[2]/li[17]/@title')[0]
    except:
        message15 = ''
    return id, brand, name, message1, message2, message3, message4, message5, message6, message7, \
           message8, message9, message10, message11, message12, message13, message14, message15
page_want_start=6
page_want_end=8
html=get_first(page_want_start,page_want_end)
def parse_html1(html):
    soup = BeautifulSoup(html, 'html.parser')
    # print(soup.find_all(name='div', attrs={'class': 'gl-i-wrap'}))
    num = 1
    for item in soup.find_all(name='div', attrs={'class': 'gl-i-wrap'}):
        data_dict = {}  # 定义一个字典存储数据
        href=[]
        price=(item.find(name='strong').get_text()).replace('￥', '').strip('\n')
        # print(price)
        name = (item.find(name='div', attrs={'class': 'p-name p-name-type-2'}))
        name1 =(name.find('em').get_text()).replace(' ', '').strip('\n')
        href_a=item.find('div',{'class':'p-name p-name-type-2'}).find_all('a',href = re.compile('//item.jd.com/'))
        for x in href_a:
            link=x.get('href')
        support=(item.find(name='div', attrs={'class': 'p-icons'}).get_text()).replace(' ', '').strip('\n')
        # print(support)
        if '自营' in support:
            support='是'
        else:
            support='否'
        # print(support)
        deal_cnt = item.find(name='div', attrs={'class': 'p-commit'}).get_text().replace('去看二手', '').strip('\n')
        # print(deal_cnt)
        data_dict["name"] = name1
        data_dict["href"]='https:'+link
        id, brand, name, message1, message2, message3, message4, message5, message6, message7, \
        message8, message9, message10, message11, message12, message13, message14, message15 = get_info(data_dict['href'])
        data_dict["price"]=price
        data_dict["support"]=support
        data_dict["deal_cnt"] = deal_cnt.replace('条评价', '')
        if '万+' in data_dict["deal_cnt"]:
            num1 = re.findall('(.*?)万+', data_dict["deal_cnt"])
            data_dict["deal_cnt"]=float(num1[0]) * 10000
        elif '+' in data_dict["deal_cnt"]:
            data_dict["deal_cnt"]=data_dict["deal_cnt"].replace('+', '')
        else:
            data_dict["deal_cnt"]=float(data_dict["deal_cnt"])
        with open("computer_info_test.csv", "a+", encoding="UTF-8", newline="") as csvfile:
            writer=csv.writer(csvfile)
            writer.writerow([id, brand, name,data_dict["price"], data_dict["deal_cnt"],data_dict["support"],message1, message2, message3, message4, message5, message6, message7, \
        message8, message9, message10, message11, message12, message13, message14, message15])
        print('爬取第'+str(num)+'条数据成功')
        num=num+1
        # print(data_dict["deal_cnt"])
        # data_list.append(data_dict)  # 将数据存入全局变量中
    # return data_list
parse_html1(html)
# def save():
#     with open('computer_href.csv', 'a', encoding='utf_8_sig', newline='') as f:
#         # 表头
#         title = data_list[0].keys()
#         # 声明writer
#         writer = csv.DictWriter(f, title)
#         # 写入表头
#         writer.writeheader()
#         # 批量写入数据
#         writer.writerows(data_list)
#     print('csv文件写入完成')
# save()

