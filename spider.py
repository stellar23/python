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
    datalist = getdata(baseurl)
    # savepath = ".\\豆瓣电影Top250.xls"
    dbpath = "movie.db"
    # 3.保存数据
    # savedata(datalist, savepath)
    savedata2db(datalist, dbpath)

    # askURL("https://movie.douban.com/top250?start=")


# 影片详情链接的规则
findlink = re.compile(r'<a href"(.*?)">')  # 创建正则表达式对象，表示规则（字符串的模式）
# 影片图片
findimgsrc = re.compile(r'<img.*src="(.*?)",re.S')  # 让换行符包含在字符中
# 影片片名
findtitle = re.compile(r'<span class="title">(.*)</span>')
# 影片评分
findrating = re.compile(r'<span class="rating_num"property="v:average">(.*)</span')
# 找到评价人数
findjudge = re.compile(r'<span>(\d*)人评价</span>')
# 找到概况
findinq = re.compile(r'<span class="inq">(.*)</span>')
# 找到影片的相关内容
findbd = re.compile(r'<p class="">(.*?)</p>', re.S)


# 爬取网页
def getdata():
    datalist = []
    for i in range(0, 10):  # 调用获取页面信息的函数
        url = baseurl + url(i * 25)
        html = askURL(url)  # 保存获取到的网页源码

        # 2.逐一解析数据
        soup = BeautifulSoup(html, "html.parser")
        for item in soup.find_all('div', class_="item"):  # 查找符合要求的字符串，形成列表
            # print(item)  # 测试：查看电影item全部信息
            data = []
            item = str(item)
            print(item)
            break
            # 影片详情的链接
            link = re.findall(findlink, item)[0]  # re库用来通过正则表达式查找指定的字符串
            data.append(link)  # 添加链接
            imgsrc = re.findall(findimgsrc, item)[0]
            data.append(imgsrc)  # 添加图片
            titles = re.findall(findtitle, item)  # 片名可能只有一个中文名，没有外国名
            if len(titles) == 2:
                ctitle = titles[0]  # 添加中文名
                data.append(ctitle)
                otitle = titles[1].replace("/", "")  # 去掉无关的符号
                data.append(otitle)  # 添加外国名
            else:
                data.append(titles[0])
                data.append(' ')  # 外国名留空
            rating = re.findall(findrating, item)[0]
            data.append(rating)  # 添加评分
            judgenum = re.findall(findjudge, item)[0]
            data.append(judgenum)  # 添加评价人数
            inq = re.findall(findinq, item)
            if len(inq) != 0:
                inq = inq[0].replace("。", "")  # 去掉句号
                data.append(inq)  # 添加概述
            else:
                data.append(" ")  # 留空
            bd = re.findall(findbd, item)[0]
            bd = re.sub('<br(\s+)?/>(\s+)?', "", bd)  # 去掉<br/>
            bd = re.sub('/', " ", bd)  # 替换/
            data.append(bd.strip())  # 去掉前后的空格
            datalist.append(data)  # 把处理好的一部电影信息放入datalist

    return datalist


# 得到指定一个URL的网页内容
def askURL(url, reason):
    head = {  # 模拟浏览器头部信息，向服务器发送消息
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/80.0.3987.163 Safari/537.36 "
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
# 1.Excel
def savedata(savepath):
    print("save...")
    book = xlwt.Workbook(encoding="utf-8", style_compression=0)  # 样式，压缩效果
    sheet = book.add_sheet('豆瓣电影Top250', cell_overwrite_ok=True)  # 覆盖以前内容
    col = ('电影详情链接', "图片链接", "影片中文名", "影片外国名", "评分", "评价数", "概况", "相关信息")
    for i in range(0, 8):
        sheet.write(0, i, col[i])  # 列名
    for i in range(0, 250):
        print("第%d条" % i)
        data = datalist[i]
        for j in range(0, 8):
            sheet.write(i + 1, j, data[j])  # 数据

    book.save(savepath)  # 保存


# 2. 数据库
def savedata2db(datalist, dbpath):
    init_db(dbpath)
    conn = sqlite3.connect(dbpath)
    cur = conn.cursor()

    for data in datalist:
        for index in range(len(data)):
            if index == 4 or index == 5:
                continue
            data[index] = '""'+data[index]+'""'
        sql = '''
             insert into movie250(
             info_link,pic_link,cname,ename,score,rated,instroduction,info
             values (%s)  # 占位
            )
         ''' % ",".join(data)  # 列表中每一个元素都用逗号连接
        print(sql)
        cur.execute(sql)
        conn.commit()
    cur.close()
    conn.close()


def init_db(dbpath):
    sql = '''
        creat table movie250
        (
        id integer primary key autoincrement,
        info_link text,
        pic_link text,
        cname varchar,
        ename varchar,
        score numeric,
        rated numeric,
        instroduction text,
        info text
        )
    
    '''
    conn = sqlite3.connect(dbpath)
    cursor = conn.cursor()
    cursor.execute(sql)
    conn.commit()
    conn.close()


if __name__ == "__main__":  # 当程序执行时
    # 调用函数
    main()
    # init_db("movietest.db")  # 测试使用
    print("爬取完毕！")
