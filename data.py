# -*- coding: utf-8 -*-
import json
file = open('data.txt','r')

#print('*************************************')
#print(d1['id'])
#print(d1['text'])
temp=[]
line=file.readline()
cnt=0
while line:
    if cnt%2==0:
        d1=json.loads(line)
        temp.append(d1['text'])
    line=file.readline()
    cnt+=1
#print(temp)
print(cnt)
 