# -*- coding: utf-8 -*-
# @Time    : 2019/2/19 9:52
# @Author  : Xin
# @File    : amason_test.py
# @Software: PyCharm

import time
import requests
from requests.exceptions import RequestException
import re
import json
import csv
from multiprocessing import Pool

def get_one_page(url):
    #请求头，将此请求欺骗服务器为浏览器请求
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36"}
    response = requests.get(url,headers=headers)
    try:
        if response.status_code==200:
            return response.text
        return None
    except RequestException:
        return None


def parse_one_page(html):
    #预先编译正则表达式，用来获取想要的信息，re.S的作用是为了让 . 能匹配任意字符，包括换行符，空格，如果不加re.S则不能匹配
    pattern = re.compile('<li.*?class="zg-item-immersion".*?class="zg-badge-text">(.*?)</span>.*?<a.*?href="(.*?)">.*?<img.*?src="(.*?)".*?data-rows="2">(.*?)</div>.*?<span.*?>(.*?)</span>.*?<a.*?>(.*?)</a>.*?<span.*?><span.*?>(.*?)</span>.*?</li>',re.S)

    result = re.findall(pattern,html)
    #print(result)
    for item in result:
        yield {
            "id":item[0],
            'product_url':item[1],
            'product_img':item[2],
            'product': item[3],
            'mark': item[4],
            'mark_num': item[5],
            'product_price':item[6]
        }

def write_to_file(content,writer):
    # with open('result.csv', 'w') as f:
    #     writer = csv.writer(f)
    #     writer.writerow([content["product_url"],content["product_img"],content["product"],content["mark"],content["mark_num"],content["product_price"]])
    writer.writerow(
        [content["id"], content["product"], content["product_url"], content["product_img"],content["product_price"], content["mark"], content["mark_num"]
         ])

def main(i):
    url = 'https://www.amazon.com/Best-Sellers-Kitchen-Dining-Bakeware/zgbs/kitchen/289668/ref=zg_bs_pg_{0}?_encoding=UTF8&pg={0}'.format(i)
    html = get_one_page(url)
    #print(html)
    parse_one_page(html)
    with open('result.csv','a') as f :
        writer = csv.writer(f)
        #标题
        writer.writerow(['id','product', 'product_url', 'product_img', 'product_price', "mark", "mark_num"])
        #循环写入csv
        for item in parse_one_page(html):
            #print(item)
            write_to_file(item,writer)

if __name__ == '__main__':
    #main(1)
#普通爬取

    # start_time = time.time()
    # for i in range(1,3):
    #     main(i)
    # end_time = time.time()
    # print(end_time-start_time)
    #print("爬取结束")
# 多进程爬取
    #start_time = time.time()
    pool = Pool()
    pool.map(main, [i for i in range(1,3)])
    #end_time = time.time()
    #time1=end_time - start_time
    print("爬取结束")
    #print("爬取结束,总耗时：",time1)