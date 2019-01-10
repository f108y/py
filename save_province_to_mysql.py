# -*- coding:utf-8 -*-


import pymysql

db = pymysql.connect('localhost','root','Test_123','local_id')

cursor = db.cursor()
sql = "INSERT INTO province_table(id,province) VALUES('%s','%s')"
with open('area_number.txt','r' ,encoding='GBK') as f:
	for line in f:
		line_list = line.split(':')
		print(line_list[0])
		print(line_list[1])
		sql ='''INSERT INTO province_table(id,province)VALUES('%s','%s');'''%(line_list[1],line_list[0])
		try:
			cursor.execute(sql)
			db.commit()
		except:
			db.rollback()
db.close()
