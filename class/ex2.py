class Dog:
    species = "Canis familiaris"  # 클래스 변수

    def __init__(self, name, breed):
        self.name = name  # 인스턴스 변수
        self.breed = breed

    def introduce(self):
        return f"My name is {self.name}, I am a {self.breed} and a {self.species}."

# 객체 생성
dog1 = Dog(name = "Buddy", breed="Golden Retriever")
dog2 = Dog(name="Max", breed="Bulldog")

print(dog1.introduce())  # My name is Buddy, I am a Golden Retriever and a Canis familiaris.
print(dog2.introduce())  # My name is Max, I am a Bulldog and a Canis familiaris.
print(dog1.species)  # Canis familiaris (클래스 변수)
