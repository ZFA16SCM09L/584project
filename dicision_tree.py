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

from sklearn import tree
#clf = tree.DecisionTreeClassifier() #criterion,max_depth,min_weight_fraction_leaf
#clf = clf.fit(data,label)
#tree.export_graphviz(clf,out_file='tree.dot') 
from sklearn.model_selection import cross_val_score
#out = cross_val_score(clf,data,label,cv = 10,scoring = "accuracy")
#print(out.mean())
print("1 entropy:")
clf = tree.DecisionTreeClassifier(criterion = "entropy") 
clf = clf.fit(data,label)
out = cross_val_score(clf,data,label,cv = 10,scoring = "accuracy")
print(out.mean())

def entro(x,y):
	clf = tree.DecisionTreeClassifier(criterion = "entropy",max_depth = x,min_weight_fraction_leaf = y) 
	clf = clf.fit(data,label)
	out = cross_val_score(clf,data,label,cv = 10,scoring = "accuracy")
	print("max_depth = ",x,"min weight frac = ",y,"accu : ",out.mean())
def gini(x,y):
	clf = tree.DecisionTreeClassifier(criterion = "gini",max_depth = x,min_weight_fraction_leaf = y) 
	clf = clf.fit(data,label)
	out = cross_val_score(clf,data,label,cv = 10,scoring = "accuracy")
	print("max_depth = ",x,"min weight frac = ",y,"accu : ",out.mean())
	
list1 = [5,10,20]
list2 = [0.1,0.15,0.2,0.3]
for i in list1:
	for j in list2:
		entro(i,j)

print("2 gini:")
clf = tree.DecisionTreeClassifier(criterion = "entropy") 
clf = clf.fit(data,label)
out = cross_val_score(clf,data,label,cv = 10,scoring = "accuracy")
print(out.mean())
for i in list1:
	for j in list2:
		gini(i,j)
