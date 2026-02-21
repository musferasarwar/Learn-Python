class Employee:
    
    language = "python"   # class attribute
    salary = 120000000
    def __init__(self,name,language,salary):#this is duder method which is automatically called
        self.name=name
        self.language=language
        self.salary=salary
        print("i am creating website")
   
musfera = Employee("musfiar",13000,"c++")
#musfera.name="musfira"
print(musfera.name,musfera.language,musfera.salary)
