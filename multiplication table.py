# -*- codeing = utf-8 -*-
# @Time : 15/03/2021 22:09
# @Author : rain
# @File : multiplication table.py
# @Software: PyCharm

print("九九乘法表:\n")
i = 1
while i < 10:
    j = 1
    while j <= i:
        print("%d*%d=%2d" % (j, i, j * i), end='\t')
        j += 1
    print("")
    i += 1
