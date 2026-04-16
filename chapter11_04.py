class employee:
    a=1
    @classmethod
    def show(self):
        print(f"the value of a is:{self.a}")



p=employee()
p.a=45
p.show()