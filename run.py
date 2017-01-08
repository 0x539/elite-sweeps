import os
import random
import string


def output_things(_things):
    for x in _things:
        print x


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


class State:
    def __init__(self, chooser):
        self._chooser = chooser
        pass

    def get_next_state(self):
        return None

    def run(self):
        pass


class AskForParticipantState(State):
    def get_next_state(self):
        _input = string.strip(raw_input())
        if _input == "":
            return AskForOptionState(self._chooser)
        else:
            self._chooser.add_participant(_input)
            return self

    def run(self):
        print("Enter participant name or nothing to go to next step: ")


class AskForOptionState(State):
    def get_next_state(self):
        _input = string.strip(raw_input())
        if _input == "":
            return CompleteState(self._chooser)
        else:
            self._chooser.add_option(_input)
            return self

    def run(self):
        print("Enter option name or nothing to go to next step: ")


class CompleteState(State):
    def __init__(self, chooser):
        State.__init__(self, chooser)

    def get_next_state(self):
        return None

    def run(self):
        print("Participants: ")
        output_things(self._chooser.participants)
        print("\nOptions: ")
        output_things(self._chooser.options)
        self._chooser.match_participants()
        print("\nSelections: ")
        output_things(self._chooser.selections)


class StateManager:
    def __init__(self, chooser, initial_state):
        self._chooser = chooser
        self._current_state = initial_state
        pass

    def run(self):
        while True:
            if self._current_state is not None:
                self._current_state.run()
                self._current_state = self._current_state.get_next_state()
            else:
                break
        pass


class Program:
    def __init__(self):
        self._step = 0
        self._chooser = SweepChooser()
        pass

    def run(self):
        _initial_state = AskForParticipantState(self._chooser)
        StateManager(self._chooser, _initial_state).run()


Program().run()
