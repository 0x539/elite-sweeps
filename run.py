import os
import random
import string


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


def output_things(_things):
    for x in _things:
        print x


class Program:
    def __init__(self):
        self._step = 0
        self._chooser = SweepChooser()
        pass

    def ask_for_participant(self):
        print("Enter participant name or nothing to go to next step: ")
        _in = raw_input()
        if _in == "":
            self._step += 1
        else:
            self._chooser.add_participant(_in)

    def ask_for_option(self):
        print("Enter option name or nothing to go to next step: ")
        _in = string.strip(raw_input())
        if _in == "":
            self._step += 1
        else:
            self._chooser.add_option(_in)

    def clear(self):
        os.system("cls")
        Greeter.greet()

    def run(self):
        while True:
            self.clear()
            if self._step == 0:
                self.ask_for_participant()
            elif self._step == 1:
                self.ask_for_option()
            else:
                print("Participants: ")
                output_things(self._chooser.participants)
                print("\nOptions: ")
                output_things(self._chooser.options)
                self._chooser.match_participants()
                print("\n`Selections: ")
                output_things(self._chooser.selections)
                break


Program().run()
