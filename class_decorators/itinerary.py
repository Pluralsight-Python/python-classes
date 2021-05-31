"""
    Another example of class decorator, this time using class decorator factory
"""


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
