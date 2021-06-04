"""
    Introduction to data classes
    We can define a class just be specifying the instance attributes we need and decorating the class with
    dataclass decorator
"""
import dataclasses
from string_representations import Position, EarthPosition


# We can parametrize the dataclass constructor and choose to enable/disable default methods generated
# - 'eq' is used to generate __eq__ method. Note that the type/class of the individual fields must also
#   implement __eq__ to give correct results.
# - 'order' enables relational operators/comparisons: __le__, __ge__, __lt__, __gt__
# - The combination of 'eq', 'frozen' can be used to make data classes hashable.
#   - To be hashable, the python object must be immmutable
#   - If two objects have same hash, they may be equal, however, if two objects are equal, they must have
#     same hash.
#   - If both 'eq' and 'frozen' is set True, the data class generates __hash__, i.e. makes data class hashable,
#   - This is possible because, setting 'frozen' to True, makes the data class attributes immutable, i.e. any
#     attempt to set the data class field raises Exception.
#   - Hashability is important because, only hashable objects can be used as 'dict' keys or in 'set'
@dataclasses.dataclass(init=True, repr=True, eq=True, order=False, unsafe_hash=False, frozen=True)
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
    position: EarthPosition


hong_kong = Location('Hong Kong', EarthPosition(latitude=22.29, longitude=114.16))
stockholm = Location('Stockholm', EarthPosition(latitude=59.33, longitude=18.06))
cape_town = Location('Cape Town', EarthPosition(latitude=-33.93, longitude=18.42))
rotterdam = Location('Rotterdam', EarthPosition(latitude=51.96, longitude=4.47))
maracaibo = Location('Maracaibo', EarthPosition(latitude=10.65, longitude=-71.65))


if __name__ == '__main__':
    south_african_capital = Location('Cape Town', EarthPosition(latitude=-33.93, longitude=18.42))
    assert south_african_capital == cape_town
    print("Cape Town is indeed South African capital...")

