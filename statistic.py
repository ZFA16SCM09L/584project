import re

data=[]
label=[]

f=open('collection','r')
content=f.read()
content=content.split('\n')
for i in range(0,len(content)-1):
	line=content[i].split(',')
	line = [float(j) for j in line]
	data.append(line[1:-1])
	label.append(line[-1])

from sklearn.preprocessing import scale
data = scale(data,copy = 'False')
print("number of instance: ", len(data))
print("number of features: ", len(data[0]))

cout = 0;
for i in label:
	if(i == 0):
		cout = cout + 1
print("accuracy of predicting the majority class all the time: ",cout/2982)

import random
cout = 0;
for i in label:
	if(i == random.randint(0,1)):
		cout = cout + 1
print("accuracy of random prediction:", cout/2982)
