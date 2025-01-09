from homeworks.point import Point
from homeworks.vehicle import Vehicle


class Car(Vehicle):
    def __init__(self):
        super().__init__()
        self._fuel = 0
        self._fuel_consumption = 1

    def get_fuel(self):
        return self._fuel

    def add_fuel(self, fuel):
        if fuel <= 0:
            print('Cannot reduce fuel')
            return

        self._fuel += fuel

    def move(self, n):
        if n <= 0:
            print('Vehicle cannot move negative times')
            return

        # TODO: вынести определение длины вектора в класс Vector
        total_fuel_consumption = self._fuel_consumption * ((self._velocity.x ** 2 + self._velocity.y ** 2) ** 0.5) * n
        if total_fuel_consumption > self._fuel:
            print('Not enough fuel for movement')
            return
        self._fuel -= total_fuel_consumption

        super().move(n)
