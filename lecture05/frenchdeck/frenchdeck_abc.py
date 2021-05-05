import collections.abc
import abc.ABC

from random import shuffle
import collections

Card = collections.namedtuple('Card', ['rank', 'suit'])


class FrenchDeck2(collections.abc.MutableSequence):
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                       for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]

    def __setitem__(self, position, value):
        self._cards[position] = value

    def __delitem__(self, position):  # <-- MutableSequence
        del self._cards[position]

    def insert(self, position, value): # <-- MutableSequence
        self._cards.insert(position, value)


def main():
    deck = FrenchDeck2()
    shuffle(deck)
    print(deck[:4])


if __name__ == "__main__":
    main()