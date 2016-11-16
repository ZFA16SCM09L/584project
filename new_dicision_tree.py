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

from sklearn import tree
from sklearn.model_selection import cross_val_score


def entro(x,y):
	clf = tree.DecisionTreeClassifier(random_state = 0, criterion = "entropy",max_depth = x,min_weight_fraction_leaf = y) 
	clf = clf.fit(data,label)
	out = cross_val_score(clf,data,label,cv = 10,scoring = "accuracy")
	print("max_depth = ",x,"min weight frac = ",y,"accu : ",out.mean())
def gini(x,y):
	clf = tree.DecisionTreeClassifier(random_state = 0, criterion = "gini",max_depth = x,min_weight_fraction_leaf = y) 
	clf = clf.fit(data,label)
	out = cross_val_score(clf,data,label,cv = 10,scoring = "accuracy")
	print("max_depth = ",x,"min weight frac = ",y,"accu : ",out.mean())

print("1 entropy:")
clf = tree.DecisionTreeClassifier(random_state = 0, criterion = "entropy") 
clf = clf.fit(data,label)
out = cross_val_score(clf,data,label,cv = 10,scoring = "accuracy")
print(out.mean())
list1 = [5,10,20]
list2 = [0.1,0.15,0.2,0.3]
for i in list1:
	for j in list2:
		entro(i,j)

print("2 gini:")
clf = tree.DecisionTreeClassifier(random_state = 0, criterion = "entropy") 
clf = clf.fit(data,label)
out = cross_val_score(clf,data,label,cv = 10,scoring = "accuracy")
print(out.mean())
for i in list1:
	for j in list2:
		gini(i,j)
