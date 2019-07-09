import numpy as np 

data = np.random.random(12).reshape(3,4)

np.save('saved_data',data)

