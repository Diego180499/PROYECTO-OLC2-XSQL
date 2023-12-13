from abc import ABC, abstractmethod


class Instruction(ABC):

    def __init__(self, line, column):
        self.line = line
        self.column = column
        super().__init__()

    @abstractmethod
    def execute(self):
        pass

    def __str__(self):
        return f"""{{"Instruction": {self.line} {self.column}}}"""
