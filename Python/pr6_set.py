# set is an unordered collection of unique elements.
x=set()
x.add(1)
x.add(2)
x.add(3)
x.add(1)
print(x)


fruits=("mango","apple","orange","kiwi","mango")
print(set(fruits))
y=set(fruits)
print(y)
for a in y:
    print(a,end=',')



#.union()
set1=x.union(y)
print('\n',set1)


#.update()
x.update(y)
print(x)



#intersection()
set2=x.intersection(y)
print(set2)


#.symmetric_difference()- A-B
set2=x.symmetric_difference(y)
print(set2)