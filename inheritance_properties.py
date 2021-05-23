"""
    How inheritance of properties works
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
        return ShippingContainer.HEIGHT_FT * ShippingContainer.WIDTH_FT * self.length_ft

    def __init__(self, owner_code, contents, length_ft, **kwargs):
        self.owner_code = owner_code
        self.contents = contents
        self.length_ft = length_ft
        # Calling static method with class object reduces flexibility and extensibility
        # Polymorphic dispatch, i.e. calling static method using derived class instance doesn't work.
        # Hence, self should be used to make polymorphic dispatch work.
        self.bic_code = self._make_bic_code(self.owner_code, ShippingContainer._generate_serial())


class RefrigeratedShippingContainer(ShippingContainer):

    VOLUME_FRIDGE_FT3 = 100
    MAX_CELSIUS = 4.0

    def __init__(self, owner_code, contents, length_ft, *, celsius, **kwargs):
        super().__init__(owner_code, contents, length_ft, **kwargs)
        self.celsius = celsius

    # Overridden volume property
    @property
    def volume_ft3(self):
        # This works but duplicates the volume calculation from overridden method
        # return (
        #         ShippingContainer.WIDTH_FT *
        #         ShippingContainer.HEIGHT_FT *
        #         self.length_ft
        #         - RefrigeratedShippingContainer.VOLUME_FRIDGE_FT3)

        # This reuses the overriden method/property
        return super().volume_ft3 - RefrigeratedShippingContainer.VOLUME_FRIDGE_FT3

    @property
    def celsius(self):
        return self._celsius

    @celsius.setter
    def celsius(self, v):
        if v > RefrigeratedShippingContainer.MAX_CELSIUS:
            raise ValueError("Too hot !!")
        self._celsius = v

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


class HeatedRefrigeratedShippingContainer(RefrigeratedShippingContainer):

    MIN_CELSIUS = -20

    # Overridden property setter

    # This doesn't work... Needs full name qualification
    # @celsius.setter

    @RefrigeratedShippingContainer.celsius.setter
    def celsius(self, v):
        # This works but duplicates the MAX CELSIUS check, already done in base class
        # if not (HeatedRefrigeratedShippingContainer.MIN_CELSIUS
        # <= v
        # <= HeatedRefrigeratedShippingContainer.MAX_CELSIUS):
        #     raise ValueError("Temperature out of range !!")

        if v < HeatedRefrigeratedShippingContainer.MIN_CELSIUS:
            raise ValueError("Too cold !!")
        # This does not work...
        # super().celsius = v

        # This works... but references the base class directly by name.
        # This is helpful as the base class implementation of celsius need not be changed
        # A much elegant way is to use Templating... to be discussed next...
        RefrigeratedShippingContainer.celsius.fset(self, v)

