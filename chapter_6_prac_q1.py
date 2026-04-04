n1=int(input("enter the number n1 is:"))
n2=int(input("enter the number n2 is:"))
n3=int(input("enter the number n3 is:"))
n4=int(input("enter the number n4 is:"))
if(n1>n2 and n1>n3 and n1>n4):
    print("the largest number is :",n1)
elif(n2>n1 and n2>n3 and n2>n4):
    print("the largest number is :",n2)
elif(n3>n1 and n3>n2 and n3>n4):
    print("the largest number is :",n3)
else:
    print("the largest number is :",n4)