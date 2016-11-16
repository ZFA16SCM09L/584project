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

from sklearn.linear_model import Ridge
from sklearn.metrics import mean_squared_error
clf = Ridge()
clf = clf.fit(data,label)
print(clf.predict(data[0].reshape(1, -1)))
"""
from sklearn.model_selection import cross_val_score
out = cross_val_score(clf,data,label,cv = 10,scoring = "neg_mean_squared_error")
print(out.mean())
"""
