#!/usr/bin/env python
# coding: utf-8

# In[4]:


import random

words =  ["WHDSPQZ", "XHO", "TTDBFRT", "QQJYF", "ENQD", "DNPK", "CNTR", "EHWHOD", "TSVMOHOF", "XNOCFQGTM"]

def random_word():
    word = random.choice(words)
    return word.upper()

def decrypt(word):
    ciphertext = word.upper()
    plaintext = ""
    i = 0
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for letter in ciphertext:
        if i < len(ciphertext):
            if i % 2 == 0:
                cipher_ascii = alphabet.find(letter)
                plain_ascii = cipher_ascii - 1
                plaintext += alphabet[plain_ascii]
                i += 1
            else:
                cipher_ascii = alphabet.find(letter)
                plain_ascii = cipher_ascii + 1
                plaintext += alphabet[plain_ascii]
                i += 1
        else:
            return plaintext
    return plaintext

def hangman(word):
    win = False
    tries = 10
    guessed_letters = []
    board = "-" * len(word)
    print("Let's Begin!")
    print(board)
    print("\n")
    while not win and tries > 0:
        guess = input("Start guessing letters: ").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                #Messages to player
                print("You already guessed that :)", guess)
                print("Guesses remaining: ", tries)
                guessed_letters_join = "".join(guessed_letters)
                print("Guessed Letters: ", guessed_letters_join)
                print("\n")
            elif guess not in word:
                print("Your letter: ", guess, " is not in the word :(")
                tries -= 1
                guessed_letters.append(guess)
                #Messages to player
                print("Guesses remaining: ", tries)
                guessed_letters_join = "".join(guessed_letters)
                print("Guessed Letters: ", guessed_letters_join)
                print("\n")
            else:
                print("You guessed correctly!")
                i = 0
                list_board = list(board)
                for letter in word:
                    if letter == guess:
                        list_board[i] = guess
                        i += 1
                    else:
                        i += 1
                        continue
                board = "".join(list_board)
                print(board)
                #Messages to player
                print("Guesses remaining: ", tries)
                guessed_letters_join = "".join(guessed_letters)
                print("Guessed Letters: ", guessed_letters_join)
                print("\n")
                if "-" not in board:
                    win = True
        elif guess == "STOP":
            break
        if win:
            print("You won!")
            print("The word is: ", decrypt(word))
        elif not win and tries == 0:
            print("Sorry, you lost. The word was: ", word)

def start():
    word = random_word()
    hangman(word)

start()


# In[ ]:




