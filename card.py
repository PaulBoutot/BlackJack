'''
Playing cards for blackjack interface
'''

class PlayCard():
    '''
    Represents a poker card.
    '''

    suits = ('Hearts', 'Spades', 'Clubs', 'Diamonds')
    ranks = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13)

    def __init__(self, suit, rank):
        '''
        Initializes this instance of the Card class.
        '''
        self.suit = suit
        self.rank = rank

    def __str__(self):
        '''
        Represents this instance as a string.
        '''
        rank_to_name = {
            1:'Ace',
            2:'Two',
            3:'Three',
            4:'Four',
            5:'Five',
            6:'Six',
            7:'Seven',
            8:'Eight',
            9:'Nine',
            10:'Ten',
            11:'Jack',
            12:'Queen',
            13:'King'
        }
        return f"{rank_to_name[self.rank]} of {self.suit}"

    def get_value(self):
        '''
        Returns the value of this card for the game of BlackJack.
        '''
        if self.is_ace():
            return tuple([1, 11])
        elif self.is_royal():
            return tuple([10])
        return tuple([self.rank])

    def get_color(self):
        '''
        Returns the color of this card.
        '''
        if self.suit in ('Clubs', 'Spades'):
            return 'Black'
        return 'Red'

    def is_royal(self):
        '''
        Returns true if this card is a royal card.
        '''
        return self.rank in (11, 12, 13)

    def is_ace(self):
        '''
        Returns true if this card is an ace.
        '''
        return self.rank == 1
