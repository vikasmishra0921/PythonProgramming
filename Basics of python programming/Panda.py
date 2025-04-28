import pandas as pd
import numpy as np



c= pd.DataFrame({'IND': [1, 2, 3, 4], 'Value': [10, 20, 30, 40]})
d  = pd.DataFrame(c, columns=["a","b"])

num = np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12],[13,14,15]])
print(num)



print(num.max(axis=1))
print(num.max(axis=0))
print(num.var())
print(num.std())

b = np.array([10,20,30,40])

a = pd.Series(b)
print(a) # 0    10

a = pd.Series(b, index=["IND","USA","UK","NZ"])

print(a)

c=pd.Series([1,2,3,4,5])
print(c) # 0    1
#Series is nothing but a structured form of 1 dimensional array.

print(a["UK"])

c= pd.DataFrame({'IND':[10,20,30],'PAK':[100,200,300]})

print(c['IND'][1])

