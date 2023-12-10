import random


class GuessTheNumber:
    def __int__(self):
        minimum = 1
        maximum = 100

    def guess_the_number(self, minimum, maximum):
        guess = input("Guess the number: ")
        try:
            if int(guess) < self.number:
                print("Too low!")
                self.guess_the_number()
            elif int(guess) > self.number:
                print("Too high!")
                self.guess_the_number()
            else:
                print(f"You won! The number was {guess}.")
        except ValueError:
            print("Invalid input!")
            self.guess_the_number()


GTN = GuessTheNumber()
GTN.guess_the_number()
