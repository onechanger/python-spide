#!/usr/bin/env python
# coding=utf-8
 
from xlwt import *
text_name = 'user.txt'
#需要xlwt库的支持
#import xlwt
file = Workbook(encoding = 'utf-8')
#指定file以utf-8的格式打开
table = file.add_sheet('data')
#指定打开的文件名
user = open(text_name,'rb')

user_list = user.readlines()
data = [['序号','用户名','资产']]
for i,j in enumerate(user_list):
    onelist = j.decode('utf-8').split('"')
    templen = len(onelist)-1
    if templen == 0:
        continue
    temp =[i]
    for k,l in enumerate(onelist):
        if k % 2 != 0:
            temp.append(l)
    data.append(temp)
user.close()


for i,p in enumerate(data):
#将数据写入文件,i是enumerate()函数返回的序号数
    for j,q in enumerate(p):
        # print i,j,q
        table.write(i,j,q)
file.save('data.xls')
