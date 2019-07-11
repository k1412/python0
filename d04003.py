import numpy as np 
import pandas as pd 

frame = pd.DataFrame(np.arange(16).reshape((4,4)),index = ['red','blue','yellow','white'],columns = ['ball','pen','pencil','paper'])
ser  = pd.Series(np.arange(4),index = ['ball','pen','pencil','paper'])
frame1 = frame.drop(['blue','yellow'])
frame2 = frame.drop(['pen','pencil'],axis=1)
# print frame,'\n',frame1,'\n',frame2
print frame
print '\n'
print ser
frame3 = frame - ser
print frame3
frame4 = np.sqrt(frame3)
print frame4