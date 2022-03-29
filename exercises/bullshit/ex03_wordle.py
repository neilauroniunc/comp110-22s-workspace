"""Wordle! With 6 guesses tho."""

__author__ = '730449902'


def main() -> None:
    """Main wordle game."""
    secret: str = 'codes'
    turn_num: int = 1
    win_condition: bool = False
    while turn_num <= 6 and not win_condition: 
        print(f'=== Turn {turn_num}/6 ===')
        guess: str = input_guess(len(secret))
        if emojified(guess, secret) == len(secret) * "\U0001F7E9":
            print(emojified(guess, secret))
            print(f'You won in {turn_num}/6 turns!')
            win_condition = True
        else:
            print(emojified(guess, secret))
            turn_num += 1
    if turn_num > 6:
        print('X/6 - Sorry, try again tomorrow!')


def contains_char(search_string: str, search_character: str) -> bool:
    """This function checks whether a given string contains a character, and returns a boolean."""
    assert len(search_character) == 1  # length of character must be 1
    index: int = 0
    char_in_word: bool = False
    while index < len(search_string):  # iterates through string to check for character
        if search_character == search_string[index]:
            char_in_word = True
        index += 1 
    return char_in_word  # returns a bool if the character is in the string


def emojified(guess: str, secret: str) -> str:
    """This function takes two strings of equal length and returns and emojified version, similar to Wordle."""
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8" 
    emoji: str = ''
    assert len(guess) == len(secret)  # asserts that the length of guess is the length of the secret
    index: int = 0
    while index < len(secret):  # iterates through secret to find matching letters
        search_char: str = guess[index]
        if search_char == secret[index]:
            emoji += GREEN_BOX
        else:
            if contains_char(secret, search_char):  # assigning yellow box using contains_char method
                emoji += YELLOW_BOX
            else:
                emoji += WHITE_BOX  # assigns white box
        index += 1    
    return emoji  # returns string of emojis


def input_guess(len_string: int) -> str:
    """This function takes in an input of a given length, and returns it."""
    guess: str = input(f'Enter a {len_string} character word: ')  # prompts user for input
    while len(guess) != len_string:  # checks if input length matches the len_string specified in function call
        guess = input(f'That wasn\'t {len_string} chars! Try again: ')
    return guess  # returns the user input


if __name__ == "__main__":
    main()