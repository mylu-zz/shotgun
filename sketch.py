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

symbol = 'msft'

"""
Note that Google for some reason only returns prices for 3/27/2014 - present, not full IPO length? Why

http://ichart.finance.yahoo.com/table.csv?s=GE&a=00&b=2&c=1962&d=05&e=10&f=2014&g=d&ignore=.csv

Meaning of parameters 
	- note the dates do not have to be within actual range of company lifetime
	- for example, doing Facebook (sym = FB) between 1/2/1962 - 5/10/2014 will return prices between 5/18/2012 - 5/9/2014. 
a = start month (0 indexed, starting january = 00)
b = start day (1 indexed, starting with the first day of month)
c = start year
d = end month
e = end day
f = end year
g = type of request (time interval)
	d -> Daily
	w -> Weekly
	m -> Monthly
	v -> Dividends only
"""

url = "http://ichart.finance.yahoo.com/table.csv?s=" + symbol + "&a=00&b=2&c=1962&d=05&e=10&f=2014&g=d&ignore=.csv"
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
blah = blah[1:,1:]

print blah


