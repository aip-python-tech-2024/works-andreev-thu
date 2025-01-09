class Mammal:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
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


dog = Dog('Шарик', 'Той-терьер')
cat = Cat('Феликс')
duck = Duck()

mammal = Mammal('Bobik')
print(mammal)

print(dog)
print(cat)

animals = [dog, cat, duck]
for animal in animals:
    animal.speak()
