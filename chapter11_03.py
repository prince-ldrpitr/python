class employee():

    a=1
    def __init__(self):
        print("employee constructer")
    


class programer(employee):
    b=2
    def __init__(self):
        print("programer constructer")


class manager(programer):
    c=3
    def __init__(self):
        super().__init__()
        print("manager constructer")


a=manager()
print(a.a,a.c)