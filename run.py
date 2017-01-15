import random

from States import StateManager


class Thing:
    def __init__(self, name):
        self.name = name
        pass

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name


class SweepChooser:
    def __init__(self):
        self.participants = []
        self.options = []
        self.selections = []
        pass

    def add_participant(self, name):
        self.participants.append(Thing(name))

    def add_option(self, name):
        self.options.append(Thing(name))

    def match_participants(self):
        random.shuffle(self.participants)
        random.shuffle(self.options)
        self.selections = zip(self.participants, self.options)


class Greeter:
    def __init__(self):
        pass

    @staticmethod
    def greet():
        print("**********************************************")
        print("***         Sweep stake Generator          ***")
        print("**********************************************")


class Program:
    def __init__(self):
        self._step = 0
        self._chooser = SweepChooser()
        pass

    def run(self):
        StateManager(self._chooser).run()


Program().run()
