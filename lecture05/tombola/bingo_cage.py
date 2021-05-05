import random

from tombola import Tombola


class BingoCage(Tombola):
    def __init__(self, items):
        self._randomizer = random.SystemRandom()
        self._items = []
        self.load(items)

    def load(self, items):
        self._items.extend(items)
        self._randomizer.shuffle(self._items)

    def pick(self):
        try:
            return self._items.pop()
        except IndexError:
            raise LookupError('pick from empty BingoCage')

    def __call__(self):
        self.pick()


def main():
    print(issubclass(BingoCage, Tombola))
    t = BingoCage(range(100))
    print(isinstance(t, Tombola))
    print(BingoCage.__mro__)


if __name__ == "__main__":
    main()

