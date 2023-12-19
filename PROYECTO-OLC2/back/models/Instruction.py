from abc import ABC, abstractmethod
from .symbolTable.SymbolTable import SymbolTable


class Instruction(ABC):

    def __init__(self, line, column):
        self.line = line
        self.column = column
        super().__init__()

    @abstractmethod
    def execute(self, symbol_table: SymbolTable):
        pass

    @abstractmethod
    def dot(self):
        pass

    @abstractmethod
    def c3d(self,scope):
        pass

    def __str__(self):
        return f"""{{"Instruction": {self.line} {self.column}}}"""
