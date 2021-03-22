# -*- codeing = utf-8 -*-
# @Time : 21/03/2021 13:02
# @Author : rain
# @File : spider test(urllib).py
# @Software: PyCharm


# 一个网页请求测试的网站“httpbin.org”
import urllib.request
import urllib.parse

# 获取一个get请求
# response = urllib.request.urlopen("http://www.baidu.com")
# print(response.read().decode("utf-8"))  # 对获取到的网页源码进行utf-8解码


# 获取一个post请求
# data = bytes(urllib.parse.urlencode({"hello": "world"}), encoding="utf-8")
# response = urllib.request.urlopen("https://httpbin.org/post", data=data)
# print(response.read().decode("utf-8"))


# 超时处理
"""
try:
    response = urllib.request.urlopen("https://httpbin.org/get", timeout=0.01)
    print(response.read().decode("utf-8"))
except urllib.error.URLError as e:
    print("time out!")
"""

# response = urllib.request.urlopen("https://httpbin.org/get")
# print(response.status)  # 状态码
# print(response.getheader("Server"))  # 各种属性（getheader）


# 爬虫test
"""
url = "http://httpbin.org/get"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/80.0.3987.163 Safari/537.36 "
}
data = bytes(urllib.parse.urlencode({'name': 'eric'}), encoding="utf-8")
req = urllib.request.Request(url=url, data=data, headers=headers, method="POST")
response = urllib.request.urlopen(req)
print(response.read().decode("utf-8"))
"""

# 豆瓣爬虫
url = "https://www.douban.com"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/80.0.3987.163 Safari/537.36 "
}
req = urllib.request.Request(url=url, headers=headers)
response = urllib.request.urlopen(req)
print(response.read().decode("utf-8"))
