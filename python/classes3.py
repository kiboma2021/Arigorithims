'''
Create a class named Person, use the __init__() function to assign values for name and age:
use __str__

'''
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    
    def __str__(self):
        return f"{self.name}({self.age})"
    
P1=Person("Mathew",45)
print(P1)