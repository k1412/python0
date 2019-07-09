import numpy as np 

A = np.arange(0,9).reshape(3,3)
B = np.ones((3,3))

C =A*B

print C
print np.dot(A,B)

structured = np.array([(1,'First',0.5,1+2j),(2,'Second',1.3,2-2j),(3,'Third',0.8,1+3j)],dtype = ('i2,a6,f4,c8'))
structured.dtype.names = ('id','order','value','complex')
print structured['order']
