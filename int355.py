#!/usr/bin/env python3


class Recipe:
    def __init__(self, name, ingredients):
        self.name = name
        self.ingredients = ingredients

    def max_poss(self, available, limits=[]):
        """Returns the maximum pies of object type that can be made."""
        for i in range(len(self.ingredients)):
            if self.ingredients[i] != 0:
                limits.append(available[i] / self.ingredients[i])
            else:
                continue
        return int(min(limits))

    def make(self, num, available):
        """Reduces the available ingredients by the amount required (num)."""
        for i in range(len(self.ingredients)):
            available[i] -= (num * self.ingredients[i])
            

class Cupboard:
    def __init__(self, contents):
        self.contents = contents


pumpkin = Recipe("pumpkin", [1, 0, 3, 4, 3])
apple = Recipe("apple", [0, 1, 4, 3, 2])
cupboard = Cupboard([12,4,40,30,40])
working = Cupboard([12,4,40,30,40])
made = []


for i in range((pumpkin.max_poss(cupboard.contents)) + 1):
    print(cupboard.contents)# Debugging.
    pumpkin.make(i, working.contents)
    print(cupboard.contents) # Debugging.
    made.append([i, apple.max_poss(working.contents)])
    made[i].append(sum(made[i]))
    working = Cupboard([12,4,40,30,40])

print(made) # Debugging.

maximums = [i[2] for i in made]
max_pies = max(maximums)
max_pump = made[maximums.index(max_pies)][0]
max_app = made[maximums.index(max_pies)][1]
print("{} pies: {} pumpkin, {} apple".format(max_pies, max_pump, max_app))
