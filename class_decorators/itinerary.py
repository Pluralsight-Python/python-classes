"""
    Another example of class decorator, this time using class decorator factory
"""
import functools
from .location import *


# A function decorator factory as a starting point for class decorator factory
# This function does a post-method_execution check as defined by predicate
def post_condition(predicate):
    def func_decor(func):
        @functools.wraps(func)
        def wrapper(_self, *args, **kwargs):
            ret = func(_self, *args, **kwargs)
            if not predicate(_self):
                raise RuntimeError(
                    f"The predicate '{predicate.__name__}' failed for function {func.__name__}"
                )
            return ret
        return wrapper
    return func_decor


# This predicate shall check if the itenerary has at least 2 locations
def at_least_two_locations(_self):
    return len(_self._locations) >= 2


class Itinerary:

    @post_condition(at_least_two_locations)
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

    @post_condition(at_least_two_locations)
    def add(self, location):
        self.locations.append(location)

    @post_condition(at_least_two_locations)
    def remove(self, location):
        self.locations.remove(location)

    @post_condition(at_least_two_locations)
    def truncate_at(self, location):
        index = self.locations.index(location)
        self._locations = self._locations[:index + 1]


if __name__ == '__main__':
    it1 = Itinerary([rotterdam, stockholm])
