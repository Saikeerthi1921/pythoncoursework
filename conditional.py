#conditional statements
age =14

if(age>=18):
    print("can vote")
else:
    print("not eligible")

#example 2
light="blue"

if(light=="red"):   
    print("stop")
elif(light=="green"):
    print("go")
elif(light=="yellow"):
    print("look")
else:
    print("light is broken")
print("end of the code")  

#example 3
marks =int(input("Enter your marks:"))
if(marks >= 90):
    print("grade A")
elif(marks >=80 and marks <90):
    print("grade B")
elif(marks >=70 and marks <80):
    print("grade C")
else:
    print("grade D")


#nesting
#example 4
age = int(input("Enter your age:"))

if(age >= 18):
    if(age >= 80):
        print("can not drive")
    else:
        print("can drive")
else:
    print("cannot drive")


#example 5
number = int(input("Enter numner:"))
if(number%2==0):
    print("Even")
else:
    print("Odd")

#example 6
a = int(input("Enter First Number:"))
b = int(input("Enter second Number:"))
c = int(input("Enter third Number:"))

if(a >= b and a >= c):
    print("First is greatest")
elif(b >= c):
    print("Second is greatest")
else:
    print("Third is greatest")

#example 7
num = int(input("Enter num:"))

if(num%7==0):
    print("multiple of 7")
else:
    print("not a multiple")    


