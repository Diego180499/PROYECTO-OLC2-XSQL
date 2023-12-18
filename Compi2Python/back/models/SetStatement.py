from .Instruction import Instruction
from ..symbolTable.SymbolTable import SymbolTable


class SetStatement(Instruction):

    def __init__(self, line, column, assignments: [Instruction]):
        super().__init__(line, column)
        self.assignments = assignments

    def execute(self, symbol_table: SymbolTable):
        for assignment in self.assignments:
            assignment.execute(symbol_table)
