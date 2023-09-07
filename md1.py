import random
words = ['apple', 'banana', 'cherry', 'date','fig', 'grape', 'kiwi', 'lemon']
word = random.choice(words)
name = input("Enter your name: ")
turns = 12
word_letters = set(word)
guessed_letters = set()
while turns > 0 and word_letters != guessed_letters:
    print(f"You have {turns} turns remaining.")
    print("Letters guessed so far:", end=' ')
    for letter in word:
        if letter in guessed_letters:
            print(letter, end=' ')
        else:
            print('_', end=' ')
    print()
    letter = input("Guess a letter: ").lower()
    if letter in guessed_letters:
        print("You already guessed that letter. Try again.")
        continue
    guessed_letters.add(letter)
    if letter in word_letters:
        print("Good guess!")
    else:
        print("Sorry, that letter is not in the word.")
        turns -= 1
if word_letters == guessed_letters:
    print(f"Congratulations {name}! You guessed the word '{word}' in {12 - turns} turns.")
else:
    print(f"Sorry {name}, you ran out of turns. The word was '{word}'.")