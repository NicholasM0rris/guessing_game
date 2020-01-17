import sys
from support.sprecognition import recognise_audio
import random
from support.tts import speak
import os

"""
A guessing game where the player must guess the correct word.
The player has 5 guesses, with a hint given for each guess.
"""


class GuessGame:
    def __init__(self):
        self.words = {}
        self.guess = None
        self.path = 'support/words.txt'
        self.current_word = None
        self.index = 0
        to_say = "Hello! Welcome to my guessing game."
        print(to_say)
        speak(to_say)
        self.play_game()

    def get_guess(self):
        self.guess = recognise_audio()
        try:
            to_speak = "Registered guess: " + self.guess
            print(to_speak)
            speak(to_speak)
        except TypeError:
            pass

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
                to_speak = "DA DUN. YOU LOSE! The correct word was {}".format(self.current_word)
                print(to_speak)
                speak(to_speak)
                return False
            to_speak = 'Guess the word: (You have {} attempts remaining)'.format(5 - self.index)
            print(to_speak)
            speak(to_speak)
            to_speak = self.words[self.current_word][self.index]
            print(to_speak)
            speak(to_speak)
            while not self.get_guess():
                to_speak = "Sorry, I missed that. Please try again!"
                print(to_speak)
                speak(to_speak)

            if self.check_guess():
                to_speak = "Correct! You Winner!"
                print(to_speak)
                speak(to_speak)
                return True
            else:
                self.index += 1
                to_speak = 'WRONG!!!!!!'
                print(to_speak)
                speak(to_speak)


def main(arglist):
    sys.stdout = open(os.devnull, "w")
    sys.stderr = open(os.devnull, "w")
    sys.stdout = sys.__stdout__
    sys.stderr = sys.__stderr__
    game = GuessGame()


if __name__ == '__main__':
    main(sys.argv[1:])
