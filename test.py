import numpy as np

print("Hello, World")

A = np.array([[1,2,3,4,5],
      [6,7,8,9,10],
      [11,12,13,14,15],
      [16,17,18,19,20]],dtype=float)
b = np.array([1,0,1,0,1],dtype=float)
product = np.dot(A,b)
sumaxis0 = np.sum(A,axis=0)
sumaxis1 = np.sum(A,axis=1)
sumaxis2 = np.sum(b,axis=0)
#E2 = np.sum(b,axis=1)
print(product)
print(sumaxis0)
print(sumaxis1)
print(sumaxis2)

a=0
for a in range(0,10):
    a = 2*a+1
    print(a)


a=6
for a in range(1,10):
    if a % 2==0:
       a = a/2
       print(a)
    else:
        a = 3*a+1
        print(a) 

