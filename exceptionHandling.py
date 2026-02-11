#2 TYPES OF ERRORS : 
# 1.Compile Time - syntax error
# 2.Run Time - exception (code is okay,still we are getting error)

try:
    x = int(input("Enter No1 : "))
    y = int(input("Enter No2 : "))

    print("Sum = ",x+y)
    print("Diff = ",x-y)
    print("Mul = ",x*y)
    print("div = ",x/y)

# except ZeroDivisionError as ze:
#     print(ze)

# except ValueError as ve:
#     print("Invalid Value")

except BaseException as be:
    print(be)
finally:
    print("Program Ended SuccessFully✅")