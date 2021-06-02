"""
    Another example of class decorator, this time using class decorator factory
"""
import functools
from class_decorators.location import *


# A function decorator factory as a starting point for class decorator factory
# This function does a post-method_execution check as defined by predicate
def post_condition(predicate):
    def func_decor(func):
        @functools.wraps(func)
        def wrapper(_self, *args, **kwargs):
            ret = func(_self, *args, **kwargs)
            if not predicate(_self):
                raise RuntimeError(
                    f"The predicate '{predicate.__name__}' failed for function '{func.__name__}(...)' "
                    f"of class {typename(_self)}"
                )
            return ret
        return wrapper
    return func_decor


# The class decorator factory... pretty intuitive
def invariant(predicate):
    func_decor = post_condition(predicate)

    def class_decor(_cls):
        members = list(vars(_cls).items())

        for name, member in members:
            # We cannot use ismethod here, because, the methods are bound to instance. For class, they are functions
            if inspect.isfunction(member):
                decorated_member = func_decor(member)
                setattr(_cls, name, decorated_member)
        return _cls

    return class_decor


# This predicate shall raise error on duplicates
def no_duplicates(_self):
    return len(set(_self._locations)) == len(_self._locations)


# This predicate shall check if the itenerary has at least 2 locations
def at_least_two_locations(_self):
    return len(_self._locations) >= 2


@class_decorator_auto_repr
@invariant(no_duplicates)
@invariant(at_least_two_locations)
class Itinerary:

    def __init__(self, locations):
        self._locations = list(locations)

    @classmethod
    def from_args(cls, *locations):
        return cls(locations)

    def __str__(self):
        return '\n'.join([location.name for location in self._locations])

    @property
    def locations(self):
        return self._locations

    @property
    def origin(self):
        return self.locations[0].name

    @property
    def destination(self):
        return self.locations[-1].name

    def add(self, location):
        self.locations.append(location)

    def remove(self, location):
        self.locations.remove(location)

    def truncate_at(self, location):
        index = self.locations.index(location)
        self._locations = self._locations[:index + 1]


if __name__ == '__main__':
    it1 = Itinerary([rotterdam, stockholm])
