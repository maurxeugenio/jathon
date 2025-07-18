from datetime import datetime


class Date:
    def __init__(self):
        self.now = datetime.now()

    def toString(self):
        return self.now.strftime("%Y-%m-%d %H:%M:%S")

    def getTime(self):
        return int(self.now.timestamp() * 1000)
