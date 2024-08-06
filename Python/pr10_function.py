# Function - function is a block of code to perform particular task and it is reuseable
#call the function using parenthesis(). eg: demo()
#define the function using def keyword.




#defining the function
def demoFunction():
    #pass
    print("This is a demoFunction")
#call
demoFunction()
demoFunction()



#fucnction with argument
#define
def addFunction(a,b):
    sum=a+b
    print(f'The sum of a and b is {sum}')




#call the function with argument
addFunction(100,200)
addFunction(10,20)



#function with return type
#define
def subFunction(num1,num2):
    sub=num1-num2
    return sub
#call the function
result=subFunction(2000,400)
print("The sub is :{}".format(result))

list1=[1,2,3,4,5,6,7,8,9,10,11,12]

#define
def checkEven(numberlist):
    even_list=[]
    odd_list=[]
    for num in numberlist:
        if num%2==0:
            even_list.append(num)
        else:
            odd_list.append(num)
    return even_list,odd_list

#call the function
even,odd=checkEven(list1)
print('even:',even)
print('odd:',odd)