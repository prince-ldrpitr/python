def gretest(a,b,c):
    if(a>b and a>c):
        print("a is gretest number :",a)
    elif(b>a and b>c):
        print("b is a gretest number",b)
    else:
        print("c is a gretest number",c)






n1=int(input("enter the number:"))
n2=int(input("enter the number:"))
n3=int(input("enter the number:"))
gretest(n1,n2,n3)