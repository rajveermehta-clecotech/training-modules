#revision

import numpy as np

# array using arange
arr=np.arange(0,11)
print(arr)

arr=np.array([1,2,3,4,5,6,7,8])
print(arr)

print(arr.reshape(2,4))

#array max index
print(np.argmax(arr))

# array max
print(np.max(arr))

# reshape
arr1=arr.reshape(2,4)
print(arr1[:1,:])

#print
for i in range(len(arr1)):
        print(arr1[i])

#shape
print(arr1.shape)

#datatype
print(arr1.dtype)


#broadcasting
arr=np.arange(0,10)
print(arr)
arr[:]=100
print(arr)

arr1=arr[0:4].reshape(2,2)
print(arr1)
arr1[:]=11
print(arr)
print(arr1)

#copying

arr2=arr1.copy()
arr2[:]=0
print(arr2)


#comparisons
arr=np.arange(0,100)
arr=arr[arr>90]
print(arr)

