#!/usr/bin/python
#-*- coding:utF-8 -*-


import MySQLdb


# 连接数据库并获取游标；同时use report 数据库
db = MySQLdb.connect(host='xxx', user='xxx', passwd='xxx',db='xxx')
cursor = db.cursor()

# 执行语句并展示结果集
cursor.execute(" desc credit_anti_fraud_metrics")
results = cursor.fetchall()
results


# 创建表 
sql = "create table if not exists wenchao_test(name varchar(128) primary key, age int(4))"  
cursor.execute(sql)  
print "success create table wenchao_test!"


# 插入数据  
sql = "insert into wenchao_test(name, age) values('%s', '%d')" % ("Jim", 19)  
try:  
    cursor.execute(sql)  
    db.commit()  #凡是insert,update,delete都要"提交事务commit()",否则数据库不会改变  
    print "succeess insert a record!"  
except Exception, e:  
    db.rollback()  #异常必须回滚rollback()  
    print e  