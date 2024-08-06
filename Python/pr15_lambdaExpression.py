# def square(n):return n**2
#     return n**2


square = lambda num: num**2
result = square(4)
print(result)



list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list(map(lambda n: n**2, list1)))





# args -> when a function parameter starts with the asterrisk ,it allows for an arbitart numbers of arguments and function takes them in a tuple of values.
# def demoFunction(*args):
#     return(args)

demoFunction = lambda *args: args

result = demoFunction(10, 20, 30, 40, 50)
print(result)


# **kwargs: it builds a dictionary of key and value pairs
def favouriteFruit(**kwargs):
    if 'fruits_name' in kwargs:
        return f"My favourite Fruits is {kwargs['fruit_name']}"
    else:
        return"Not my favourite fruits."

show=favouriteFruit(Fruit_name='Mango')
print(show)