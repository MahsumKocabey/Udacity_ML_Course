#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:    
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess
from sklearn.svm import SVC


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()


# Use a small part of the train data to get a prediction in a shorter time.
features_train = features_train[:int(len(features_train)/100)]
labels_train = labels_train[:int(len(labels_train) / 100)]

#########################################################
### your code goes here ###
clf = SVC(kernel = 'linear')
clf.fit(features_train, labels_train)
clf.predict(features_test)
print("The prediction score is {}".format(clf.score(features_test, labels_test)))
#########################################################


