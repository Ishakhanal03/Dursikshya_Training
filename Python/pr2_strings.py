tex='python is high level programming language.'
print(tex)

#to count the number of chararcters in the string use : len()
print(len(tex))


#indexing
print(tex[0])
print(tex[40])
print(tex[0:10])
print(tex[0:7])
print(tex[0:7])
print(tex[0:])


#built in string methods
#upper: uppercase
print(tex.upper())
print(tex.lower())


#split(): splits from the space and return in the form of list.
print(tex.split())
print(tex.split("high"))


#format string with placeholder
lang='python'
print("we are learning %s"%lang)