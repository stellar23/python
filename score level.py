# -*- codeing = utf-8 -*-
# @Time : 15/03/2021 21:05
# @Author : rain
# @File : score level.py
# @Software: PyCharm

"""
import random  # 引入随机库
score = random.randint(0, 100)  # 生成随机数
print("score=%d" % score)
"""

score = int(input("请输入你的成绩："))
if 90 <= score <= 100:
    print("本次考试，等级为‘A’")
elif 80 <= score <= 90:
    print("本次考试，等级为‘B’")
elif 70 <= score <= 80:
    print("本次考试，等级为‘C’")
elif 60 <= score <= 70:
    print("本次考试，等级为‘D’")
elif 0 <= score <= 60:
    print("本次考试，等级为‘E’")
else:
    print("输入错误")
