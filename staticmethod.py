class ShippingContainer:

    next_serial = 1337

    @staticmethod
    def _generate_serial():
        serial = ShippingContainer.next_serial
        ShippingContainer.next_serial += 1
        return serial

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

