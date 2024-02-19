from selenium import webdriver
import time
import json


'''
ip, port, tp = open('proxy.txt').read().split()
proxy = tp + '://' + ip + ':' + port
print(proxy)
option = ChromeOptions()
option.add_argument('--proxy-server=' + proxy)
driver = webdriver.Chrome(chrome_options=option)
'''
#登录并保存cookie
# 1.创建chrom浏览器对象
driver = webdriver.Chrome()
# 2.打开淘宝登录网址
driver.get('https://passport.jd.com/new/login.aspx?ReturnUrl=https%3A%2F%2Fwww.jd.com%2F')
#等待30s
time.sleep(30)
'''有时候我们爬虫的网站需要验证码登录，
一般这时我们不可能再使用账号密码登录这种方法了，
而是把登录后cookie保存起来，保存在txt文件，然后再把cookie取出来直接登录
'''
'''
我们获取的cookie是字典格式，
我们需要使用cookies = json.dumps(cookies)转换为字符串格式再保存入txt文件
# 获取cookie并通过json模块将dict转化成str
所在域、name、value、有效期和路径
'''
with open('cookies.txt', 'w') as f:
    f.write(json.dumps(driver.get_cookies()))
    print('writed')
driver.quit()

