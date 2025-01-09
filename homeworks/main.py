from homeworks.car import Car
from homeworks.vector import Vector
from homeworks.vehicle import Vehicle

bicycle = Vehicle()
bicycle.set_recording_on()
bicycle.set_velocity(Vector(5, 3))
bicycle.move(5)
bicycle.set_velocity(Vector(-1, -2))
bicycle.move(3)
bicycle.print_waypoints()

car = Car()
car.add_fuel(15)
car.set_recording_on()
car.set_velocity(Vector(5, 3))
car.move(5)
car.set_velocity(Vector(-1, -2))
car.move(3)
car.print_waypoints()
print(car.get_fuel())
