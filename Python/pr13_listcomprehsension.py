# list comprehension allows us to build out list using different notations.We can think it as one line for loop inside bracket.
numbers=[1,2,3,4,5,6,7]
# result=[x for x in numbers]
result=[x**2 for x in numbers]
print(result)

even_no=[x for x in range(0,21) if x%2==0]
print(even_no)



#celsius to farenheit
celsius=[10,20,30,40,50,60,70,80,90,100]
farenheit=[(9/5)*temp+32 for temp in celsius]
print(farenheit)


#nesing list compreshension
result=[x**2 for x in [x**2 for x in range(0,10)]]
print(result)
