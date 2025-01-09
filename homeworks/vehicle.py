from homeworks.point import Point
from homeworks.vector import Vector


class Vehicle:
    def __init__(self):
        self._position = Point(0, 0)
        self._velocity = Vector(0, 0)
        self._way = []
        self._is_recording = False

    def set_velocity(self, velocity):
        self._velocity = velocity

    def move(self, n):
        if n <= 0:
            print('Vehicle cannot move negative times')
            return

        for i in range(n):
            # TODO: сделать сложение точки и вектора в классе Point
            # Нужно, чтоб работало self._position += self._velocity
            self._position.x += self._velocity.x
            self._position.y += self._velocity.y

            if self._is_recording:
                self._way.append(Point(self._position.x, self._position.y))

    def set_recording_on(self):
        self._is_recording = True

    def set_recording_off(self):
        self._is_recording = False

    def print_waypoints(self):
        for point in self._way:
            print(point)