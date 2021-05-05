import collections
import collections.abc as abc
from random import shuffle
from frenchdeck import FrenchDeck


def set_card(deck, position, card):
    deck._cards[position] = card


def main():
    # deck = FrenchDeck()
    # shuffle(deck)

    FrenchDeck.__setitem__ = set_card
    deck = FrenchDeck()
    shuffle(deck)
    print(deck[:4])


if __name__ == "__main__":
    main()