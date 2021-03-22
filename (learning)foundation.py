# -*- codeing = utf-8 -*-
# @Time : 15/03/2021 13:55
# @Author : rain
# @File : (learning)foundation.py
# @Software: PyCharm


"""#整体注释掉
print("标准化输出字符串")
a=10
print("这是变量：",a)
"""

"""
# 格式化输出
# %d有符号十进制整数；%s通过str()字符串转换来格式化
age = 18
print("我的年纪是：%d岁" % age)
print("我的名字是%s，我的国籍是%s" % ("小王", "中国"))

print("www", "baidu", "com", sep=".")  # 设置分隔符
print("hello", end="")  # 空格表示直接连接后面的字符串
print("world", end="\t")  # Tab键
print("python", end="\n")  # 换行
print("end")
”“”

“”“
a = 10
print(type(a))  # 查看变量类型
b = "abc"
print(type(b))

for i in range(5):
    print(i)

for i in range(-1, 10, 3):
    print(i)

# 字符串中提取字符
name = "beijing"
for x in name:
    print(x, end="\t")

print("\n")
i = 2
while i <= 7:
    print("第%d次循环" % (i - 1))
    print("i=%d" % i)
    i += 1
“”“

”“”
# 1~100自然数之和
i = 1
sum0 = 0
while i <= 100:
    sum0 = sum0 + i
    i += 1
print("1~100自然数之和为：%d" % sum0)
“”“

“”“
# 字符串截取
str1 = "chengdu"
print(str1)
print(str1[0])
print(str1[0:5])
print(str1[1:7:2])
print(str1[5:])
print(str1 + "，你好")
print(str1 * 3)

print(len(str1))  # len()可以得到列表的长度
“”“

”“”
# 添加到列表
m = [1, 2]
n = [3, 4]
# 区别一下
m.append(n)
print(m)
m.extend(n)
print(m)
m.insert(1, n)
print(m)
del m[2]  # 删除元素
"""

"""
# 改
namelist = ["111", "Xiaoping", "小兰", "速度与激情"]
print("-----增加前名单的列表数据------")
for name in namelist:
    print(name)
namelist[1] = "九九九感冒灵"
print("-----增加前名单的列表数据------")
for name in namelist:
    print(name)
"""

"""
# 查:[in or not]
namelist = ["111", "Xiaoping", "小兰", "速度与激情"]
findName = input("请输入要查找的内容：")
if findName in namelist:
    print("已找到")
else:
    print("未找到")
"""

"""
a = ["a", "b", "c", "a", "b", "d"]
print(a.index("a", 1, 4))  # 可以查找指定下标范围的元素，并返回对应数据的下标（范围区间左闭右开）
print(a.count("c"))  # 计数
a.reverse()  # 反转
print(a)
a.sort()  # 升序排列
print(a)
a.sort(reverse=True)  # 降序排列
print(a)
"""

# 三个房间，八个老师，随机分配
# import random (在开头)

"""
office = [[], [], []]
names = ["A", "B", "C", "D", "E", "F", "G", "H"]
for name in names:
    index = random.randint(0, 2)
    office[index].append(name)
print(office)
"""

"""
tup1 = (50,)  # 定义一个元祖
print(type(tup1))
tup2 = ("aaa", "bbb", "ccc")
print(type(tup2))

# 增
tup = tup1 + tup2
print(tup)
"""

"""
# 字典定义
info = {"name": "吴彦祖", "age": "18"}
# 字典的访问
print(info["name"])
print(info["age"])
# 访问不存在的键“None”
print(info.get("gender", "m"))
# 增/改
newID = input("请输入新的学号：")
info["id"] = newID
print(info)
# 删
del info["name"]
# 查
print(info.keys())  # 打印所有的键
print(info.values())  # 打印所有的值
# 遍历值
for key in info.keys():
    print(key)
# 遍历所有键值对
for key, value in info.items():
    print("key=%s, value=%s" % (key, value))
"""

"""
# 函数的定义
def printinfo():
    print("---------------------")
    print("--人生苦短，我用python--")
    print("---------------------")


# 函数的调用
printinfo()
"""

"""
# 带参数
# 函数的定义
def add(a, b):
    c = a + b
    print(c)


# 函数的调用
add(11, 22)
"""


# 返回多个值
def divide(a, b):
    shang = a // b
    yushu = a % b
    return shang, yushu


sh, yu = divide(5, 2)
print(sh, yu)
