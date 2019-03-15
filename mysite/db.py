# -*- coding: utf-8 -*-
# @Time    : 2019/2/19 14:52
# @Author  : Xin
# @File    : db.py
# @Software: PyCharm


import xlrd
import pymysql

def leading_in_front():
    book = xlrd.open_workbook("1.xlsx")
    sheet = book.sheet_by_name("detail")

    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='123456', db='test')
    # 创建游标
    cursor = conn.cursor()
    sql = """INSERT INTO app01_detail(Asin_detail, Total_reviews_detail, Total_score_detail,Asin_tag,Reviewer,Stars,Title,Date_str,Review_Content) VALUES (%s, %s, %s, %s,%s, %s, %s, %s,%s)"""

    #获取excle表数据，并插入数据库
    for r in range(2, sheet.nrows):
        Asin = sheet.cell(r, 0).value
        Total_reviews = sheet.cell(r, 1).value
        Total_score = sheet.cell(r, 2).value
        Asin_tag = sheet.cell(r, 3).value
        Reviewer = sheet.cell(r, 4).value
        Stars = sheet.cell(r, 5).value
        Title = sheet.cell(r, 6).value
        Date_str = sheet.cell(r, 7).value
        Review_Content = sheet.cell(r, 8).value
        values = (Asin, Total_reviews, Total_score, Asin_tag, Reviewer, Stars, Title, Date_str, Review_Content)
        cursor.execute(sql, values)
        conn.commit()

    cursor.close()
    conn.close()
    columns = str(sheet.ncols)
    rows = str(sheet.nrows)
    print("导入front表成功")
    print("我刚导入了 "+columns+" 列 and "+rows+" 行数据到MySQL!")

def leading_in_detail():
    book = xlrd.open_workbook("1.xlsx")
    sheet = book.sheet_by_name("front")

    # 建立一个MySQL连接
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='123456', db='test')
    # 创建游标
    cursor = conn.cursor()
    # 创建插入SQL语句
    sql ="""INSERT INTO app01_product(Asin, Total_reviews, Total_score) VALUES (%s,%s,%s)"""

    # 创建一个for循环迭代读取xls文件每行数据的, 从第二行开始是要跳过标题
    for r in range(3,sheet.nrows):
        Asin=sheet.cell(r, 1).value
        Total_reviews=sheet.cell(r, 2).value
        Total_score = sheet.cell(r, 3).value
        values = (Asin,Total_reviews,Total_score)
        # 执行sql语句
        cursor.execute(sql, values)
        # 提交
        conn.commit()

    # 关闭游标
    cursor.close()
    # 关闭数据库连接
    conn.close()
    columns = str(sheet.ncols)
    rows = str(sheet.nrows)
    print("导入detail表成功")
    print("我刚导入了 " + columns + " 列 and " + rows + " 行数据到MySQL!")

if __name__=="__main__":
    leading_in_front()
    leading_in_detail()


