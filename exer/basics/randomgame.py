import sys
from random import randint

guess = sys.argv[1]
max = sys.argv[2]
answer = randint(1,int(max))

if int(guess) == answer:
    print("you got it!")
else:
    print(f"random number was {answer}, sorry")