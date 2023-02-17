import random
import Dice_random

class num_game:

    score = 4
    rand_num = random.randint(0, 30)
    prime_list = []

    def __init__(self, guess_num):
        self.guess_num = guess_num

    def guess(self):
        if self.guess_num == num_game.rand_num:
            print("CORRECT!!")
            print("Target number is", num_game.rand_num)
            print("Your guess is", self.guess_num)
            print("Your score is", num_game.score)
        else:
            num_game.score -= 1
            if num_game.score != 0:
                if num_game.score == 3:
                    if num_game.rand_num % 2 != 0:
                        print("_______________________________________________")
                        print("INCORRECT!!")
                        print("HINT!!")
                        print("This number is odd number")
                        print("Your current score is", num_game.score)
                        print("_______________________________________________")
                    else:
                        print("_______________________________________________")
                        print("INCORRECT!!")
                        print("HINT!!")
                        print("This number is even number")
                        print("Your current score is", num_game.score)
                        print("_______________________________________________")
                elif num_game.score == 2:
                    if num_game.rand_num > 15:
                        print("_______________________________________________")
                        print("INCORRECT!!")
                        print("HINT!!")
                        print("This number is greater than 15")
                        print("Your current score is", num_game.score)
                        print("_______________________________________________")
                    else:
                        print("_______________________________________________")
                        print("INCORRECT!!")
                        print("HINT!!")
                        print("This number is less than or equal to 15")
                        print("Your current score is", num_game.score)
                        print("_______________________________________________")
                elif num_game.score == 1:
                    for check in range(1, num_game.rand_num):
                        if num_game.rand_num % check == 0:
                            num_game.prime_list.append(check)
                    num_game.prime_len = len(num_game.prime_list)
                    if len(num_game.prime_list) > 2:
                        print("_______________________________________________")
                        print("INCORRECT!!")
                        print("HINT!!")
                        print("This number is not a prime number")
                        print("Your current score is", num_game.score)
                        print("_______________________________________________")
                    else:
                        print("_______________________________________________")
                        print("INCORRECT!!")
                        print("HINT!!")
                        print("This number is a prime number")
                        print("Your current score is", num_game.score)
                        print("_______________________________________________")
            else:
                print("_______________________________________________")
                print("Unlucky! Try again next time")
                print("The correct answer is", num_game.rand_num)
                print("_______________________________________________")

    def play(self):
        if self.guess_num == num_game.rand_num or num_game.score == 0:
            return False
        elif self.guess_num != num_game.rand_num and num_game.score != 0:
            return True


guess_num = int(input("Enter your guess: "))
guess_game = num_game(guess_num)
guess_game.guess()

while guess_game.play():
    guess_num = int(input("Enter your guess: "))
    guess_game = num_game(guess_num)
    guess_game.guess()