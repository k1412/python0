import numpy as np

# a = np.array([[1,2,3,4,2,3,1],[3,1,4,2,5,2]])

# print a
# print a.shape
# #print a.dtpye
# print a.ndim
# print a.size

student = np.dtype([('name','S20'),('age','i1'),('marks','f4')])
print student

student_aGroup = np.array([('abc',21,50),('xyz',18,75)],dtype = student)

print student_aGroup




#ndarray.ndim用于返回数组的维数，等于秩
a = np.arange(24)  
print (a.ndim)             # a 现只有一个维度
# 现在调整其大小
b = a.reshape(2,4,3)  # b 现在拥有三个维度
print (b.ndim)

a = np.array([[1,2,3],[4,5,6]])  
print a
print a.shape
a.shape = (3,2)
print a
print (a.shape)

x = np.array([1,2,3,4,5], dtype = np.int8)  
print (x.itemsize)

y = np.array([1,2,3,4,5], dtype = np.float64)  
print (y.itemsize)

x = np.array([1,2,3,4,5])  
print (x.flags)