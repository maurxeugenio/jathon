class Collections:
    @staticmethod
    def sort(lst):
        lst.sort()
        return lst

    @staticmethod
    def reverse(lst):
        lst.reverse()
        return lst

    @staticmethod
    def shuffle(lst):
        import random
        random.shuffle(lst)
        return lst
