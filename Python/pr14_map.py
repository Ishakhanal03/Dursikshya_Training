#map method allows us to 'map a function iterable objects.It means we can call the function for the single elements in the iterable objects.

def square(num):
    return num**2

numbers=[1,2,3,4,5,6]
# result=map(square,numbers)
# result=list(map(square,numbers))
# result=tuple(map(square,numbers))
result=set(map(square,numbers))

print(result)


def check(n):
    if len(n)%2==0:

        return n[0]
    else:
        return n
    


name=['Ram','Sita','laxmi','hari']
result=list(map(check,name))
print(result)

#filter-. it returns the values which passes the test.
def check_even(num):
    return num%2==0
number=[1,2,3,4,5,6]
result=list(filter(check_even,number))
print(result)

