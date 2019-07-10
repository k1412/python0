import pandas as pd 

frame2 = pd.read_csv('myCSV_01.csv')


print frame2
print frame2.columns
print frame2.index
print frame2.values
print frame2['animal']
print frame2.ix[2]
print '对比两种行选取\n'
print frame2[0:1]
print frame2[1:2]
print frame2[2:3]