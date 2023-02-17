# Import 'random' module to randomize the target number
import random


class num_game:

    # 'score' is the number of guess you can have
    score = 4
    
    # Randomize target number in the range from 0 - 30
    rand_num = random.randint(0, 30)
    prime_list = []

    
    def __init__(self, guess_num):
        self.guess_num = guess_num
    
    # Crete function 'guess' so that the code will check if the guess is correct or not
    def guess(self):
        
        # If the guess is correct, it will show the target number and your score as in how many life you have left
        if self.guess_num == num_game.rand_num:
            print("CORRECT!!")
            print("Target number is", num_game.rand_num)
            print("Your guess is", self.guess_num)
            print("Your score is", num_game.score)
            
        # If the guess is not correct, it decrease the 'score' by one and will show the hint according to how many 'score' you have left
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
                        
            # if the 'score' is equal to 0, game will be over
            else:
                print("_______________________________________________")
                print("Unlucky! Try again next time")
                print("The correct answer is", num_game.rand_num)
                print("_______________________________________________")

    # Crete a function so that the player can continue guessing untill the game is over           
    def play(self):
        if self.guess_num == num_game.rand_num or num_game.score == 0:
            return False
        elif self.guess_num != num_game.rand_num and num_game.score != 0:
            return True

# Player input the guess
guess_num = int(input("Enter your guess: "))
guess_game = num_game(guess_num)
guess_game.guess()

# If function 'play' return as 'True' player will be able to keep guessing. If not the program will finish running
while guess_game.play():
    guess_num = int(input("Enter your guess: "))
    guess_game = num_game(guess_num)
    guess_game.guess()
