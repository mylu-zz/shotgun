import json
#import scipy as sp
import numpy as np
#import sklearn
import csv
import urllib2
import subprocess
import StringIO
#from sklearn import svm
#from sklearn import tree
#from sklearn import linear_model

symbol = 'goog'
url = 'http://ichart.yahoo.com/table.csv?s=' + symbol #+ '&a=5&b=1&c=2009 &d=0&e=31&f=2010&g=w&ignore=.csv'
q = urllib2.urlopen(url)
csvfile = q.read()
f = StringIO.StringIO(csvfile)
#subprocess.call('mv ~/Downloads/table.csv .',shell=True)
stock_info = []
#with open(symbol + '.csv', 'rb') as csvfile:
reader = csv.reader(f, delimiter=",")
for row in reader:
	stock_info.append(row)

blah = np.matrix(stock_info)




