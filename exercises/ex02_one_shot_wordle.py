"""COMP 110 is my favorite class I love Kris Jordan so much."""

__author__ = '730449902'

secret_word = 'python'

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8" 

guess: str = input(f"What is your {len(secret_word)}-letter guess? ")

while len(guess) != len(secret_word):
    if len(guess) != len(secret_word):
        guess = input(f'That was not {len(secret_word)} letters! Try again: ')
# checking if the length of user input is the same length of the secret word


index: int = 0
emoji: str = ''

while index < len(secret_word):
    if guess[index] == secret_word[index]:
        emoji += GREEN_BOX
# assigning green box if the guess is correct for that index
    else:
        wrong_letter: str = guess[index]
        alt_index: int = 0
        character_in_word: bool = False
        while alt_index < len(secret_word):
            if wrong_letter == secret_word[alt_index]:
                character_in_word = True
# running through every character again using an alt index, and creating True bool if there is a match in the word
            alt_index += 1    
        if character_in_word:
            emoji += YELLOW_BOX
# assigning yellow box by checking for character in word bool created earlier
        else:
            emoji += WHITE_BOX
# assigning white box
    index += 1
print(emoji)

if guess == secret_word:
    print('Woo! You got it!')
else:
    print('Not quite. Play again soon!')
# Checking if guess is equal to the secret word and giving user feedbacl
