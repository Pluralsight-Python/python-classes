"""
    Defining getter and setter methods using property decorator
"""
import iso6346
from classmethods_bic_code import ShippingContainer


class RefrigeratedShippingContainer(ShippingContainer):

    MAX_CELSIUS = 4.0

    def __init__(self, owner_code, contents, *, celsius, **kwargs):
        super().__init__(owner_code=owner_code, contents=contents, **kwargs)
        # Using property to set the value...
        # This is called self-encapsulation, when a class internally uses its property getter and setter
        # to get/set attributes
        self.celsius = celsius

    # In Python, 'property' is used to convert 'getter' methods to be used as if they were attributes.
    @property
    def celsius(self):
        return self._celsius

    # If we do not define setter, we can create a Read-Only Attribute
    @celsius.setter
    def celsius(self, v):
        if v > RefrigeratedShippingContainer.MAX_CELSIUS:
            raise ValueError("Too hot !!")
        self._celsius = v

    # A getter need not return the value of an attribute, it can dynamically generate the value
    @property
    def fahrenheit(self):
        return self._c_to_f(self.celsius)

    # Using property 'celsius' instead of attribute '_celsius', helps in checking the Class Invariant Condition
    @fahrenheit.setter
    def fahrenheit(self, vf):
        self.celsius = self._f_to_c(vf)

    # Since these methods do not need the class instance But they are still related to this class,
    # It is better to define these as staticmethod
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

