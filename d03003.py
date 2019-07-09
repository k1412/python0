#自定义numpy中的聚合函数

import numpy as np 



def NarraryMax(Narray):
    temp = 0
    for i in Narray:
        if i>=temp:
            temp = i
    return temp
        
a = np.arange(0,12).reshape([3,4])
print(a)
b = np.apply_along_axis(NarraryMax, axis = 1, arr = a)
print(b)


