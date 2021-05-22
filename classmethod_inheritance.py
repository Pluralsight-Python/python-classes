"""
    This shall fail...
"""

import iso6346
from classmethods_bic_code import ShippingContainer


class RefrigeratedShippingContainer(ShippingContainer):

    MAX_CELSIUS = 4.0

    def __init__(self, owner_code, contents, celsius):
        super().__init__(owner_code=owner_code, contents=contents)
        if celsius > self.MAX_CELSIUS:
            raise ValueError("Too hot !!")
        self.celsius = celsius

    @staticmethod
    def _make_bic_code(owner_code, serial):
        return iso6346.create(owner_code=owner_code,
                              serial=str(serial).zfill(6),
                              category="R")


if __name__ == '__main__':
    # This shall fail...
    # When calling 'create_empty()' named constructor from Derived class, the inherited copy of constructor
    # shall be called which in turn will call Derived class' __init__ method, which expects 3 args.
    # The Base Class' named constructor 'create_empty()' passes only 2 args
    # There is no way (and should not be a way) for Base Class to know number and order of args acceptable
    # to Derived class
    r1 = RefrigeratedShippingContainer.create_empty("YBL")

