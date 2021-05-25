class Position:
    def __init__(self, lat, long):
        if not -90 <= lat <= 90:
            raise ValueError(f"Latitude {lat} must be in range [-90°, 90°]")
        if not -180 <= long <= 180:
            raise ValueError(f"Longitude {long} must be in range [-180°, 180°]")

        self._latitude = lat
        self._longitude = long

    @property
    def latitude(self):
        return self._latitude

    @property
    def longitude(self):
        return self._longitude


