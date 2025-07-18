__author__ = '@marcosfelipp'


class Scanner:
    def __init__(self, source=None):
        self.source = source or input

    def nextLine(self):
        return self.source()

    def nextInt(self):
        return int(self.source())

    def nextFloat(self):
        return float(self.source())

    def next(self):
        return self.source().strip().split()[0]
