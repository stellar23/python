# -*- codeing = utf-8 -*-
# @Time : 23/03/2021 22:05
# @Author : rain
# @File : spider test(Re).py
# @Software: PyCharm


# 正则表达式：字符串模式（判断字符串是否符合一定的标准）

import re
# 创建模式对象

# pat = re.compile("AA")  # 标准
# m = pat.search("AB")  # 校验对象
# print(m)

# 没有模式对象

m = re.search("asd", "Aasd")  # 前面是规则，后面是被检验对象
print(m)

print(re.findall("a", "ASDaDFGAa"))  # 前面字符串是规则（正则表达式），后面字符串是被检验的字符串

print(re.findall("[A-Z]", "ASDaDFGAa"))
print(re.findall("[A-Z]+", "ASDaDFGAa"))

# sub
print(re.sub("a", "A", "abcdcasd"))  # 找到a用A替换，在第三个字符串中查找

# 建议在正则表达式中，被比较的字符串前面加上r，不用担心转义字符的问题
