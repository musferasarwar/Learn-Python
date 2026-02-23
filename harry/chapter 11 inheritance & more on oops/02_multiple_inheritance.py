class Employee:   
    company =  "ITC"
    name="default name"
    
    def show(self):
        print(f"the company of the employee {self.name},the language of the employee is {self.company}")

class coder:
    language="Python"
    def printlanguages(self):
        print(f"Out of all the languages here is your language:{self.language}")
    


class programmer(Employee,coder):   
    company="ITC fotech"
    
    def showlanguage(self):
     print(f"the company of the employee {self.company},the language of the employee is {self.language}")

a=Employee()
b=programmer()
c=coder()

a.show()
c.printlanguages() 
b.showlanguage()
