# In OOP paradigm everything is an object:


# We use type to check type of an object.
print(type(20))
print(type("hello"))

# to create user define class we have to use keyword: class
# class is a blueprint that defines the nature of object.
# from class we can construct instances.
# An instance is a specific object that is created from the class.


class Student:
    pass

#instance(object) of a class
obj_ram=Student()
print(type(obj_ram))
obj_saksham=Student()
print(type(obj_saksham))