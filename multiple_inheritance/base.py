"""
    Base file for experiments on multiple inheritance
"""


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


