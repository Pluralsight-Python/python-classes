"""
    - Inheriting setter properties is quite complex.
    - The best way to inherit properties (getter and setter) is to not inherit them at all.
    - An alternative is to delegate the processing (to be) done in setter/getter to a normal method, which
      can then be easily overridden.
"""
import iso6346


class ShippingContainer:

    HEIGHT_FT = 8.5
    WIDTH_FT = 8.0

    next_serial = 1337

    @classmethod
    def _generate_serial(cls):
        serial = cls.next_serial
        cls.next_serial += 1
        return serial

    @classmethod
    def create_empty(cls, owner_code, **kwargs):
        return cls(owner_code, contents=[], **kwargs)

    @classmethod
    def create_with_items(cls, owner_code, items, **kwargs):
        return cls(owner_code, contents=list(items), **kwargs)

    @staticmethod
    def _make_bic_code(owner_code, serial):
        return iso6346.create(owner_code=owner_code, serial=str(serial).zfill(6))

    @property
    def volume_ft3(self):
        return self._calc_volume()

    # A template method, which can be easily overridden
    def _calc_volume(self):
        return self.HEIGHT_FT * self.WIDTH_FT * self.length_ft

    def __init__(self, owner_code, contents, length_ft, **kwargs):
        self.owner_code = owner_code
        self.contents = contents
        self.length_ft = length_ft
        self.bic_code = self._make_bic_code(self.owner_code, ShippingContainer._generate_serial())


class RefrigeratedShippingContainer(ShippingContainer):

    VOLUME_FRIDGE_FT3 = 100
    MAX_CELSIUS = 4.0

    def __init__(self, owner_code, contents, length_ft, *, celsius, **kwargs):
        super().__init__(owner_code, contents, length_ft, **kwargs)
        self.celsius = celsius

    # Overrides the template method
    # Also, use 'self' to access Class Attribute as this helps in accessing
    # correct inherited attribute based on class instance, e.g. VOLUME_FRIDGE_FT3 is redefined
    # to a different value for HeatedRefrigeratedShippingContainer, using self, we can access
    # each class' own attribute using their instance object.
    def _calc_volume(self):
        return super()._calc_volume() - self.VOLUME_FRIDGE_FT3

    @property
    def celsius(self):
        return self._celsius

    @celsius.setter
    def celsius(self, v):
        self._set_temp(v)

    @property
    def fahrenheit(self):
        return self._c_to_f(self.celsius)

    @fahrenheit.setter
    def fahrenheit(self, vf):
        self.celsius = self._f_to_c(vf)

    @staticmethod
    def _c_to_f(c):
        return c * (9/5) + 32

    @staticmethod
    def _f_to_c(f):
        return (f - 32) * (5/9)

    @staticmethod
    def _make_bic_code(owner_code, serial):
        return iso6346.create(owner_code=owner_code,
                              serial=str(serial).zfill(6),
                              category="R")

    # Another template method, which can be easily overridden
    def _set_temp(self, v):
        if v > RefrigeratedShippingContainer.MAX_CELSIUS:
            raise ValueError("Too hot !!")
        self._celsius = v


class HeatedRefrigeratedShippingContainer(RefrigeratedShippingContainer):

    MIN_CELSIUS = -20
    VOLUME_FRIDGE_FT3 = 200

    def _set_temp(self, v):
        if v < self.MIN_CELSIUS:
            raise ValueError("Too cold !!")
        super()._set_temp(v)
