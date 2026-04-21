def sum(y):
    if(y==1):
        return 1
    return sum(y-1) + y



n=int(input("enter the number:"))
print(sum(n))