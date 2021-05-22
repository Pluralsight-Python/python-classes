from typing import Collection, Union, List


class ShippingContainer:

    next_serial = 1337

    def __init__(self, owner_code, contents):
        self.owner_code = owner_code
        self.contents = contents
        self.serial = ShippingContainer.next_serial
        ShippingContainer.next_serial += 1


if __name__ == '__main__':
    inst = ShippingContainer("MEV", ['bottles'])

    print(inst.owner_code)
    print(inst.contents)
    print(inst.serial)
    print(inst.next_serial)
    print(ShippingContainer.next_serial)

