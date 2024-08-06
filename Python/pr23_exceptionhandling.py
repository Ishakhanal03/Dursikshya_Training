# error handling/exception handling is used for user friendly error 
# try: test the block of code 
# except: handle the error
# else: execute code when there is no error 
# finally: execute code if there is error or not 


try:
    print("hello World")
    # print(hello,World)

except:
    print("An error occured.")



# multiple except:
    
try:
    print(hello)
except NameError:
    print("Variable is not defined")
except:
    print("There is some error in the code.")
finally:
    print("Exception handling is completed.")


try:
    print(30)
except:
    print("Error occured")
else:
    print("There is no error while processing.")


# pow()
print(pow(3,2))
# abs()
print(abs(-20.5))

import math 
print(math.ceil(20.3))
print(math.floor(19.9))

print(math.pi)

#date and time
import datetime
print(datetime.datetime.now())
x=datetime.datetime.now()
print(x.year)
print(x.month)
d=x.strftime("%A")
print(d)

