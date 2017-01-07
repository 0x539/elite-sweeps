import os


class Thing:
    def __init__(self, name):
        self.name = name
        pass

    def __str__(self):
        return self.name


class SweepChooser:
    def __init__(self):
        self.participants = []
        self.options = []
        pass

    def add_participant(self, name):
        self.participants.append(Thing(name))

    def add_option(self, name):
        self.options.append(Thing(name))


class Greeter:
    def __init__(self):
        pass

    @staticmethod
    def greet():
        print("**********************************************")
        print("***         Sweep stake Generator          ***")
        print("**********************************************")


def output_list(_list):
    for x in _list:
        print x


class Program:
    def __init__(self):
        self._step = 0
        self._chooser = SweepChooser()
        pass

    def ask_for_participant(self):
        print("Enter participant name or nothing to go to next step: ")
        _in = raw_input()
        self._chooser.add_participant(_in)
        if _in == "":
            self._step += 1

    def ask_for_option(self):
        print("Enter option name or nothing to go to next step: ")
        _in = raw_input()
        self._chooser.add_option(_in)
        if _in == "":
            self._step += 1

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
                output_list(self._chooser.participants)
                print("Options: ")
                output_list(self._chooser.options)
                break


Program().run()
