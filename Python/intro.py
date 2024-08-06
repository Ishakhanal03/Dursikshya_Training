#filter
arr=np.array([1,2,3,4,5,6,7,8,9,10])
print(f"original array:",arr)
filtered_array=arr[arr%2==0]
print(f'new/filtered array{filtered_array}')


#reshape()
#iterate(loop)


#random number in numpy
from numpy import  random
x=random.randint(50)
print(x)

# to print random number between 0 and 1
x=random.rand()
print(x)


#random array
a=random.randint(50,size=(6))
print(a)

# 2d random array
b=random.randit(50,size=(2,4))
print(b)



#random data distribution
test=random.choice([10,25,15,20,25],p=[0.2,0.0,0.3,0.5])
print(test)




