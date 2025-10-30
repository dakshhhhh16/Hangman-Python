Stages = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']
lives = 6
world_list = ["python", "java", "kotlin", "javascript"]
import random
chosen_word = random.choice(world_list)
print(chosen_word)

#Step-2 Blank to be filled in by user
placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print(placeholder)

game_over = False
correct_letter = [ ]

while not game_over:
    guess = input ("Guess a letter: ").lower()

 


#Step-3 Changing the for loop so that it checks each letter in the chosen word keeping the correct guesses
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
            print("You lose.") 




    if "_" not in display:
        game_over = True
        print("You win.") 

    print(Stages[6 - lives])