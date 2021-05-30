"""
    Practice file for understanding and learning about Class Decorators
"""
from string_representations import Position, EarthPosition, MarsPosition, typename


class Location:

    def __init__(self, name, position):
        self._name = name
        self._position = position

    @property
    def name(self):
        return self._name

    @property
    def position(self):
        return self._position

    def __repr__(self):
        # Returning a constructor-like representation
        return f'{typename(self)}(name={self.name}, position={self.position})'

    def __str__(self):
        return self.name


hong_kong = Location('Hong Kong', EarthPosition(latitude=22.29, longitude=114.16))
stockholm = Location('Stockholm', EarthPosition(latitude=59.33, longitude=18.06))
cape_town = Location('Cape Town', EarthPosition(latitude=-33.93, longitude=18.42))
rotterdam = Location('Rotterdam', EarthPosition(latitude=51.96, longitude=4.47))
maracaibo = Location('Maracaibo', EarthPosition(latitude=10.65, longitude=-71.65))

