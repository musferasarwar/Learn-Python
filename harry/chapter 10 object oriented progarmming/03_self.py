class Employee:
    
    language = "python"   # class attribute
    salary = 120000000
    
    def info(self):       
        print(f"The language is {self.language}\nThe salary is {self.salary}")
    @staticmethod
    def greet():
        print("good mroning")

musfera = Employee()
musfera.greet()
musfera.info()            
# Employee.info(musfera)  