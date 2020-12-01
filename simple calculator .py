def add(x,y):
    return x+y
def subtract(x,y):
    return x-y
def multiply(x,y):
    return x*y
def divide(x,y):
    return x/y
a=int(input("Enter a value:"))
choice = input("Enter +,-,* or /: ")
b=int(input("Enter b value:"))
try:
     if choice == '+':
            print(a, "+", b, "=", add(a,b))
     elif choice == '-':
            print(a, "-",b, "=", subtract(a,b))
     elif choice == '*':
            print(a, "*",b, "=", multiply(a,b))
     elif choice == '/':
            print(a, "/",b, "=", divide(a,b))
     else:
            print("Invalid Input")
except exception as ex:
    print("error:()".format(str(ex)))