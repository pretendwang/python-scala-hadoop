import requests
import json
from lxml import  etree
import csv
import time
import random
from selenium import webdriver
def get_comment(page,productId):
    url = 'https://club.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98&productId={}&score=0&sortType=5&page={}&pageSize=10&isShadowSku=0&fold=1'.format(productId,page)
    headers={
    'Accept':'*/*',
    'Accept-Encoding':'gzip, deflate, br',
    'Accept-Language':'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'Connection': 'keep-alive',
    'Cookie': '__jdu=16591170929141554292632; shshshfpa=07db6877-b40f-0fcb-d992-f957c6d56b70-1666282711; shshshfpb=raKDDLO9C0GGt6MQsAnfVHw; unpl=JF8EALRnNSttXR9RAUkFHBVHTQ9dWw1cQx4Ab25QBwoLGFJVHgpPGhR7XlVdXhRLFx9vZBRXXlNIVw4aAisSEXteU11bD00VB2xXVgQFDQ8WUUtBSUt-SV5RXF4AQhQKam8BZG1bS2QFGjIbFRRDXVRYXABIHwNqZwFQWFtDVwIZASsTIExtZG5VCUgUAmpXBGRcaAkAWRMCHRcSShBUWVkASxcFbm8GXF1dS1ABHgETERdJXmRfbQs; __jdv=122270672|direct|-|none|-|1668930231242; PCSYCityID=CN_140000_140100_0; jwotest_product=99; user-key=05170692-4648-4b5a-a8bc-55629bf64173; areaId=6; ipLoc-djd=6-303-305-5328; jsavif=0; __jda=122270672.16591170929141554292632.1659117092.1669875591.1669882092.17; __jdc=122270672; shshshfp=f3a00a3f0778bbe50a647b46ad2edfc2; token=2f623f9d8a91f7449cc8ed058cf22866,2,927712; __tk=AbX0RVh6lEfJXtn1gZXunsbkkvg0hbp1gZIwnDIalEXQXuH1gWhunuMymvpPStRcgXXZ4cIO,2,927712; ip_cityCode=303; shshshsID=9b67ee97f1f817bb22acc0412f465045_6_1669882274672; wlfstk_smdl=wlapfpfa5rlxkysaswa62dobkzqho08k; TrackID=1NChf398Z-nPPAuF6MrGjXwDSpuoU7I8I_Pm9W7cuyAem_kfTYWT2CWG1xVKMqaIoSro4UQLfGeFQG30VicLZ-ULp7_Jk6xqfKkQAXbofBTtmWRMbJcHYQgq38T7K-U3_; thor=445A8A2E21EC765B3FC7FE29BF0A968B4C3BE62944B401CF335FA6E3317FE72C546E29CB78A43A069CD4D57F9E4A65DAEEDA30020CE4ABEA72DC0A0BFE6C719AD2157E273935F6F5F82636EF21C2555E2366E37A19C616B497DCF4D4636823C9D258019F144E3A4ADD8E894DDD09F39E419C48314B321BBA583740AEF0217C3F95452F5FE7988876A4C79459D11072CC12C46C5300F19127D5EABF498FF9D0CE; pinId=0_ix3o6McL1_0IgnQJrUqw; pin=jd_SOmEoTWOJNxr; unick=jd_SOmEoTWOJNxr; ceshi3.com=201; _tp=zX%2Bda7AgBlKZUtVVhyfhhA%3D%3D; _pst=jd_SOmEoTWOJNxr; __jdb=122270672.12.16591170929141554292632|17.1669882092; 3AB9D23F7A4B3C9B=FAOK2WPMD2UQ3YIXQWQOR4M2UVR2N454B2JK6L7XMO75LLAPJXNENGBLMPNVMBRW5UV3QF2MW3TUZG772GY2TN5MGM; cn=4; JSESSIONID=B02D4183A7D299E3477377C0EABFA77F.s1',
    'Host': 'club.jd.com',
    'Referer': 'https://item.jd.com/',
    'sec-ch-ua': 'Microsoft Edge";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'Sec-Fetch-Dest': 'script',
    'Sec-Fetch-Mode': 'no-cors',
    'Sec-Fetch-Site': 'same-site',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.62'
    }
    time.sleep(3)
    r=requests.get(url=url,headers=headers).text.replace('fetchJSON_comment98(','').replace(');','')
    # print(r)
    dict = json.loads(r)
    comments=dict['comments']
    with open('computer_comment_test.csv', 'a', encoding='utf-8', newline='')as f:
        writer = csv.writer(f)
        for comment in  comments:
            content=comment['content']
            score=comment['score']
            creationTime=comment['creationTime']
            writer.writerow([productId,content,creationTime,score])
if __name__=='__main__':
    with open('computer_comment_test.csv', 'w', encoding='utf-8', newline='')as f:
       writer=csv.writer(f)
    with open('computer_info.csv','r',encoding='utf-8')as f:
            Lines=csv.reader(f)
        # for Line in Lines:
        #     productId=Line[0]
            productId='100020508229'
            for page in range(0,9):
                get_comment(page,productId)