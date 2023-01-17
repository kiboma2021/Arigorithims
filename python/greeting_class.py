class Greeting:
    def __init__(self, name):
        self.name = name
    
    def greeting2(self):
        print("Hello", self.name, ".You are the greatest")

my_name = Greeting(input("Please enter your name: "))
print(my_name.name)
my_name.greeting2()