"""EX01 - Chardle - A cute step toward Wordle."""

__author__ = "730449902"

word: str = input('Enter a 5-character word: ')

if len(word) != 5:
    print('Error: Word must contain 5 characters')
    exit()

character: str = input('Enter a single character: ')

if len(character) != 1:
    print('Error: Character must be a single character')
    exit()


print('Searching for ' + character + ' in ' + word)

match_count: int = 0

if word[0] == character:
    print(character + ' found at index 0')
    match_count += 1

if word[1] == character:
    print(character + ' found at index 1')
    match_count += 1

if word[2] == character:
    print(character + ' found at index 2')
    match_count += 1

if word[3] == character:
    print(character + ' found at index 3')
    match_count += 1

if word[4] == character:
    print(character + ' found at index 4')
    match_count += 1

if match_count == 0:
    print('No instances of ' + character + ' found in ' + word)

if match_count == 1:
    print(str(match_count) + ' instance of ' + character + ' found in ' + word)
else:
    print(str(match_count) + ' instances of ' + character + ' found in ' + word)