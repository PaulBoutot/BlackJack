'''
A interface for a deck that holds the standard 52 cards.
'''

from random import shuffle
from card import PlayCard

class Deck():
    '''
    A deck that holds the standard 52 cards.
    '''

    def __init__(self):
        self.cards = []
        for suit in PlayCard.suits:
            for rank in PlayCard.ranks:
                self.cards.append(PlayCard(suit, rank))

    def __str__(self):
        cards_string_list = [str(card) for card in self.cards]
        return '[' + ', '.join(cards_string_list) + ']'

    def __len__(self):
        return len(self.cards)

    def shuffle(self):
        '''
        Shuffles the deck.
        '''
        shuffle(self.cards)

    def draw(self):
        '''
        Draws the card at the top of the deck.
        '''
        return self.cards.pop()

    def is_empty(self):
        '''
        Returns true if there are no cards left in the deck.
        '''
        return len(self.cards) == 0

if __name__ == "__main__":
    DECK = Deck()
    print("The deck consists of: {}".format(DECK))
    DECK.shuffle()
    print("The deck shuffled is: {}".format(DECK))
