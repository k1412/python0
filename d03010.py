import numpy as np
data  = np.genfromtxt('data2.csv',delimiter = ',',names=True)
print data

#标题充当索引

print data['id']
print type(data)
print data[1,0]

A = np.arange(10,19).reshape((3,3))
print A[[0,2],0:2]
print type(A)