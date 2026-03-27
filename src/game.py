import enum
from random import shuffle

player_hand = []
dealer_hand = []

ranks = {2: "2", 3: "3", 4: "4", 5: "5", 6: "6", 7: "7", 8: "8", 9: "9", 10: "10", 11: "Jack", 12: "Queen", 13: "King", 14: "Ace"}

class Color(enum.Enum):
    RED = "Red"
    BLACK = "Black"

class Suit(enum.Enum):
    HEARTS = ["Hearts", Color.RED]
    DIAMONDS = ["Diamonds", Color.RED]
    CLUBS = ["Clubs", Color.BLACK]
    SPADES = ["Spades", Color.BLACK]

class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __str__(self):
        color_code = "\033[38;2;130;0;0m" if self.suit.value[1] == Color.RED else "\033[38;2;0;0;0m"
        return f"{color_code}{ranks[self.value]} of {self.suit.value[0]}\033[0m"
        
    
deck = [Card(suit, value) for suit in Suit for value in range(2, 15)]

shuffle(deck)
for deck_card in deck:
    print(deck_card)