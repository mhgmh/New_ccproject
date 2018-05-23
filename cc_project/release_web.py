import pymysql as py
import Pub_articles
import time
import requests
from lxml import etree

se = requests.session()

while True:
    db = py.connect(host='47.98.194.196',user='toutiao',password='toutiao',db='toutiao',charset='utf8')
    curs = db.cursor()
    TABLES = "SHOW TABLES;"
    curs.execute(TABLES)
    tables = list(curs.fetchall())
    for table in tables:
        print("当前数据库名为:"+str(table))
        cycle = 0
        fromsql = "select * from {}".format(table[0]) #提取出数据表里面所有的内容
        curs.execute(fromsql)
        result = list(curs.fetchall())  #取出当前数据表里面的内容
        if len(result) != 0:
            for base in result:   #利用数据表内容取出每一行标题内容
                print('当前提取到的标题为:'+base[1])
                alls = se.get("https://www.222zhe.com/search/"+base[1]).text
                f = etree.HTML(alls)
                title = f.xpath("//div[@class='pagewrapper']/div[@class='cardlist']/div[@class='card col span_1_of_4']/div[@class='shop-item']/h3/a/text()")
                bases = ""
                for tl in title:
                    bases += tl + "\n"
                if base[1] in bases:
                    print("当前文章重复,准备跳到下一条！")
                    pass
                else:
                    articles = Pub_articles.articles.Pub_article(base[2])  #返回信息
                    print("返回信息："+str(articles))
                    if str(articles) != '错误信息':
                        listarticle = list(articles)
                        print(listarticle)
                        Pub_articles.articles.Blog_article(table[0], listarticle[0], listarticle[1], listarticle[2])  #发布文章

                print('当前即将删除第：'+str(table[0])+"的第"+str(base[0])+'条数据')
                Delete_sql = "DELETE FROM {} WHERE id = {}".format(table[0],base[0])
                curs.execute(Delete_sql)
                db.commit()
                if cycle == 5:
                    print("当前{}分类已发布完成,正在准备延时~~~".format(table[0]))
                    time.sleep(5)
                    break
                else:
                    cycle += 1
        else:
            print("当前{}数据库已无数据".format(table[0]))








