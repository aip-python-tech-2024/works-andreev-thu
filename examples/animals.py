class Mammal:
    name: str

    def __init__(self, name: str):
        self.name = name

    def __repr__(self) -> str:
        return f'Mammal(name={self.name})'


class Dog(Mammal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def speak(self):
        print('Woof!')

    def __repr__(self):
        return f'Dog(name={self.name}, breed={self.breed})'


class Cat(Mammal):
    def speak(self):
        print('Meow!')


class Duck:
    def speak(self):
        print('Quack!')


dog: Dog = Dog('Шарик', 'Той-терьер')
cat: Cat = Cat('Феликс')
duck: Duck = Duck()

mammal: Mammal = Mammal('Bobik')
print(mammal)

print(dog)
print(cat)

animals = [dog, cat, duck]
for animal in animals:
    animal.speak()
