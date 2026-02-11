#USER DEFINED FUNCTIONS:HOW TO CREATE YOUR OWN FUNCTION

#function definition
# def f1():
#     print("This is f1 function")

#function calling
# f1()

#parameterised function
# def f1(x,y):
#     print(x+y)

# f1(2,3)

#return value in function

# def f1(x,y):
#     return x+y

# result = f1(3,5)
# print(result)


#TYPES OF PARAMETER :
# 1.Optional parameter
# def f1(a,b=6):
#     print(a+b)

# f1(5,2) 

# * args
# def f1(a,*b):
#     print(f"a={a}, b={b}")

# f1(1,2,3,4,5)

# ** - keyworded Argument

def f1(name,**others):
    print(name,others)

f1("Ravi",age=20,salary=150000)