'''
Insert a function that prints a greeting, and execute it on the p1 object

'''
class Person:
    def __init__(self,name):
        self.name=name
    
    def greeting(self):
        print("Hello. My name is ", self.name)

p1=Person(input("Enter your name: "))
p1.greeting()