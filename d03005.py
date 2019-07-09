import numpy as np 

A = np.arange(32).reshape(4,4,2)

[B,C] = np.vsplit(A,2)

print A,"\n下面是数组B:\n",B,"\n下面是数组C:\n",C

D = np.arange(16).reshape(4,4)

[E,F] = np.vsplit(D,2)
print D,"\n",E,"\n",F