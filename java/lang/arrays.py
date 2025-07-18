class Arrays:
    @staticmethod
    def sort(arr):
        arr.sort()
        return arr

    @staticmethod
    def toString(arr):
        return "[" + ", ".join(map(str, arr)) + "]"
