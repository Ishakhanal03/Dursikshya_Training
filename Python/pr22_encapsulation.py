# access modifiers
# public : access anywhere from outside the class. eg : self.name
# private : access within the class eg: self.__name
# protected : access within the same class and its sub-classes. eg: self._name


class Employee: 
    # Constructor
    def __init__(self):
        #public 
        self.name="looza Shakya"
        #private
        self.__salary=35000
        #protected
        self._phone=987654321

    # def show(self):
    #     print("Name:",self.name, "salary:",self.salary)


obj_looza=Employee()
name=obj_looza.name
# salary=obj_looza.salary
# obj_looza.show()
# print("Name:",name,"\nsalary:",salary)

# for private : _className__attributename

print('salary:',obj_looza._Employee__salary)
print('Phone Number:',obj_looza._phone)

#self._phone lai sub class baunune 

