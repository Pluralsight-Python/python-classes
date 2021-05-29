"""
    Base file for experiments on multiple inheritance

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


class SortedList(SimpleList):
    def __init__(self, items=()):
        super().__init__(items)
        self.sort()

    def add(self, item):
        super().add(item)
        self.sort()


class IntList(SimpleList):
    def __init__(self, items=()):
        for i in items: self._validate(i)
        super().__init__(items)

    @staticmethod
    def _validate(val):
        if not isinstance(val, int):
            raise TypeError("IntList expects integer items")

    def add(self, item):
        self._validate(item)
        super().add(item)


class SortedIntList(SortedList, IntList):
    pass


if __name__ == '__main__':
    sil = SortedIntList([29, 39, 21, 41])
    print(f'{sil=}')
    # sil.add(76)
    # try:
    #     sil.add('6')
    # except TypeError as e:
    #     traceback.print_tb(e.__traceback__, file=sys.stdout)
    #
    # print(f'{sil=}')
    #
    # # The __bases__ attribute
    # print(f'{SortedIntList.__bases__=}')
    # print(f'{IntList.__bases__=}')
    # print(f'{SortedList.__bases__=}')
    # print(f'{SimpleList.__bases__=}')

    # Method Resolution Order
    # For classes inheriting from multiple classes, the order of base class in __mro__ is same as their order
    # in class declaration.
    # Also all subclasses come before their base class
    print(f"{SortedIntList.__mro__ = }")
    print(f"{IntList.__mro__ = }")
    print(f"{SortedList.__mro__ = }")
    print(f"{SimpleList.__mro__ = }")


