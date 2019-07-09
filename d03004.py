import numpy as np 

a = np.random.random(24)

A = a.reshape(3,4,2)
print "数组A：\n",A

a.shape = (3,4,2)

print "数组a: \n",a

b = a.ravel()
print "回复的数组a:\n",b            