#Hi! this is a game i made with only 15 lines code!

import random
def random_number():
    return random.randint(1, 10)
def game():
    input('***NUMBER 15*** \n(made by Yibe) \n \npress enter to play: \n')
    for i in range(1):
      number = random_number()
      guess = int(input('guess number: \n'))
      if guess == number:
        print('won! \n \n')
        game()
      else:
        print('lose! \nthe number was: ', number, '\n \n')
        game()
game()
