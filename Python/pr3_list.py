#list are the collection of elements. List are mutuable i.e element inside the list can be changed.


fruits=["mango","apple","banana","kiwi","orange"]
print(fruits)
print(len(fruits))

#indexing
print(fruits[0])
print(fruits[4])
print(fruits[0][0])
print(fruits[0:3])
print(fruits[2:5])
print(fruits[-1])

#to add element in the list
#.append()
fruits.append('strawbeery')
print(fruits)

#to add element in the particular position
# .insert(index,value)
fruits.insert(3,'berry')
print(fruits)

#to remove the element of the list
#.pop(): removes the element

fruits.pop(3)
print(fruits)


#.remove(value)
fruits.remove("apple")
print(fruits)


#.sort(): accessinding order
fruits.sort()
print(fruits)


#.reverse: reverse the list
fruits.reverse()
print(fruits)


test=[1,2,3,4,5,6,7,89,]
#.clear(): clear will empties the list but the list will remain
test.clear()
print(test)


#del: delete the list
del test
# print(test)


#for loop : for loop can be used only in the collections of the elements
fruit=["mango","apple","banana","kiwi","orange"]
for x in fruit:
    print(x)


# arithemetic operator
#+,-,*,/,%,**(power),//(floor division)
    
    x=20/3
    print(x)

    y=20//3
    print(y)


#Assignment operator
    # = : value assign
    # += : eg: x+=y same as x=x+y
    # -= : eg: x-=y same as x=x-y
    # *= : eg: x*=y same as x=x*y
    # /= : eg: x/=y same as x=x/y
    # %= : eg: x%=y same as x=x%y
    # **= : eg: x**=y same as x=x**y


    x=20
    y=10
    x+=y
    print(x)
    x-=5
    print(x)


#comparison operator
    #<,<=,>,>=,==,!=

    print(12>13)



#logical operator

    # or : returns  true if any one condition is true otherwise returns false
    # and : return if all conditin are true
    # not : returns opposite resluts

    x=12>13 and 13>12
    print(x)

    y=12>13 or 13>12
    print(y)

    z=not(12>13 or 13>12)
    print(z)


#bitwise operator
    # &,| , X-OR(^)
    a=5&1
    print(a)


    b=5|1
    print(b)


    c=5^1
    print(c)






