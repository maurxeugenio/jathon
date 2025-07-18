class String:
    def __init__(self, value):
        self.value = str(value)

    def equals(self, other):
        return self.value == str(other)

    def length(self):
        return len(self.value)

    def charAt(self, index):
        return self.value[index]

    def toUpperCase(self):
        return self.value.upper()

    def toLowerCase(self):
        return self.value.lower()

    def substring(self, start, end=None):
        return self.value[start:end]
