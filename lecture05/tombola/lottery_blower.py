import random

from tombola import Tombola


class LotteryBlower(Tombola):
    def __init__(self, iterable):
        self._balls = list(iterable)

    def load(self, iterable):
        self._balls.extend(iterable)

    def pick(self):
        try:
            position = random.randrange(len(self._balls))
        except ValueError:
            raise LookupError('pick from empty BingoCage')
        return self._balls.pop(position)

    def loaded(self):
        return bool(self._balls)

    def inspect(self):
        return tuple(sorted(self._balls))


def main():
    print(issubclass(LotteryBlower, Tombola))
    t = LotteryBlower(range(100))
    print(isinstance(t, Tombola))
    print(LotteryBlower.__mro__)


if __name__ == "__main__":
    main()

