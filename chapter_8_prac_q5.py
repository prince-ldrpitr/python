def pattern(n):
    for i in range(n,0,-1):
        print("*" * n)
n=int(input("enter the number:"))
pattern(n)


# or
def pattern(n):
    for i in range(1, n+1):
        print("*" * (n - i + 1))

n = int(input("enter the number: "))
pattern(n)