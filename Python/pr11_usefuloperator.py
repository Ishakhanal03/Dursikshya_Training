#range
x=range(0,11)

print(x)
x=list(range(0,11))
print(x)

x=tuple(range(-10,1,2))
print(x)


#enumerate: It is useful while working on for loop
text='hello'
# i=0
# for n in text:
#     print(f"The letter in string at index {i} is {n}")
#     i+=


#simplify using enumerate: by defalult  i=0 and i+=1
for i,n in enumerate(text):
    print("The letter at {} index is {}".format(i,n))


#zip 
list1=[1,2,3,4,5,6]
list2=['a','b','c','d']
print(zip(list1,list2))
print(tuple(zip(list1,list2)))
print(list(zip(list1,list2)))



#max,min
list=[10,20,30,40,50,60,70]
print(max(list))
print(min(list))


#random
from random import shuffle
shuffle(list)
print(list)


from random import randint
print(randint(0,100)) #0-99
