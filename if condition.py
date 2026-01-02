#take a number as input and check whether it is even or odd?
'''
a = int(input("Enter No:"))
#operators
#1.arithemtic operators : +,-,/,*,//,**,%
#relational/comparison Operator : >,<,>=,<=,==,!=(not equals)
#logical operators: and , or , not
if a%2==0:
    print("Even")
else:
    print("Odd")

'''
#take 2 numbers as input and find the largest no.
'''
a = int(input("Enter No:"))
b = int(input("Enter No:"))

if a>b:
    print(a,"is largest")
else:
    print(b,"is largest")
'''

#take 3 numbers as input and find the largest no.
'''
a = int(input("Enter No1:"))
b = int(input("Enter No2:"))
c = int(input("Enter No3:"))

if a>b and a>c:
    print(a,"is largest")
elif b>c :
    print(b,"is largest")
else:
    print(c,"is largest")
'''
#take 3 sides as input and if they arr forming a traingle which traingle is it?
#equilateral/isoceles/scalene
a = int(input("Enter Side1:"))
b = int(input("Enter Side2:"))
c = int(input("Enter Side3:"))
#nested if else
if a+b>c and b+c>a and c+a>b:
    if a==b and b==c:
        print("Equilateral Traingle")
    elif a==b or b==c or c==a:
        print("Isoceles Traingle")
    else:
        print("Scalene Traingle")
else:
    print("Invalid Sides")
