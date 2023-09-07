import random

class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __str__(self):
        return f"{self.value} of {self.suit}"

class Deck:
    def __init__(self):
        self.cards = []
        self.reset()

    def reset(self):
        self.cards = []
        suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        for suit in suits:
            for value in values:
                self.cards.append(Card(suit, value))

    def deal(self):
        if len(self.cards) == 0:
            return None
        return self.cards.pop()

    def shuffle(self):
        if len(self.cards) < 52:
            self.reset()
        random.shuffle(self.cards)
my_deck = Deck()
my_deck.shuffle()
card = my_deck.deal()
if card is not None:
    print(f"Dealt card: {card}")
else:
    print("No cards left in deck")

