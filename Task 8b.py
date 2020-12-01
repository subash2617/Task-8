# Print one message if the try block raises a NameError and another for other errors
try:
    print(x)
except NameError:
    print("variable x is not defined")
except:
    print("something els went wrong,please check again !!!")

#Try getting an input inside the try catch block
try:
    a=int(input("age:"))
    print(a)
except:
    print("error")