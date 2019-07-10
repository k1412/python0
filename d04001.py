import pandas as pd 
import numpy as np 
s = pd.Series([1,2,3,4,3,2,1])

print s
s2 = pd.Series([12,32,45,52],index = ['a','v','c','d'])
print s2
print s2.values
print (s2.index)
arr = np.random.random(12)
s3 = pd.Series(arr)
print s3

