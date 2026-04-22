def convert(n):
    return n*2.54


n=int(input("enter the number:"))
print(convert(n))

# q8  Write a python function to print multiplication table of a given number. 
def fun(n):
    for i in range(1,11):
        print(f"{n} x {i} = {n*i}")


n=int(input("enter the number:"))
fun(n)