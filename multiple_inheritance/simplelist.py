"""
    Base file for experiments on multiple inheritance
    super()
        - super() is used to call base class methods
        - super(Arg1, Arg2) actually accepts two arguments
            - Arg1 is a Class Object
            - Arg2 shall either be a instance or class object.
            - super() uses the __mro__ of Arg2 to find the class given by Arg1
            - When any method is called (including __init__) using super(), it traverses
            the class objects after the Arg1 class in the MRO to search for called method.
            - It executes the first method reference it finds. And fails if it could not find any.
            - super() on its own returns a SuperProxy Object
                - This Proxy object can be used to call base class methods
                - The Proxy can be Instance-Bound, when super() is called inside a Instance Method
                - Or, the Proxy can be Class-Bound, when super() is called inside a Class Method
                - Instance Bound Proxies figure out the MRO from the 'type()' of instance object Arg2
                - Class Bound Proxies figure out the MRO from the class object passed as Arg2
        - super() cannot be called inside a staticmethod, because, there is no way for super() to
        get Arg2, as neither the instance object (self), nor the class object (cls) is passed to
        a staticmethod.
"""

import sys
import traceback


class SimpleList:
    def __init__(self, items=()):
        self._l = list(items)

    def __len__(self):
        return len(self._l)

    def __getitem__(self, index):
        return self._l[index]

    def __repr__(self):
        return f"{type(self).__name__}({self._l})"

    def sort(self):
        return self._l.sort()

    def add(self, item):
        self._l.append(item)

    @staticmethod
    def dummy():
        print(f"StaticMethod called in SimpleList")


class SortedList(SimpleList):
    def __init__(self, items=()):
        super().__init__(items)
        self.sort()

    def add(self, item):
        super().add(item)
        self.sort()

    @staticmethod
    def dummy():
        print(f"StaticMethod called in SortedList")
        super().dummy()


class IntList(SimpleList):
    def __init__(self, items=()):
        _super = super()
        for i in items:
            self._validate(i)
        _super.__init__(items)
        print(f'{_super = }')
        print(f"{_super.__init__ = }")

    @staticmethod
    def dummy():
        print(f"StaticMethod called in IntList")
        super().dummy()

    @staticmethod
    def _validate(val):
        if not isinstance(val, int):
            raise TypeError("IntList expects integer items")

    def add(self, item):
        self._validate(item)
        super().add(item)


class SortedIntList(SortedList, IntList):
    @staticmethod
    def dummy():
        print(f"StaticMethod called in SortedIntList")
        super().dummy()


if __name__ == '__main__':
    sil = SortedIntList([29, 39, 21, 41])
    print(f'{sil = }')
    sil.add(76)
    try:
        sil.add('6')
    except TypeError as e:
        traceback.print_tb(e.__traceback__, file=sys.stdout)

    print(f'{sil = }')

    # The __bases__ attribute
    print(f'{SortedIntList.__bases__ = }')
    print(f'{IntList.__bases__ = }')
    print(f'{SortedList.__bases__ = }')
    print(f'{SimpleList.__bases__ = }')

    # Method Resolution Order
    # For classes inheriting from multiple classes, the order of base class in __mro__ is same as their order
    # in class declaration.
    # Also all subclasses come before their base class
    print(f"{SortedIntList.__mro__ = }")
    print(f"{IntList.__mro__ = }")
    print(f"{SortedList.__mro__ = }")
    print(f"{SimpleList.__mro__ = }")
    print(f"{sil.__class__.__mro__ = }")

    # This shall fail...
    empty = SortedIntList([])
    print("Calling super() inside staticmethod shall fail:")
    try:
        empty.dummy()
    except Exception as e:
        print(f"{e}\n")
        traceback.print_tb(e.__traceback__, file=sys.stdout)

