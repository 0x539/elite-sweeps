import os
import string


def output_things(_things):
    for x in _things:
        print x


class StateManager:
    def __init__(self, chooser, initial_state=None):
        self._chooser = chooser

        if initial_state is None:
            self._current_state = AskForParticipantState(self._chooser)
        else:
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


class State:
    def __init__(self, chooser):
        self._chooser = chooser
        pass

    def get_next_state(self):
        return None

    def run(self):
        os.system("cls")
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
        State.run(self)
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
        State.run(self)
        print("Enter option name or nothing to go to next step: ")


class CompleteState(State):
    def __init__(self, chooser):
        State.__init__(self, chooser)

    def get_next_state(self):
        return None

    def run(self):
        State.run(self)
        print("Participants: ")
        output_things(self._chooser.participants)
        print("\nOptions: ")
        output_things(self._chooser.options)
        self._chooser.match_participants()
        print("\nSelections: ")
        output_things(self._chooser.selections)
