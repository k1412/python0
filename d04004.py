import numpy as np 
import pandas as pd 

def f(x):
    return x.max() - x.min()
frame = pd.DataFrame(np.arange(16).reshape((4,4)),index = ['red','blue','yellow','white'],columns = ['ball','pen','pencil','paper'])

frame1 = frame.apply(f)
frame2 = frame.apply(f,axis=1)
print frame
print frame1
print frame2
frame3 = frame.apply(lambda x:x.max()-x.min(),axis =1)
frame4 = frame.apply(lambda x:pd.Series([x.min(),x.max()],index = ['min','max']))
print frame4
print '\n'
print frame
print '\n'
ser2 = frame.sum(axis=1)
ser3 = frame.mean(axis=1)
print ser2,'\n',ser3,'\n'
print frame.describe()

