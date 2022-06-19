
class Employee:
    
    count=0
    def __init__(self,name,position,salary):
        self.name=name
        self.position=position
        self.salary=salary
        Employee.count+=1
        
    def displayCount(self):
        print(f"There are {Employee.count} Employee")
        
    
    def displayDetails(self):
        print(f"Name:{self.name}, Position:{self.position},Salary:{self.salary}")
        
#creating objects
employee1=Employee('Sheriff','Software Engineer',1000)
employee2=Employee('Ousman','Food Scientist',5000)


employee1.displayDetails()
employee2.displayDetails()
employee1.displayCount()
