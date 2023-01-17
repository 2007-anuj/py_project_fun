import random

def r():
    human = input('pick "R" for rock, "P" for paper, "S" for scisors ')
    computer = random.choice(['R', 'P', 'S'])
  

def p(human, computer):
    if (human == 'R' and computer == 'P') or (computer == 'S' and human == 'P') or (human == 'S' and computer == 'R'):
        return 'computer won'
    else:
        return 'human won'

r()