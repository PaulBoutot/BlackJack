'''
Tests to see if the deck works correctly.
'''

import unittest
from deck import Deck

class TestDeck(unittest.TestCase):
    '''
    Tests the deck class.
    '''

    def test_deck_size(self):
        '''
        Tests to see if the deck is the proper size.
        '''
        deck = Deck()
        self.assertEqual(len(deck), 52)

    def test_deck_size_after_draw(self):
        '''
        Tests to see if the deck size goes down after drawing.
        '''
        deck = Deck()
        deck.draw()
        self.assertEqual(len(deck), 51)

    def test_draw_pull(self):
        '''
        Tests to see that the card that is drawn is the top card of the deck.
        '''
        deck = Deck()
        top_card = deck.cards[-1]
        pull_card = deck.draw()
        self.assertEqual(top_card, pull_card)

    def test_draw_all(self):
        '''
        Tests to see if all cards can be drawn from the deck.
        '''
        deck = Deck()
        while not deck.is_empty():
            deck.draw()
        self.assertEqual(len(deck), 0)

if __name__ == "__main__":
    unittest.main()
