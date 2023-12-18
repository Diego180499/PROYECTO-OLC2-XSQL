from .Instruction import Instruction
from .symbolTable import SymbolTable
from .Variable import Variable
from .VariableType import VariableType
from .SymbolType import SymbolType


class ParameterStatement(Instruction):

    def __init__(self, line, column, id, type: VariableType):
        super().__init__(line, column)
        self.id = id
        self.type = type

    def execute(self, symbol_table: SymbolTable):

        result = Variable()
        result.variable_type = self.type
        result.symbol_type = SymbolType().VARIABLE
        result.id = id
        return result
