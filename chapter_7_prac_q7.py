n=int(input("enter the number is:"))
for i in range(1,n+1):
    print(" " * (n-i),end="")
    print("*" * (2*i-1))

    # q8

n=int(input("enter the number is:"))
for i in range(1,n+1):
    print("* " *  i)


# q9
n=int(input("enter the number is:"))
for i in range(1,n+1):
    if(i==1 or i==n):
        print("*" * n)
    else:
       print("*",end="")
       print(" " * (n-2),end="")
       print("*")