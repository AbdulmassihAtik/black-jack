import enum
from random import shuffle
from typing import Iterator
import random

ranks = {2:"2",3:"3",4:"4",5:"5",6:"6",7:"7",8:"8",9:"9",10:"10",11:"J",12:"Q",13:"K",14:"A"}

class Color(enum.Enum):
    RED   = "Red"
    BLACK = "Black"

class Suit(enum.Enum):
    HEARTS   = ("Hearts",   Color.RED)
    DIAMONDS = ("Diamonds", Color.RED)
    CLUBS    = ("Clubs",    Color.BLACK)
    SPADES   = ("Spades",   Color.BLACK)

    def __init__(self, suit_name, color):
        self.suit_name = suit_name
        self.color = color
        
    def __str__(self):                   
        return self.suit_name

class Card:
    def __init__(self, suit: Suit, value: int):
        self.color = suit.color
        self.suit  = suit
        self.value = value

    def __str__(self):
        return f"{ranks[self.value]} of {self.suit.suit_name} ({self.color.value})"

deck = [Card(suit, value) for suit in Suit for value in range(2, 15)]
shuffle(deck)
print("How much do you wanna bet")
bet = int(input())
card_player=[]
card_dealer=[]
card_player.append(random.choice(deck))
card_dealer.append(random.choice(deck))
print("Wanna hit")
if input() == "yes":
    card_player.append(random.choice(deck))
print(card_player)
print(card_dealer)
print("Wanna hit")
if input() == "yes":
    card_player.append(random.choice(deck))
print(card_player)
print(card_dealer)
print("Wanna hit")
if input() == "yes":
    card_player.append(random.choice(deck))
print(card_player)
print(card_dealer)
print("Wanna hit")
if input() == "yes":
    card_player.append(random.choice(deck))
print(card_player)
print(card_dealer)
print("Wanna hit")
if input() == "yes":
    card_player.append(random.choice(deck))
print(card_player)
print(card_dealer)




