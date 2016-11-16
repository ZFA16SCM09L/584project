import re

data=[]
label=[]
list1 = [2,5,7,8,9]
f=open('collection','r')
content=f.read()
content=content.split('\n')
for i in range(0,len(content)-1):
	line=content[i].split(',')
	line = [float(j) for j in line]
	tem = []
	for m in list1:
		tem.append(line[m])
	data.append(tem)
	label.append(line[-1])

from sklearn.preprocessing import scale
data = scale(data,copy = 'False')

from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_val_score

def l2(x,y):
	clf = LogisticRegression(penalty = 'l2',random_state = 0, solver = x, fit_intercept = y)
	clf = clf.fit(data,label)
	out = cross_val_score(clf,data,label,cv = 10,scoring = "accuracy")
	print("solver = ",x,"  fit intercept = ",y,"   accu = ",out.mean())
def l1(x):
	clf = LogisticRegression(penalty = 'l1',random_state = 0, solver = "liblinear", fit_intercept = x)
	clf = clf.fit(data,label)
	out = cross_val_score(clf,data,label,cv = 10,scoring = "accuracy")
	print("fit intercept = ",x,"   accu = ",out.mean())

list1 = ["newton-cg", "lbfgs", "liblinear", "sag"]
list2 = [0,1]
print("l2 default:")
clf = LogisticRegression(penalty = 'l2',random_state = 0)
clf = clf.fit(data,label)
out = cross_val_score(clf,data,label,cv = 10,scoring = "accuracy")
print(out.mean())
print ("other combine:")
for i in list1:
	for j in list2:
		l2(i,j)

list3 = [0,1]
print("l1 default:")
clf = LogisticRegression(penalty = 'l1',random_state = 0)
clf = clf.fit(data,label)
out = cross_val_score(clf,data,label,cv = 10,scoring = "accuracy")
print(out.mean())
print ("other combine:")
for i in list3:
	l1(i)

clf = LogisticRegression(penalty = 'l2',random_state = 0)
clf = clf.fit(data,label)
print("weight of every feature in model with best accu: ",clf.coef_[0])
