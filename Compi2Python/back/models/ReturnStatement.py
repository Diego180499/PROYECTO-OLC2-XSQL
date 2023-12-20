from .Instruction import Instruction
from .symbolTable.SymbolTable import SymbolTable
from .Variable import Variable


class ReturnStatement(Instruction):

    def __init__(self, line, column, instruction: Instruction):
        super().__init__(line, column)
        self.instruction = instruction

    def execute(self, symbol_table: SymbolTable):
        result: Variable = self.instruction.execute(symbol_table)

        if result is None:
            print('A value was expected')

        return result
    