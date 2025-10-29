#Step-1 Choose and assign a word to be guessed

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
guess = input ("Guess a letter: ").lower()


#Step-3 Check if letter is in the word
display= ""
for letter in chosen_word:
    if letter == guess:
        display += letter
    else:
        display += "_"
print(display)