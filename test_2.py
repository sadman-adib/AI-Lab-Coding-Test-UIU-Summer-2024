import numpy as np

a = np.array([[1,2,3,4,5],
              [6,7,8,9,10],
              [11,12,13,14,15],
              [16,17,18,19,20]])

print(a[1:3, :]) # print middle two rows
print(a.sum(axis = 0)) # column wise sum
c = a[1:2, :]
print(c) # only 2nd row
d = c[c>8] # 2nd row values greater than 8
print(d)
print(sum(d)) # sum of d

