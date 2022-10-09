import random
from word_list import words
import string

def get_word(words):
    secret_word = random.choice(words)
    while "-" in secret_word or " " in secret_word:
        secret_word = random.choice(words)
        
    return secret_word.upper()

def hangman():
    word = get_word(words)
    word_letter = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()
    lives = 6
    
    while len(word_letter) > 0 and lives > 0:
        letter_list = [letter if letter in used_letters else '-' for letter in word]
        print('')
        print("Current word is:", ' '.join(letter_list))
        user_input = input("What is your letter? ").upper()
        if user_input not in used_letters and alphabet:
            used_letters.add(user_input)
            
            if user_input in word_letter:
                word_letter.remove(user_input)
                print(f"Letter {user_input} was in the word, keep going! You still have {lives} lives remaining. \nUsed letters:", ' '.join(used_letters))
            else:
                lives = lives - 1
                if lives == 0:
                    break
                else:
                    print(f"Letter {user_input} was not in the word, you have lost a life and now have {lives} lives remaining! \nUsed letters:", ' '.join(used_letters))
                    
        else:
            print("You have already guessed that letter or its not a valid letter, try again. \nUsed letters:", ' '.join(used_letters))
            
    if len(word_letter) == 0:
        print(f"Congratulations, you won! The word was {word}.")
    else:
        print(f"You have run out of lives and lost, the word was {word}.")

hangman()