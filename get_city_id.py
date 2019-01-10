 


# -*- coding=utf-8 -*-



import requests
import re


url = 'http://www.qucha.net/shenfenzheng/city.htm'

html = requests.get(url)
re_str = '\d{6}\s[\u4E00-\u9FA5]*\s'
city_ = '\d{4}00\s[\u4E00-\u9FA5]*\s'
html.encoding='gb2312'
with open('city_id_list.txt',mode='w') as f:
	print(html.text,file = f)

with open('city_id_list.txt',mode='r') as f1:
	match_obj = re.findall(re_str,f1.read())
#	print(len(match_obj))
#	print(type(match_obj))
#	l = int(len(match_obj))
#	print(match_obj,end = '\n')
	for i in iter(match_obj):
		tmp = i.split(' ')
#		tmp = match_obj(i-1).split(' ')
#		print(tmp[0])
#		print(tmp[1])			
#		print(tmp)
		city_ = re.findall(city_,match_obj)
		a,b,c,d,e,f = tmp[0]
		str_=c+d
