import json
#import scipy as sp
#import numpy as np
#import sklearn
import csv
#from sklearn import svm
#from sklearn import tree
#from sklearn import linear_model

symbol = 'goog'
with open(symbol + '.csv', 'rb') as csvfile:
	reader = csv.reader(csvfile, delimiter= ',')
	for row in reader:
		print ', '.join(row)
