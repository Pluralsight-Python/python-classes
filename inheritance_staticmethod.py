
from classmethods_bic_code import ShippingContainer
import iso6346


class RefrigeratedShippingContainer(ShippingContainer):

    @staticmethod
    def _make_bic_code(owner_code, serial):
        return iso6346.create(owner_code=owner_code,
                              serial=str(serial).zfill(6),
                              category="R")


if __name__ == '__main__':
    c1 = ShippingContainer("MSD", ["UNKNOWN"])
    print(c1.bic_code)

    r1 = RefrigeratedShippingContainer("MAE", ["meat"])
    print(r1.bic_code)

    if r1.bic_code[3] != "R":
        raise TypeError(f"Wrong category '{r1.bic_code[3]}' for Refrigerated Shipping Container")

