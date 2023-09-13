import random
from phrase import Phrase


class Game():
    def __init__(self):
        self.missed = 0
        self.phrases = [
            Phrase("None shall pass"),
            Phrase("Why so serious"),
            Phrase("May the force be with you"),
            Phrase("To infinity and beyond"),
            Phrase("You shall not pass"),
            Phrase("Nobody expects the spanish inquisition"),
            Phrase("Life is like a box of chocolates"),
            Phrase("A penny for your thoughts"),
            Phrase("The early bird gets the worm"),
            Phrase("Actions speak louder than words"),
            Phrase("An apple a day keeps the doctor away")
        ]
        self.active_phrase = self.random_phrase()
        self.guesses = []
        self.number_missed = 0
        self.play_again = 1

    def start(self):
        while self.number_missed < 5:
            self.active_phrase.display(self.guesses)
            guess = self.get_guess()
            num_guess_remaining = 4 - self.number_missed
            if self.active_phrase.check_complete(self.guesses):
                print(f"\n{self.active_phrase.phrase.upper()}\n")
                print("-"*50)
                print("Congratulations! You guessed the phrase!")
                print("-"*50)
                break
            if self.active_phrase.check_letter(guess):
                pass
            else:
                self.number_missed += 1
                if self.number_missed < 5:
                    print(
                        f"\nIncorrect guess! You have {num_guess_remaining} guesses remaining.")
                else:
                    print("\nGAME OVER\nNo guesses remaining. Try again.")
        while True:
            self.play_again = input(
                "\nWould you like to play again?\n1 = Yes\n2 = No\n>>>  ")
            try:
                self.play_again = int(self.play_again)
            except ValueError:
                print("\nSorry, please enter 1 or 2")
            else:
                break
        return self.get_play_again()

    def get_play_again(self):
        return self.play_again

    def welcome(self):
        lines = "_" * 50
        print(f"{lines}\n\n        Welcome to the Phrase Hunter game!\n{lines}")

    def get_guess(self):
        attempts = 0
        while True:
            if attempts > 3:
                self.active_phrase.display(self.guesses)
            try:
                guess = input(
                    '\n\nGuess a letter:\nOR\nEnter "1" to guess the whole phrase:\n>>>')
                if guess == "1":
                    attempts += 1
                    self.guess_entire_phrase()
                    break
                elif not guess.isalpha():
                    print("\nSorry, please enter a letter or 1")
                    attempts += 1
                elif len(guess) > 1:
                    print("\nSorry, please only enter one letter at a time")
                    attempts += 1
                else:
                    guess = guess.lower()
                    if guess in self.guesses:
                        print("\n\nYou already guessed that letter. Try again")
                        attempts += 1
                    else:
                        self.guesses.append(guess)
                        break
            except ValueError:
                print("\n\nSorry, please enter a single letter")
                break
        return guess

    def random_phrase(self):
        return random.choice(self.phrases)

    def guess_entire_phrase(self):
        entire_phrase = input(
            "\nGuess the entire phrase (letters only) with no punctuation or apostroph:   ").lower()
        if entire_phrase == self.active_phrase.phrase.lower():
            entire_phrase = entire_phrase.replace(" ", "").replace(
                ".", "").replace("'", "").replace("!", "").replace("?", "")
            for letter in entire_phrase:
                if letter not in self.guesses:
                    self.guesses.append(letter)
        else:
            print(
                "\nSorry, that wasn't the phrase! Double check your spelling and try again.")
