lives = 6
import random
import hangman_words
import hangman_art
from hangman_art import logo

print(logo)

chosen_word = random.choice(hangman_words.word_list)

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print(placeholder)

game_over = False
correct_letter = [ ]

while not game_over:
    guess = input ("Guess a letter: ").lower()

    if guess in correct_letter:
        print(f"You have already guessed {guess} " ) 
    display= ""
    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letter.append(guess )
        elif letter in correct_letter:
            display += letter 
        else:
            display += "_"
    print(display)

    if guess not in chosen_word:
        lives -= 1
        print(f"You have {lives} lives left.")
        if lives == 0:
            game_over = True
            print("You lose.", f"The word was {chosen_word}.") 



    if "_" not in display:
        game_over = True
        print("You win.") 

    print(hangman_art.Stages[6 - lives])