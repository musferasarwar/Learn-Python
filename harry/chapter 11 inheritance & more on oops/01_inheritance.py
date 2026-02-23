class Employee:    # parent class or base class
    company =  "ITC"
    
    def show(self):
        print(f"the name of the employee{self.name},the salary of the employee is{self.salary}")
#class progarmmer:
#   company ="ITC fotech"
    
#   def show(self):
#       print(f"the name of the employee{self.name},the salary of the employee is{self.salary}")
        
#  def showlanguage(self):
#    print(f"the name of the employee{self.name},the language of the employee is{self.language}")

class programmer(Employee):   #inheritance class
    company="ITC fotech"
    
    def showlanguage(self):
     print(f"the name of the employee{self.name},the language of the employee is{self.language}")

a=Employee
b=programmer


print(a.company,b.company) 