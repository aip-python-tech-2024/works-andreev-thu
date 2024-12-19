class Dog:
    def speak(self):
        print('Woof!')


class Cat:
    def speak(self):
        print('Meow!')


class Duck:
    def speak(self):
        print('Quack!')


dog = Dog()
cat = Cat()
duck = Duck()

animals = [dog, cat, duck]
for animal in animals:
    animal.speak()
