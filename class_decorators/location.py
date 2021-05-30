"""
    Practice file for understanding and learning about Class Decorators
    Class decorators:
    - Like Function Decorators, class decorators are also functions.
    - Class Decorators accept a class object as their argument and return a class object
    - Unlike function decorator
        - which wraps the decorated function and returns the reference to wrapping function with same name as
        wrapped function...
    - ...the class decorator usually modifies the input class object inplace and return the reference to same
    class object.
    - Thus, the Class decorators can be used to add, delete, or modify class attributes dynamically
"""
from string_representations import EarthPosition, typename


def class_decorator_auto_repr(_cls):
    return _cls


@class_decorator_auto_repr
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

    def repr(self):
        # Returning a constructor-like representation
        return f'{typename(self)}(name={self.name!r}, position={self.position!r})'

    def __str__(self):
        return self.name


hong_kong = Location('Hong Kong', EarthPosition(latitude=22.29, longitude=114.16))
stockholm = Location('Stockholm', EarthPosition(latitude=59.33, longitude=18.06))
cape_town = Location('Cape Town', EarthPosition(latitude=-33.93, longitude=18.42))
rotterdam = Location('Rotterdam', EarthPosition(latitude=51.96, longitude=4.47))
maracaibo = Location('Maracaibo', EarthPosition(latitude=10.65, longitude=-71.65))

