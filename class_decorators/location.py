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
from pprint import pprint
import inspect
from string_representations import EarthPosition, typename, MarsPosition


def class_decorator_auto_repr(_cls):
    """
        This class decorator shall generate __repr__ method for the decorated class
        TODO:
        - Check that class hasn't already defined __repr__
            - Use 'vars()' (or cls.__dir__) to get list of all class members and find __repr__ in that list.
        - Check that class has defined its own __init__, because we shall get the name of the __init__ args from
        __init__ function
            - In the members list, check if __init__ is present.
        - Check that the class has 'properties' defined with same name as the __init__ args name. This is required
        because the decorator references the arg value in the __repr__ with the same name as in the __init__ arg list.
            - Use 'inspect signature' to get list of names of args accepted by __init__
            - Ignore arg1 (= self)
            - For each of the remaining arg names, use 'getattr' to fetch the class attributes by that name
            - Check if each of the attributes is an instance of 'property'
                - This is required because we have a class object at hand.
                - And we cannot create a class instance here, as we will need to pass the values of args to class
                initializer (__init__).
                - If the attributes are defined as self.<attrib>, then they will be instance attributes
                and shall be accessible with instance object only.
                - Hence, the only option we have is to define class 'property' with same name as ahese attributes
        - Define a local function which shall work as __repr__
            - Construct the __repr__ representation of the class as a constructor
        - Use 'setattr' to set the __repr__ attribute of class to the defined function
    """
    members = vars(_cls)
    # pprint(members)

    if '__repr__' in members:
        raise TypeError(f"Class {_cls} already defines __repr__")

    if '__init__' not in members:
        raise TypeError(f"Class {_cls} doesn't override __init__")

    init_signature = inspect.signature(_cls.__init__)
    # pprint(init_signature.parameters)
    init_params = list(init_signature.parameters)[1:]
    # pprint(init_params)

    for param in init_params:
        obj = members.get(param, None)
        # print(obj)
        if not isinstance(obj, property):
            raise TypeError(f"Parameter '{param}' has no corresponding property object defined")

    def custom_repr(_self):
        klass = typename(_self)
        args = ", ".join([
            "{name}={reference!r}".format(
                name=param,
                reference=getattr(_self, param, None)
            ) for param in init_params
        ])
        return f'{klass}({args})'

    setattr(_cls, '__repr__', custom_repr)

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
olympus_mons = Location('Olympus Mons', MarsPosition(latitude=18.65, longitude=46.2))

