#sort
import numpy as np 
import pandas as pd 

frame = pd.DataFrame(np.arange(16).reshape((4,4)),index = ['red','blue','yellow','white'],columns = ['ball','pen','pencil','paper'])
frame2 = pd.DataFrame(np.random.random(16).reshape((4,4)),index = ['red','blue','yellow','white'],columns = ['ball','pen','pencil','paper'])
ser  = pd.Series(np.random.random(4),index = ['ball','pen','pencil','paper'])

print frame2
print frame2.sort_index()
# print frame.sort_values()
print frame2.sort_index(by='red',axis=1)
print frame2.sort_values(by='blue',axis=1)
print ser.sort_index()
print ser.sort_values()
print "新的测试：\n"
print frame2.sort_index(by=['blue','red'],axis=1)