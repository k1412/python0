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

# del frame2['animal']
# print frame2[frame2<3]

frame3 = frame2.reindex(range(6),method='ffill',columns = ['white','red','blue','green','new','animal'])

print frame3