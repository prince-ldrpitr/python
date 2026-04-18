# custom exception : apna khub ka error banana
a=int(input("enter a number:"))
b=int(input("enter a number:"))
if(b==0):
    raise ZeroDivisionError("hey this is a zerodivisionerroe")
else:
    print(a/b)