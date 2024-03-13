# -*- coding: utf-8 -*-
"""
Created on Thu Feb 22 16:29:02 2024

@author: PCX
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import itertools
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from mlxtend.classifier import EnsembleVoteClassifier
from mlxtend.data import iris_data
from mlxtend.plotting import plot_decision_regions


import data_set

# Initializing Classifiers
clf1 = LogisticRegression(random_state=20)
clf2 = RandomForestClassifier(random_state=0)
clf3 = SVC(random_state=0, probability=True)
eclf = EnsembleVoteClassifier(clfs=[clf1, clf2, clf3], weights=[2, 1, 1], 
                              voting='soft')

# Loading some example data
data = data_set.data_set('Desktop/practica1/tripinfo.csv')

X = data[:,[1, 1]]
y = np.asarray(data[:,2], dtype = 'int')

# Plotting Decision Regions
gs = gridspec.GridSpec(2, 2)
fig = plt.figure(figsize=(10, 8))

for clf, lab, grd in zip([clf1, clf2, clf3, eclf],
                         ['Logistic Regression (1:t_0 2:t_1 3:t_2)', 
                          'Random Forest (1:t_0 2:t_1 3:t_2)', 
                          'RBF kernel SVM (1:t_0 2:t_1 3:t_2)', 
                          'Ensemble (1:t_0 2:t_1 3:t_2)'],
                         itertools.product([0, 1], repeat=2)):
    clf.fit(X, y)
    ax = plt.subplot(gs[grd[0], grd[1]])
    fig = plot_decision_regions(X=X[::-1], y=y, clf=clf)
plt.show()
