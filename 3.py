class Duck:
    def quack(self):
        print("Quack! Quack!")
    def swim(self):
        print("Splish! Splash!")

class Person:
    def quack(self):
        print("I'm quacking like a duck!")
    def swim(self):
        print("I'm swimming like a duck!")
def make_it_quack_and_swim(thing):
    thing.quack()
    thing.swim()
duck = Duck()
person = Person()
make_it_quack_and_swim(duck)
make_it_quack_and_swim(person)
