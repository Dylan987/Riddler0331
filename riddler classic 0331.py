# Riddler Classic from March 31, 2019.
# See https://fivethirtyeight.com/features/can-you-win-a-spelling-bee-if-you-know-99-percent-of-the-words/
# for full problem description

import random


class Contestant:
    def __init__(self, chance):
        self.chance = chance

    def spell(self):
        if random.random()*100 <= self.chance:
            return True
        return False


ctr = 0
n = 0
mode = 0  # if mode == 0, you(99) are the first contestant to spell. if mode == 1, you (99) are the last to spell

for i in range(10000):
    if not mode:
        contestants = [Contestant(99-i) for i in range(10)]
    else:
        contestants = [Contestant(90+i) for i in range(10)]

    while len(contestants) > 1:
        for contestant in contestants:
            if not(contestant.spell()):
                contestants.remove(contestant)
                if len(contestants) == 1:
                    break
    if contestants[0].chance == 99:
        ctr += 1
    n += 1

print(ctr/n)
