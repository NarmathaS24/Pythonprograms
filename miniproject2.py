import random
import hashlib
import mysql.connector
from datetime import datetime

# Connect to the MySQL database
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Narmatha@24",
    database="blackjack"
)
cursor = db.cursor()

# Create player table if it doesn't exist
cursor.execute(
    "CREATE TABLE IF NOT EXISTS players (id INT AUTO_INCREMENT PRIMARY KEY, username VARCHAR(255) UNIQUE, password VARCHAR(255))")

# Create results table if it doesn't exist
cursor.execute(
    "CREATE TABLE IF NOT EXISTS results (id INT AUTO_INCREMENT PRIMARY KEY, player_id INT, dealer_score INT, player_score INT, result VARCHAR(255), timestamp TIMESTAMP)")


# Function to encrypt the password using SHA-256 algorithm
def encrypt_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


# Function to validate the user's login credentials
def validate_login(username, password):
    hashed_password = encrypt_password(password)
    cursor.execute("SELECT id FROM players WHERE username = %s AND password = %s", (username, hashed_password))
    player = cursor.fetchone()
    return player


# Function to register a new user
def register_user(username, password):
    hashed_password = encrypt_password(password)
    cursor.execute("INSERT INTO players (username, password) VALUES (%s, %s)", (username, hashed_password))
    db.commit()
    return cursor.lastrowid


# Function to deal a new card
def deal_card():
    cards = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
    return random.choice(cards)


# Function to calculate the value of the hand
def calculate_hand(hand):
    score = 0
    aces = 0
    for card in hand:
        if card.isdigit():
            score += int(card)
        elif card in ["J", "Q", "K"]:
            score += 10
        elif card == "A":
            aces += 1
            score += 11
    while score > 21 and aces > 0:
        score -= 10
        aces -= 1
    return score


# Function to display the player's hand and dealer's visible card
def display_game(dealer_hand, player_hand):
    print("Dealer's card: [{}]".format(dealer_hand[0]))
    print("Your cards: {}".format(player_hand))


# Function to play the dealer's turn
def play_dealer_turn(dealer_hand):
    dealer_score = calculate_hand(dealer_hand)
    while dealer_score < 17:
        dealer_hand.append(deal_card())
        dealer_score = calculate_hand(dealer_hand)
    return dealer_hand, dealer_score


# Function to play the player's turn
def play_player_turn(player_hand):
    player_score = calculate_hand(player_hand)
    while player_score < 21:
        action = input("Do you want to Hit or Stand? ")
        if action.lower() == "hit":
            player_hand.append(deal_card())
            player_score = calculate_hand(player_hand)
            print("Your cards: {}".format(player_hand))
        elif action.lower() == "stand":
            break
    return player_hand, player_score


# Function to display the result of the game and update the results table
def display_result(player_score, dealer_score, player_id):
    if player_score > 21:
        result = "Busted"
    elif player_score == dealer_score:
        result = "Push"
    elif player_score == 21:

