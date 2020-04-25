import random


class Dice:
    def roll(self):
        rv1 = random.randint(1, 10)
        rv2 = random.randint(1, 10)
        rv = (rv1, rv2)
        return rv


dice = Dice()

print(dice.roll())
