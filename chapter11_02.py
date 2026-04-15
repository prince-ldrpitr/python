class Father:
    def skills(self):
        print("Coding aati hai")

class Mother:
    def hobby(self):
        print("Cooking pasand hai")

class Child(Father, Mother):
    pass

obj = Child()
obj.skills()
obj.hobby()