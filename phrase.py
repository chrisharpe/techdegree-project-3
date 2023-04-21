import random


class Phrase:
    def __init__(self, phrase):
        self.phrase = phrase.lower()

    def __str__(self):
        return self.phrase

    def display(self, guesses):
        print("\n")
        for letter in self.phrase:
            if letter in guesses:
                print(letter, end=" ")
            elif letter == " ":
                print(" ", end=" ")
            else:
                print("_", end=" ")

    def check_letter(self, letter):
        return letter in self.phrase

    def check_complete(self, guesses):
        for letter in self.phrase:
            if letter not in guesses and letter != ' ':
                return False
        return True
