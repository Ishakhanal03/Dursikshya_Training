# dictionary is a key value paired data
student={
    'firstname':'Looza',
    'lastname':'Shakya',
    'age':22,
    'gender':'Male',
    'subject':['html','css','js','python']
}

print(student['firstname'])
print(student['lastname'])
print(student['age'])
print(student['gender'])
print(student['subject'][0])
print(type(student))
print(len(student))



#loop
for x in student:
    # print(x)
    print(x,':',student[x])


#.key()-> returns all the key of the dictionary
#.values()-> returns all the values of the dictionary
print(student.keys())
print(student.values())

d={}
d['fruits']='mango'
d['sports']='football'
print(d)

#nesting with dictionary
nest_dict={'key':{'nestkey':{'subnestkey':'final result'}}}
print(nest_dict['key'])

print(nest_dict['key']['nestkey'])
print(nest_dict['key']['nestkey']['subnestkey'])


#nestlist(nesting with list)
list=['a',['b','c',['d','e','f']]]
print(list[1])
print(list[1][0])
print(list[1][2][0])
print(list[1][2][2])



