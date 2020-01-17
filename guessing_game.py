import sys
from support.sprecognition import recognise_audio
import random

"""
A guessing game where the player must guess the correct word.
The player has 5 guesses, with a hint given for each guess.
"""


class GuessGame:
    def __init__(self):
        self.words = {}
        self.guess = None
        self.path = 'Lisbeth/guessing_game/words.txt'
        self.current_word = None
        self.index = 0
        self.play_game()

    def get_guess(self):
        self.guess = recognise_audio()
        print("Registered guess: ", self.guess)
        # failed to get user response
        if not self.guess:
            return False
        else:
            return self.guess

    def load_hints(self):
        with open(self.path, 'r') as f:
            word_list = f.read().splitlines()
            for idx, line in enumerate(word_list):
                if idx % 6 == 0:
                    self.words[line[6:]] = [word_list[idx + 1], word_list[idx + 2], word_list[idx + 3],
                                            word_list[idx + 4], word_list[idx + 5]]

    def choose_word(self):
        self.current_word = random.choice(list(self.words.keys()))

    def check_guess(self):
        if self.current_word.lower() in self.guess:
            return True
        else:
            return False

    def play_game(self):
        self.load_hints()
        self.choose_word()
        while True:
            if self.index >= 5:
                print("DA DUN. YOU LOSE!")
                return False

            print('Guess the word: (You have {} attempts remaining)'.format(5-self.index))
            print(self.words[self.current_word][self.index])
            while not self.get_guess():
                print("Sorry, I missed that. Please try again!")

            if self.check_guess():
                print("Correct! You Winner!")
                return True
            else:
                self.index += 1
                print('WRONG!!!!!!')



def main(arglist):
    game = GuessGame()




if __name__ == '__main__':
    main(sys.argv[1:])
