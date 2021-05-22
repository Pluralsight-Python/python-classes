"""
    This shall fail...
"""

import iso6346
from classmethods_bic_code import ShippingContainer


class RefrigeratedShippingContainer(ShippingContainer):

    MAX_CELSIUS = 4.0

    def __init__(self, owner_code, contents, *, celsius, **kwargs):
        super().__init__(owner_code=owner_code, contents=contents, **kwargs)
        if celsius > RefrigeratedShippingContainer.MAX_CELSIUS:
            raise ValueError("Too hot !!")
        self.celsius = celsius

    @staticmethod
    def _make_bic_code(owner_code, serial):
        return iso6346.create(owner_code=owner_code,
                              serial=str(serial).zfill(6),
                              category="R")


if __name__ == '__main__':
    r2 = RefrigeratedShippingContainer.create_empty("YBL", celsius=0.0)
    print(r2.celsius)
    r3 = RefrigeratedShippingContainer.create_with_items("MDF", ["onions"], celsius=10.0)
