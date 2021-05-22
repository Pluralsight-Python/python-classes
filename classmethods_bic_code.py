import iso6346


class ShippingContainer:

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

    def __init__(self, owner_code, contents, **kwargs):
        self.owner_code = owner_code
        self.contents = contents
        # Calling static method with class object reduces flexibility and extensibility
        # Polymorphic dispatch, i.e. calling static method using derived class instance doesn't work.
        # Hence, self should be used to make polymorphic dispatch work.
        self.bic_code = self._make_bic_code(self.owner_code, ShippingContainer._generate_serial())


if __name__ == '__main__':
    inst = ShippingContainer("MEV", ['bottles'])

    print(inst.bic_code)
    print(inst.owner_code)
    print(inst.contents)
    print(inst.next_serial)
    print(ShippingContainer.next_serial)

