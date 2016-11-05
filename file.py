import re
import numpy as np

data=[]
label=[]
sum1=[]
sum2=[]
sum3=[]
sum4=[]
sum5=[]
sum6=[]
sum7=[]
sum8=[]
sum9=[]
var1=[]
var2=[]
var3=[]
var4=[]
var5=[]
var6=[]
var7=[]
var8=[]
var9=[]
f=open('collection','r')
content=f.read()
content=content.split('\n')
for i in range(0,len(content)-1):
	line=content[i].split(',')
	line = [float(j) for j in line]
	data.append(line[1:-1])
	label.append(line[-1])
	sum1.append(line[1])
	sum2.append(line[2])
	sum3.append(line[3])
	sum4.append(line[4])
	sum5.append(line[5])
	sum6.append(line[6])
	sum7.append(line[7])
	sum8.append(line[8])
	sum9.append(line[9])
	var1.append(line[1])
	var2.append(line[2])
	var3.append(line[3])
	var4.append(line[4])
	var5.append(line[5])
	var6.append(line[6])
	var7.append(line[7])
	var8.append(line[8])
	var9.append(line[9])

mean2 = np.var(sum3)
print(mean2)
"""
from sklearn.linear_model import LogisticRegression
clf = LogisticRegression(penalty = 'l1')
clf = clf.fit(data,label)
print (clf.coef_[0])
"""
