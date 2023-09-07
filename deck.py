import random
class Deck_Cards():
        l1 = ["Heart", "Spades", "Diamond", "Clubs"]
        l2 = ['A', '2', '3','4', '5', '6', '7', '8', '9', '10', 'K', 'Q', 'J']
        l3=[]
class Cards(Deck_Cards):
    def deal(self):
        x = super().l1
        y = super().l2
        z = super().l3
        a=random.choice(x)
        z.append(a)
        b = random.choice(y)
        z.append(b)
        print(z[1],"of",z[0])
    def shuffle(self):
        x = super().l1
        y = super().l2
        e=len(x)*len(y)
        print("The Deck Has ",e," Cards")
c=Deck_Cards()
d=Cards()
d.deal()
d.shuffle()