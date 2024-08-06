my_file=open('pr21_text.txt')
print(my_file)
print(my_file.read())


my_file.seek(10)
print(my_file.read())



#readlines(): returns the list of the lines.
my_file.seek(0)
print(my_file.readlines())

# writing in file
# open('filename','w+')
# passing w+ will truncate the original file i.e it deletes the content of the file.
test=open('pr21_text1.txt','w+')
print(test)

test.write('This is the first line of the paragraph.')
test.seek(0)
print(test.read())


# appending (a+)
new_file=open('pr21_text2.txt','a+')
print(new_file)
new_file.write('Dursikshya education Network')
new_file.seek(0)
print(new_file.read())


new_file.close()