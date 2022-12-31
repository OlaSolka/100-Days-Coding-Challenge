#from replit import clear
import random
from word_list import word_list
from logo import logo
from stages import stages

print(logo)
print("Hello! Welcome to the game \"Hangman\"")
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
print(f'Pssst, the solution is {chosen_word}.')
display = []

for letter in chosen_word:
    display.append("_")

print(f"Your word is: {' '.join(display)}")

end_of_game = False
lives = 6

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    print(f" Your guess is \"{guess}\"")
    if guess in display:
        print(f"You've already guessed \"{guess}\"")
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
            print(f"Correct. The letter\"{guess}\" is in this word.")
    if guess not in chosen_word:
        lives -= 1
        print(f"Your guess is incorrect. The letter \"{guess}\" is not in this word. You loose one life.")

    print(stages[lives])
    print(f"Remaining letters: {' '.join(display)}")
    if "_" not in display:
        end_of_game = True
        print("You win.")
    elif lives == 0:
        end_of_game = True
        print("You loose")

print(f"{' '.join(display)}")
