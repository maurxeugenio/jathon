__author__ = '@maureugenio'

import sys


class OutStream:
    @staticmethod
    def print(msg):
        sys.stdout.write(str(msg))

    @staticmethod
    def println(msg=""):
        print(msg)


class System:
    out = OutStream()
