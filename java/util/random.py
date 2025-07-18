import random


class Random:
    def __init__(self, seed=None):
        self._random = random.Random(seed)

    def nextInt(self, bound=None):
        return self._random.randint(
            0, bound - 1
        ) if bound else self._random.randint(0, 2**31 - 1)

    def nextFloat(self):
        return self._random.random()

    def nextBoolean(self):
        return self._random.choice([True, False])
