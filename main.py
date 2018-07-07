'''
Assembles the project, and lets the player play the game.
'''

from deck import Deck
from player import HumanPlayer
from player import AutomatedPlayer

def replay():
    '''
    Returns True if the user would like to play again.
    '''
    while True:
        answer = input("Would you like to play again? Enter Yes or No. ")
        if len(answer) == 0 or (answer[0].lower() != 'y' and answer[0].lower() != 'n'):
            print("I don't understand. Can you try again?")
            print("")
        elif answer[0].lower() == 'y':
            return True
        elif answer[0].lower() == 'n':
            return False

def play(player):
    '''
    Plays Blackjack with the user.
    '''
    input(f"Press Enter to start the game {name}.")
    while True:
        d = Deck()
        d.shuffle()

        player.deck = d
        player.hand = []
        player.make_bet()

        dealer = AutomatedPlayer("Dealer", 100, d)

        # The initialize two cards that the dealer has.
        dealer.hit()
        dealer.hit()

        # The initialize two cards that the player has.
        player.hit()
        player.hit()

        dealer.show_hand(True)

        # if the player busts.
        if not player.hit_or_stay():
            print(f"{player.name} Lost.")
            player.show_hand()
            player.pay_bet()
            if replay():
                continue
            else:
                break

        # if the dealer busts.
        if not dealer.hit_or_stay():
            print(f"Dealer Lost. {player.name} Wins!")
            dealer.show_hand(False)
            player.take_money(player.bet)
            if replay():
                continue
            else:
                break

        # sees who wins and adjusts the money accordingly.
        if dealer.hand_value() >= player.hand_value():
            print(f"{player.name} Lost.")
            player.pay_bet()
            if replay():
                continue
            else:
                break
        else:
            print(f"Dealer Lost. {player.name} Wins!")
            player.take_money(player.bet)
            if replay():
                continue
            else:
                break

if __name__ == "__main__":
    name = input("What is your name? ")
    player = HumanPlayer(name, 100, None)
    play(player)
