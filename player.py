'''
Interface for a player's decisions in the game.
'''

class Player():
    '''
    Represents a player in a game.
    '''

    def __init__(self, name, money, deck):
        self.name = name
        self.money = money
        self.deck = deck
        self.bet = 0
        self.hand = []

    def show_hand(self):
        '''
        Shows the player's hand.
        '''
        print(f"{self.name}'s hand is:")
        if len(self.hand) > 0:
            for card in self.hand:
                print(f"  {card}")
        else:
            print("  empty")

    def hand_value(self):
        '''
        Calculates the value of the cards in the hand.
        '''
        aces = 0
        total = 0
        for card in self.hand:
            if card.is_ace():
                aces += 1
                total += card.get_value()[1]
            else:
                total += card.get_value()[0]

        while total > 21 and aces > 0:
            total -= 10
            aces -= 1
        return total

    def hit(self):
        '''
        Asks for a card, and puts it into the player's hand.
        Returns True if it there was a card to draw, False, otherwise.
        '''
        if not self.deck.is_empty():
            self.hand.append(self.deck.draw())
            return True
        return False

    def stay(self):
        '''
        Does not ask for another card, and does nothing.
        '''
        pass

    def hit_or_stay(self):
        '''
        Gets the player to make a decision.
        '''
        raise NotImplementedError("Subclasses must override the 'hit_or_stay()' function")

    def make_bet(self):
        '''
        Input's the bet, until it is valid.
        '''
        raise NotImplementedError("Subclasses must override the 'input_bet()' function")

    def pay_bet(self):
        '''
        Pays back whatever the bet was.
        '''
        self.money -= self.bet
        iou = self.bet
        self.bet = 0
        return iou
    
    def take_money(self, money):
        '''
        Takes money and adds it to the total money.
        '''
        self.money += money

class HumanPlayer(Player):
    '''
    Let's a human be in control of this instance of the player.
    '''

    def __init__(self, name, money, deck):
        Player.__init__(self, name, money, deck)

    def make_bet(self):
        '''
        Input's the bet, until it is valid.
        '''
        while True:
            print(f"You have ${self.money}.")
            try:
                bet = int(input("How much do you want to bet? $"))
            except:
                print("Sorry, I didn't understand that. Can you try again?\n")
            else:
                if self.money >= bet:
                    self.bet = bet
                    break
                else:
                    print("You don't have enough money. Can you try again?\n")

    def hit_or_stay(self):
        '''
        Gets the player to make a decision.
        Returns True if the player stays, False if the player busts.
        '''
        while self.hand_value() <= 21:
            self.show_hand()
            answer = input(f"{self.name}, would you like to hit? Enter Yes or No: ")

            if len(answer) == 0 or (answer[0].lower() != 'y' and answer[0].lower() != 'n'):
                print("I don't understand. Can you try again?")
                print("")
            elif answer[0].lower() == 'y':
                self.hit()
            elif answer[0].lower() == 'n':
                self.stay()
                return True
        print(f"{self.name}, you got a bust.")
        return False

class AutomatedPlayer(Player):
    '''
    Let's a AI be in control of this instance of the player.
    '''

    def __init__(self, name, money, deck):
        Player.__init__(self, name, money, deck)

    def show_hand(self, show_one):
        if show_one and len(self.hand) > 0:
            print(f"{self.name}'s hand is:")
            print(f"  {self.hand[0]}")
            for _ in self.hand[1:]:
                print(f"  Unknown")
        else:
            Player.show_hand(self)

    def hit_or_stay(self):
        '''
        Gets the player to make a decision.
        Returns True if the player stays, False if the player busts.
        '''
        while self.hand_value() <= 21:
            self.show_hand(False)

            if self.hand_value() >= 17:
                self.stay()
                return True
            self.hit()
        print(f"{self.name} got a bust")
        return False
