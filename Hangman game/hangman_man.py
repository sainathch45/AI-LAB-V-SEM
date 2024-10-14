import random

from hangman_words import word_list
from hangman_art import stages,logo
chosen_word=random.choice(word_list)

lives=6
#print(f"Pssst, the solution is {chosen_word}.")
print(logo)
print(len(stages))
display=[]
guessed=[]
for i in range(len(chosen_word)):

    display.append("_")

while "_" in display and lives>0:
    guess=input("Guess a letter:").lower()
    if len(guess)==1 and guess.isalpha():
        if guess in guessed:
            print("letter already present")
            continue
        guessed.append(guess)
        for i in range(len(chosen_word)):
            letter=chosen_word[i]

            if letter==guess:
                display[i]=letter
        if guess not in chosen_word:
            if lives>0:
                lives=lives-1
                if lives==0:
                    print(stages[lives])
                    print(f"The solution is {chosen_word}.")
                    print("You loose")
                    exit(1)
        print(f"{''.join(display)}")
        print(lives)
        print(stages[lives])
    else:
        print("guess hsould be a character rather than a word")
else:
    print("You have won")
