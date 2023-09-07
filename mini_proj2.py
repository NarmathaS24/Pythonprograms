import random
import hashlib
import mysql.connector as mysq
from datetime import datetime
mydb = mysq.connect(host="localhost",user="root",password="Narmatha@24",database="blackjack")
mycursor = mydb.cursor()

def create_player():
    username = input("Enter username: ")
    password = input("Enter password: ")
    encrypted_password = hashlib.sha256(password.encode()).hexdigest()

    # check if the username already exists
    mycursor.execute("SELECT * FROM players WHERE username = %s", (username,))
    result = mycursor.fetchone()
    if result:
        print("Username already exists. Please try again.")
        return

    # insert the new player into the database
    sql = "INSERT INTO players (username, password) VALUES (%s, %s)"
    val = (username, encrypted_password)
    mycursor.execute(sql, val)
    mydb.commit()

    print("Player created successfully!")


def login():
    username = input("Enter username: ")
    password = input("Enter password: ")
    encrypted_password = hashlib.sha256(password.encode()).hexdigest()

    # check if the username and password are correct
    mycursor.execute("SELECT * FROM players WHERE username = %s AND password = %s", (username, encrypted_password))
    result = mycursor.fetchone()
    if not result:
        print("Invalid username or password. Please try again.")
        return

    print("Welcome to Blackjack, {}!".format(username))

    play_game(username)
def play_game(username):
    while True:
        # initialize the deck and deal the initial cards
        deck = Deck()
        player_hand = Hand()
        dealer_hand = Hand()
        player_hand.add_card(deck.deal())
        dealer_hand.add_card(deck.deal())
        player_hand.add_card(deck.deal())
        dealer_hand.add_card(deck.deal())

        print("Your cards: {}".format(player_hand))
        print("Dealer's first card: {}".format(dealer_hand.cards[0]))

        # check for blackjack
        if player_hand.is_blackjack():
            print("Blackjack! You win!")
            result = "win"
            break

        # player's turn
        while True:
            action = input("Do you want to hit or stand? ")
            if action.lower() == "hit":
                player_hand.add_card(deck.deal())
                print("Your cards: {}".format(player_hand))
                if player_hand.is_bust():
                    print("Bust! Dealer wins!")
                    result = "loss"
                    break
            elif action.lower() == "stand":
                break

        # dealer's turn
        if result is None:
            while dealer_hand.get_value() < 17:
                dealer_hand.add_card(deck.deal())
                print("Dealer's cards: {}".format(dealer_hand))
                if dealer_hand.is_bust():
                    print("Dealer busts! You win!")
                    result = "win"
                    break

        # determine the winner
        if result is None:
            player_value

