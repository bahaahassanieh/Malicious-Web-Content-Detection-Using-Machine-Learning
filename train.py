import numpy as np

from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
from sklearn import metrics

import sys
import joblib

labels=[]
features=[]
file=open('/home/rohit/PycharmProjects/BE/Training Dataset.arff').read()
list=file.split('\r\n')
data=np.array(list)
data1=[i.split(',') for i in data]
data1=data1[0:-1]
for i in data1:
	labels.append(i[30])
data1=np.array(data1)
features=data1[:,:-1]
features=features[:,[0,1,2,3,4,5,6,7,8,9,11,12,13,14,15,16,17,18,22,23,24,25,27,29]]
#print features
features=np.array(features).astype(np.float)

##### HAS TO BE CHANGED TO ALL ENTRIES OF THE DATASET
features_train=features[:10000]
labels_train=labels[:10000]
features_test=features[10000:]
labels_test=labels[10000:]

print("\n\n ""Random Forest Algorithm Results"" ")
clf4 = RandomForestClassifier(min_samples_split=7)
clf4.fit(features_train, labels_train)
pred4=clf4.predict(features_test)
print(classification_report(labels_test, pred4))
print 'The accuracy is:', accuracy_score(labels_test, pred4)
print metrics.confusion_matrix(labels_test, pred4)

sys.setrecursionlimit(9999999)
joblib.dump(clf4, 'classifier/random_forest.pkl',compress=9)
