# -*- codeing = utf-8 -*-
# @Time : 28/03/2021 12:54
# @Author : rain
# @File : Asynchronously browse.py
# @Software: PyCharm

"""
如何防止被拦截：
1.间隔时间爬取
2.代理
如何异步加载：
0.判断是否为异步加载
1.找到异步请求的连接并分析规律（参数、规律）
2.获取并返回json数据并解析（转换、解析）
"""


import json
import urllib.request,urllib.error
import re

def main():
    url0 = "https://search.51job.com/list/010000,000000,0000,00,9,99,+,2,1.html?lang=c&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&ord_field=0&dibiaoid=0&line=&welfare="
    askURL(url0)

# 得到指定一个URL的网页内容
def askURL(url):
    head = {  # 模拟浏览器头部信息，向服务器发送消息
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36 "
    }  # 用户代理，表示告诉豆瓣服务器，我们是什么类型的机器、浏览器（本质是告诉浏览器，我们可以接受什么水平的文件内容）

    # 发送消息
    request = urllib.request.Request(url, headers=head)
    html = ""
    try:
        response = urllib.request.urlopen(request)
        html = response.read().decode("gbk")
    except urllib.error.URLError as e:
        if hasattr(e, "code"):
            print(e.code)
        if hasattr(e, "reason"):
            print(e, reason)
    return html

if __name__ == "__main__":
    main()

