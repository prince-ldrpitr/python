class Number:
    def __init__(self, num):
        self.num = num

    def __add__(self, other):
        return self.num + other.num
    
    def __mul__(self, other):
        return self.num * other.num

n1 = Number(5)
n2 = Number(3)

print(n1 + n2)
print(n1 * n2)