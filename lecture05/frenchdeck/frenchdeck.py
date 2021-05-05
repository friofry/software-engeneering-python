import collections
import collections.abc as abc

Card = collections.namedtuple('Card', ['rank', 'suit'])

class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                                        for rank in self.ranks]
    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]


def main():
    deck = FrenchDeck()
    print(len(deck), deck)
    for c in deck:
        print(c)

    print(list(deck))
    c = Card("2", "hearts")
    print(c)


if __name__ == "__main__":
    main()