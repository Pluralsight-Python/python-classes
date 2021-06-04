"""
    Introduction to data classes
    We can define a class just be specifying the instance attributes we need and decorating the class with
    dataclass decorator
"""
import dataclasses
from string_representations import Position, EarthPosition


@dataclasses.dataclass()
class Location:
    """
        - The dataclass decorator of builtin dataclasses module of python, helps define the classes which
        aim to be used as a structure for holding similar related data.
        - It provides the default implementations for __init__, __repr__ and __eq__ dunder functions
        - The 'type_annotations', although, optional in python everywhere, is 'required' for each data field
        in a data class, because the dataclass uses the type anotations to ignore variables of type 'ClassVar' and
        'InitVar'.
        - This data class works the same way as the 'Location' class defined in <class_decorators.location> module
    """
    name: str
    position: Position


hong_kong = Location('Hong Kong', EarthPosition(latitude=22.29, longitude=114.16))
stockholm = Location('Stockholm', EarthPosition(latitude=59.33, longitude=18.06))
cape_town = Location('Cape Town', EarthPosition(latitude=-33.93, longitude=18.42))
rotterdam = Location('Rotterdam', EarthPosition(latitude=51.96, longitude=4.47))
maracaibo = Location('Maracaibo', EarthPosition(latitude=10.65, longitude=-71.65))
