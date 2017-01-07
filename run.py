import os
import string
from sys import stdin, stdout


class Thing:
    def __init__(self, name):
        self.name = name
        pass


class SweepChooser:
    def __init__(self):
        self.participants = []
        self.options = []
        pass


class Greeter:
    def __init__(self):
        pass

    @staticmethod
    def greet():
        print("**********************************************")
        print("***         Sweep stake Generator          ***")
        print("**********************************************")

os.system("cls")

Greeter.greet()

_input = ''

while _input != 'q':
    _input = string.strip(raw_input())
    print(_input)
