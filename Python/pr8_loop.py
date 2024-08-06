#loop : repeatation/iteration
#for loop : for loop executes only on the collection of element
numbers = [1,2,3,4,5,6,7,8,9,10]
for i in numbers:
    print(i,end=" ")

print('\n')


for num in numbers:
    if num%2==0:
        print(num,"is a even number")


fruits=["mango","apple","grapes","kiwi","orange"]
for y in fruits:
    print(y, end=" ")
print('\n')
#break and continue 
for i in fruits:
    if i=='apple':
        break
    print(i)
print("\n")

for a in fruits:
    if a=="apple":
        continue
    print(a)
print('\n')

#range() method
for i in range(10):
    print(i)
print('\n')
for i in range(2,11):
    print(i)
print('\n')


for a in range(10,101,10):
    print(a,end=' ')

print('\n')
