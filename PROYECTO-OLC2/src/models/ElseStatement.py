from .Instruction import Instruction
from .symbolTable.SymbolTable import SymbolTable


class ElseStatement(Instruction):

    def __init__(self, line, column, instruction: Instruction):
        super().__init__(line, column)
        self.instruction = instruction

    def execute(self, symbol_table: SymbolTable, errors):
        result = self.instruction.execute(symbol_table, errors)

        if result is None:
            print('A value was expected')

        return result

    def dot(self,nodo_padre, graficador):
        pass
        
    def c3d(self,scope):
        pass