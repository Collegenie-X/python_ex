class Dog : 
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed 
        
    def bark(self):
        print(f"{self.name} :says woof!")
        
    def introduce(self):
        print(f"{self.name} and I am a {self.breed}!")
        
        

dog1 = Dog("Buddy", "Golden Retiever ")
dog2 = Dog("Max", "Bulldog")

dog1.bark()
dog2.introduce()