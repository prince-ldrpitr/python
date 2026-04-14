class employee:
    name = "prince"



    def __init__(self,name,language,salary): 
        self.name = name
        self.language = language
        self.salary = salary
        print("i am constructer")

janak = employee("janak","javascript",100000)
print(janak.name,janak.language,janak.salary)

