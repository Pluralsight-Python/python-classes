class ShippingContainer:

    next_serial = 1337

    @classmethod
    def _generate_serial(cls):
        serial = cls.next_serial
        cls.next_serial += 1
        return serial

    @classmethod
    def create_empty(cls, owner_code):
        return cls(owner_code, contents=[])

    @classmethod
    def create_with_items(cls, owner_code, items):
        return cls(owner_code, contents=list(items))

    def __init__(self, owner_code, contents):
        self.owner_code = owner_code
        self.contents = contents
        self.serial = self._generate_serial()


if __name__ == '__main__':
    inst = ShippingContainer("MEV", ['bottles'])

    print(inst.owner_code)
    print(inst.contents)
    print(inst.serial)
    print(inst.next_serial)
    print(ShippingContainer.next_serial)

