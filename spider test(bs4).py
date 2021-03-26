# -*- codeing = utf-8 -*-
# @Time : 22/03/2021 20:18
# @Author : rain
# @File : spider test(bs4).py
# @Software: PyCharm


# 文档解析
"""
BeautifulSoup4将复杂HTML文档转换成一个复杂的树形结构，每个节点都是python对象，所有对象可以归纳为4种：

-Tag
-NavigableString
-BeautifulSoup
-Comment
"""

import re
from bs4 import BeautifulSoup

file = open("./baidu.html", "rb")
html = file.read().decode("utf-8")
bs = BeautifulSoup(html, "html.parser")

"""
# 1.Tag(标签及其内容；拿到它所找到的第一个内容)
print(bs.title)
print(bs.a)
print(bs.head)
print(type(bs.head))

# 2.NavigableString
print(bs.title.string)  # 不要标签，只要内容
print(bs.a.attrs)  # 拿到一个标签里的所有属性值

# 3.BeautifulSoup(表示整个文档)
print(type(bs))
print(bs.name)
print(bs)

# 4.Comment 是一个特殊的NavigableString，输出的内容不包含注释符号
print(bs.a.string)
print(type(bs.a.string))
"""

# --------------------------------------------------------


# 文档的遍历（更多内容，搜索文档）
print(bs.head.contents)
print(bs.head.contents[1])

# 文档的搜索

# (1)find_all()
# 字符串过滤：会查找与字符串完全匹配的内容
t_list = bs.find_all("a")
print(t_list)

# (2)正则表达式搜索：使用search（）方法来匹配内容
t_list1 = bs.find_all(re.compile("a"))
print(t_list1)


# (3)方法：传入一个函数（方法），根据函数的要求来搜索
def name_is_exists(tag):
    return tag.has_attr("name")


t_list2 = bs.find_all(name_is_exists)
print(t_list2)

# (4)kwargs 参数
t_list3 = bs.find_all(id="head")
for item in t_list3:
    print(item)

t_list4 = bs.find_all(class_=True)
for item1 in t_list4:
    print(item1)

t_list5 = bs.find_all(href="http://news.baidu.com")
for item2 in t_list5:
    print(item2)

# (5)text参数
t_list6 = bs.find_all(text="hao123")
for item3 in t_list6:
    print(item3)

t_list7 = bs.find_all(text=re.compile("\d"))  # 应用正则表达式来查找包含特定文本的内容（标签里的字符串）
for item4 in t_list7:
    print(item4)

# (6)limit参数
t_list8 = bs.find_all(text="a", limit=3)
for item5 in t_list8:
    print(item5)

# CSS选择器
t_list9 = bs.select('title')  # 通过标签来查找
for item6 in t_list9:
    print(item6)

t_list10 = bs.select(".mnav")  # 通过类名来查找
for item7 in t_list10:
    print(item7)

t_list11 = bs.select("#u1")  # 通过id来查找
for item8 in t_list11:
    print(item8)

t_list12 = bs.select("a[class='bri']")  # 通过属性来查找
for item9 in t_list12:
    print(item9)

t_list13 = bs.select("a[class='bri']")  # 通过属性来查找
for item10 in t_list13:
    print(item10)

t_list14 = bs.select("head>title")  # 通过子标签来查找
for item11 in t_list14:
    print(item11)

t_list15 = bs.select(".mnav~.bri")
print(t_list15[0].get_text())
