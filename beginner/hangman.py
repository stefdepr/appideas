import re


while True:
    char_shouldnt = set('0123456789')
    the_word_to_guess = input("The word to guess: ")
    if any((c in char_shouldnt)for c in the_word_to_guess):
        print("not a real word")
    else:
        break

hidden_word = ''

for i in range(0, len(the_word_to_guess)):
    hidden_word += 'X'

#print(f"{the_word_to_guess}\n{hidden_word}")

count_guesses = 0
the_word_to_guess = the_word_to_guess.lower()
guessed = False

while count_guesses <= 10 and not guessed:
    print(hidden_word)
    while True:
        guess_letter = input("Guess a letter: ")
        if not guess_letter.isalpha() or len(guess_letter) != 1:
            print("give one letter")
            continue
        else:
            guess_letter = guess_letter.lower()
            break

    count_in_word = -1
    if guess_letter in the_word_to_guess:
        for i in the_word_to_guess:
            count_in_word += 1
            if i == guess_letter:
                hidden_word = hidden_word[0:count_in_word] + guess_letter + hidden_word[count_in_word+1:]
    else:
        count_guesses += 1
        print("Wrong guess")

    if hidden_word == the_word_to_guess:
        print("You've did it!")
        print(f"The hidden word was {hidden_word}")
        guessed = True
    else:
        print(hidden_word)
        print(f"You still have {10-count_guesses} available")








