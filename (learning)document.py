# -*- codeing = utf-8 -*-
# @Time : 18/03/2021 00:04
# @Author : rain
# @File : (learning)document.py
# @Software: PyCharm

"""
f = open("text.txt", "w")
f.write("Hello world, I am here.")
f.close()
"""

# 文件读取
f = open("text.txt", "r")
content = f.read(5)
print(content)
f.close()
f = open("text.txt", "r")
contents = f.readlines()
print(contents)
i = 1
for temp in contents:
    print("%d:%s" % (i, temp))
    i += 1
f.close()
