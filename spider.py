# -*- codeing = utf-8 -*-
# @Time : 18/03/2021 11:48
# @Author : rain
# @File : (learning)spider.py
# @Software: PyCharm

# 爬虫流程
"""
1、准备工作
通过浏览器查看分析目标网页，学习编程基础规范。
2、获取数据
通过HTTP库向目标站点发出请求，请求可以包含额外的header等信息，如
果服务器能正常响应会得到一个Response，便是所要获取的页面内容。
3、解析内容
得到的内容可能是HTML，json等格式，可以用页面解析器、正则表达式等进行解析
4、保存数据
保存形式多样，可以存为文本，也可以保存到数据库，或者保存特定格式的文件。
"""

from bs4 import BeautifulSoup  # 网络解析，获取数据
import re  # 正则表达式，进行文字匹配
import urllib  # 制定URL，获取网页数据
import urllib.request
import urllib.error
import xlwt  # 进行Excel匹配
import sqlite3  # 进行SQLite数据库操作


def main():
    baseurl = "https://movie.douban.com/top250?start="
    # 1.解析网页
    datalist = getdata()
    savepath = ".\\豆瓣电影Top258.xls"
    # 3.保存数据
    # savedata(savepath)

    askURL("https://movie.douban.com/top250?start=")


# 爬取网页
def getdata():
    datalist = []
    for i in range(0, 10):  # 调用获取页面信息的函数
        url = baseurl + url(i*25)
        html = askURL(url)  # 保存获取到的网页源码

    # 2.逐一解析数据
    return datalist

# 得到指定一个URL的网页内容
def askURL(url, reason):
    head = {  # 模拟浏览器头部信息，向服务器发送消息
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36 "
    }  # 用户代理，表示告诉豆瓣服务器，我们是什么类型的机器、浏览器（本质是告诉浏览器，我们可以接受什么水平的文件内容）

    # 发送消息
    request = urllib.request.Request(url, headers=head)
    html = ""
    try:
        response = urllib.request.urlopen(request)
        html = response.read().decode("utf-8")
    except urllib.error.URLError as e:
        if hasattr(e, "code"):
            print(e.code)
        if hasattr(e, "reason"):
            print(e, reason)
    return html


# 保存数据
def savedata(savepath):
    print("save...")


if __name__ == "__main__":  # 当程序执行时
    # 调用函数
    main()
