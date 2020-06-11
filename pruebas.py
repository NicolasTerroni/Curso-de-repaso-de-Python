# Ahorcado usando listas, usamos ascii arts
import random

IMAGES = ['''
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
    |   |
        |
    =========''', '''
    +---+
    |   |
    O   |
   /|\  |
    |   |
   /    |
        |
    =========''', '''
    +---+
    |   |
    O   |
   /|\  |
    |   |
   / \  |
        |
    =========''']

WORDS = ["python","django","framework","script","shell","scrapping","cookies","cache","editor","evernote","platzi","youtube"]


def display(hidden_word,tries):
    print(IMAGES[tries])
    print("")
    print(f"[{hidden_word}]")

def random_word():
    idx = random.randint(0 , len(WORDS) -1 )
    return WORDS[idx]

def run():
    word = random_word()
    hidden_word = ["-"]*len(word)
    tries = 0
    alive = True
    
    while alive:
        display(hidden_word, tries)
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        get_letter = str(input("Intenta una letra ---> "))

        letter_index = []
        
        for idx in range(len(word)):
            if get_letter == word[idx]:
                letter_index.append(idx)
        
        if len(letter_index) == 0:
            tries += 1
            if tries == 7:
                display(hidden_word, tries)
                print("")
                print(f"Perdiste, la palabra era: {word}")
                alive = False
        else:
            for idx in letter_index:
                hidden_word[idx] = get_letter
            letter_index = []

        if "-" not in hidden_word:
            display(hidden_word, tries)
            print("")
            print(f"Ganaste! la palabra era {word}")
            alive = False
            

if __name__ == "__main__":
    print("------- A H O R C A D O -------")
    run()