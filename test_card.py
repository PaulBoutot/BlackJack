'''
Tests the card class.
'''

import unittest
from card import PlayCard

class TestCard(unittest.TestCase):
    '''
    Tests the Card class.
    '''

    def test_ace_rank_one(self):
        '''
        Tests to see if card is ace when appropriate.
        '''
        card = PlayCard(PlayCard.suits[0], 1)
        self.assertTrue(card.is_ace())

    def test_ace_all_ranks(self):
        '''
        Tests to see if card is ace when appropriate.
        '''
        for rank in PlayCard.ranks:
            card = PlayCard(PlayCard.suits[0], rank)
            self.assertEqual(card.is_ace(), rank == 1)

    def test_ace_all_suits(self):
        '''
        Tests to see if card is ace when appropriate.
        '''
        for suit in PlayCard.suits:
            for rank in PlayCard.ranks:
                card = PlayCard(suit, rank)
                self.assertEqual(card.is_ace(), rank == 1)

    def test_royal_rank_royal(self):
        '''
        Tests to see if card is royal when appropriate.
        '''
        card = PlayCard(PlayCard.suits[0], 11)
        self.assertTrue(card.is_royal())
        card = PlayCard(PlayCard.suits[0], 12)
        self.assertTrue(card.is_royal())
        card = PlayCard(PlayCard.suits[0], 13)
        self.assertTrue(card.is_royal())

    def test_royal_all_ranks(self):
        '''
        Tests to see if card is royal when appropriate.
        '''
        for rank in PlayCard.ranks:
            card = PlayCard(PlayCard.suits[0], rank)
            self.assertEqual(card.is_royal(), rank in (11, 12, 13))

    def test_royal_all_suits(self):
        '''
        Tests to see if card is royal when appropriate.
        '''
        for suit in PlayCard.suits:
            for rank in PlayCard.ranks:
                card = PlayCard(suit, rank)
                self.assertEqual(card.is_royal(), rank in (11, 12, 13))

    def test_value(self):
        '''
        Tests to see if the value of the card is correct.
        '''
        result = PlayCard(PlayCard.suits[0], 1).get_value()
        self.assertEqual(result, tuple([1, 11]))

    def test_values(self):
        '''
        Tests to see if the value of the card is correct.
        '''
        for rank in PlayCard.ranks:
            result = PlayCard(PlayCard.suits[0], rank).get_value()
            if rank == 1:
                self.assertEqual(result, tuple([1, 11]))
            elif rank in (11, 12, 13):
                self.assertEqual(result, tuple([10]))
            else:
                self.assertEqual(result, tuple([rank]))

if __name__ == "__main__":
    unittest.main()
