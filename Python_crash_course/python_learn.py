# a, b = 9, 10
# print(a & b)  # line 1
# print(a and b) 


l1=[1,2,3,4,5,6,7,8,9]
l2=[9,8,7,6,5,4,3,2,1]


l3=list(zip(l1,l2))
print(l3)

arrays = [['A', 'A', 'B', 'B'], [1, 2, 1, 2]]
tuples = list(zip(* arrays))
print(tuples)
print(*arrays)




class MyClass:
    def add(self, x, y):
        return x + y
    
    def add(self, x, y, z):
        return x + y + z

# The last defined method will be called
obj = MyClass()
print(obj.add(2, 3))      # This will raise an error
print(obj.add(2, 3, 4)) 