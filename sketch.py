import json
#import scipy as sp
import numpy as np
#import sklearn
import csv
import urllib2
import subprocess
import StringIO
import sys
#from sklearn import svm
#from sklearn import tree
#from sklearn import linear_model

symbol = sys.argv[1]

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

stock_info = np.matrix(stock_info)
# Percent changes in OPENING price per day
open_price = [float(x.tolist()[0][1]) for x in stock_info[1:len(stock_info)]]
percent_change_open = [np.divide((x - open_price[i-1]), open_price[i - 1]) for i, x in enumerate(open_price)][1:]
percent_change_open = np.matrix(['PercChangeOpen1Day',np.nan]+percent_change_open).T
# add as another feature column
stock_info = np.append(stock_info, percent_change_open, axis=1)

#Percent changes in OPENING price per 5 days
percent_change_5_open = [np.divide((x - open_price[i-5]), open_price[i - 5]) for i, x in enumerate(open_price)][5:]
percent_change_5_open = np.matrix(['PercChangeOpen5Day',np.nan,np.nan,np.nan,np.nan,np.nan]+percent_change_5_open).T
# add as another feature column
stock_info = np.append(stock_info, percent_change_5_open, axis=1)

#I(close > open) on a given day where I is indicator fn
close_price = [float(x.tolist()[0][4]) for x in stock_info[1:len(stock_info)]]
indic = [1 if close_price[i]>open_price[i] else 0 for i in range(len(close_price))]
indic = np.matrix(['I(Close>Open)']+indic).T
# add as another feature column
stock_info = np.append(stock_info, indic, axis=1)

print stock_info

#run svm

