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
        for i in range(len(self.ingredients)):
            available[i] =- (num * self.ingredients[i])


pumpkin = Recipe("pumpkin", [1, 0, 3, 4, 3])
apple = Recipe("apple", [0, 1, 4, 3, 2])
cupboard = [10, 14, 10, 42, 24]
made = []

for i in range(pumpkin.max_poss(cupboard)):
    working = cupboard
    pumpkin.make(i, working)
    made.append([i, apple.max_poss(working)])
    made[i].append(sum(made[i]))

maximums = [i[2] for i in made]
max_pies = max(maximums)
max_pump = made[maximums.index(max_pies)][0]
max_app = made[maximums.index(max_pies)][1]
print("{} pies: {} pumpkin, {} apple".format(max_pies, max_pump, max_app))
