"""
    - __repr__ method of any class defines the class' default representation, i.e.
        - What should be printed when repr(<classObject>) is called
        - And when classObject is entered on REPL, its __repr__ is returned as the output.
    - The output of repr() is meant to be used by developers for debugging
    - Hence, there are few recommendations on what to return using __repr__:
        - The output of repr should contain as much state information of the class as feasible
        - The output shall be in the form of valid python class Constructor call
    - __str__ method of any class defines its representation when str() is called on its instance.
    - By default, __str__ delegates to __repr__
    - __str__ representation is meant for users and hence should be displayed in natural language form.
"""


class Position:
    def __init__(self, latitude, longitude):
        if not -90 <= latitude <= 90:
            raise ValueError(f"Latitude {latitude} must be in range [-90°, 90°]")
        if not -180 <= longitude <= 180:
            raise ValueError(f"Longitude {longitude} must be in range [-180°, 180°]")

        self._latitude = latitude
        self._longitude = longitude

    @property
    def latitude(self):
        return self._latitude

    @property
    def longitude(self):
        return self._longitude

    @property
    def hemisphere_latitude(self):
        return 'N' if self.latitude >= 0 else 'S'

    @property
    def hemisphere_longitude(self):
        return 'E' if self.longitude >= 0 else 'W'

    # Defining __repr__ as mentioned in __doc__ above
    # Our class has 3 informations: class name: Position and its two args: latitude and longitude
    def __repr__(self):
        # Formatting as a valid class constructor call, and using keyword arguments...
        out = f"{typename(self)}(latitude={self.latitude}, longitude={self.longitude})"
        return out

    def __str__(self):
        """Position coordinates in natural language form ar expressed, for example, as "20° N, 45° W"
           The direction N is chosen for +ve valued latitudes, and E is chosen for +ve valued longitudes, similar
           to Cartesian Coordinate system
        """
        out = f"{self.latitude}° {self.hemisphere_latitude}, " \
              f"{self.longitude}° {self.hemisphere_longitude}"
        return out


class EarthPosition(Position):
    pass


class MarsPosition(Position):
    pass


def typename(obj):
    return type(obj).__name__
