# Project 2 - Hangman

This project is split into two parts: a game function and a decryption function.

Flowcharts for the game and the decrypt functions can be found above.

The hangman games selects a random word that has been encrypted, and gives the user 10 chances to select a letter found in the encrypted word. If the user selects correctly, the dashes are updated to display the letter. If the user selects a letter that is not found in the word, their tries are reduced by one and displayed. Since the words are random letters, the decrypted word will not be shown to the user unless they correctly guess all the letters before the number of tries they have remaining is equal to zero. If they do end up guessing all the correct letters, the output word is decrypted with the decrypt function and displayed to the user.
