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

from sklearn.linear_model import LogisticRegression
clf = LogisticRegression(penalty = 'l1',random_state = 0)
clf = clf.fit(data,label)
print (clf.coef_[0])
