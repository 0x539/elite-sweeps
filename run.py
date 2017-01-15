import random

from States import AskForParticipantState


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
