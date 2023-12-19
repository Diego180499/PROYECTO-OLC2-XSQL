from .Instruction import Instruction
from .symbolTable.SymbolTable import SymbolTable
from .Variable import Variable
from .SymbolType import SymbolType
import re


class Assignment(Instruction):

    def __init__(self, line, column, id: str, value: Instruction):
        super().__init__(line, column)
        self.id = id
        self.value = value

    def execute(self, symbol_table: SymbolTable):
        result = Variable()
        result.id = self.id
        result_val: Variable = self.value.execute(symbol_table)

        if result_val is None:
            print('A value was expected')
            return None

        result.value = result_val.value
        result.symbol_type = SymbolType().VARIABLE
        result.variable_type = result_val.variable_type

        return result

    def dot(self):
        pass
        
    def c3d(self,scope):
        pass