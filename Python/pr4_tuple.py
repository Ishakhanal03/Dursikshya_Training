# tuple is also a collevtion of elements.It is imutuable i.e we cannot change the elements inside the tuple

fruits=("mango","apple","orange","kiwi","mango")
print(fruits)
print(len(fruits))
print(type(fruits))
print(fruits[1])
print(fruits[1][1])
print(fruits[1:3])
print(fruits[-1])


# .count()
print(fruits.count("mango"))
print(fruits.count("grapes"))

print(fruits.index("orange"))



for x in fruits:
    print(x)


# to convert tuple into list
y=list(fruits)
print(y)


#membership operator
#in operator
print("mango" in fruits)
print("guva" in fruits)

#not in operator
print("mango" not in fruits)
print("guva" not in fruits)


