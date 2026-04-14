class employee:
    company = "Odoo"
    def show(self):
        print(f"my name is {self.name}")

class programer(employee):
    def func(self):
        print(f"my favaourite language is : {self.language}")


a=programer()
a.name="prince"
a.language="python"

a.func()
print(a.company)
