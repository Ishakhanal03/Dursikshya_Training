# properties of an object is known as attribute

class Student:
    def __init__(self,name,age,address):
        self.Full_Name=name
        self.age=age
        self.address=address

obj_looza=Student(name="Looza Shakya0",age=22,address='indrachowk')
print(f'The name of the student is {obj_looza.Full_Name}.He is {obj_looza.age}years old. He is from {obj_looza.address}')

obj_kusum=Student(name="kusum shrestha",age=22,address='banasthali')
print(f'The name of the student is {obj_kusum.Full_Name}.She is {obj_kusum.age} years old. She is from {obj_kusum.address}')