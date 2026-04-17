try:
    a = int(input("Number dalo: "))
    b = int(input("Number dalo: "))
    print(a / b)
except:
    print("Error aaya hai")


# Specific Exception Handle karna
try:
    a = int(input())
    b = int(input())
    print(a / b)
except ZeroDivisionError:
    print("0 se divide nahi kar sakte")
except ValueError:
    print("Galat input diya hai")

# else block (Agar error nahi aata tab chalta hai):

try:
    a = 5
    b = 2
    print(a / b)
except:
    print("Error")
else:
    print("Sab sahi chala")