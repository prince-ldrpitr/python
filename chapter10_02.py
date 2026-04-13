class student:
    name = "prince"
    enrollment = "24BEIT30033"
    sem = "4th"

    def getinfo(self):
        print(f"the language is {self.language}")
    @staticmethod    
    def greet():
        print("good morning")

krishna =  student()
krishna.language = "python"
krishna.greet()
krishna.getinfo()
student.getinfo(krishna)
