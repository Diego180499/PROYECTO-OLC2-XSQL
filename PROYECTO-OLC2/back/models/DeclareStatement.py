from .Instruction import Instruction
from symbolTable import SymbolTable
from .Variable import Variable
from .VariableType import VariableType
from .SymbolType import SymbolType


class DeclareStatement(Instruction):

    def __init__(self, line, column, id: str, type: VariableType):
        super().__init__(line, column)
        self.type = type
        self.id = id

    def execute(self, symbol_table: SymbolTable):
        var_in_table = symbol_table.find_var_by_id(self.id)
        if var_in_table is not None:
            print(f'The variable: {self.id} already exists')
            return None

        result = Variable()
        result.variable_type = self.type
        result.symbol_type = SymbolType().VARIABLE
        result.id = self.id

        if self.type.type == 'int' or self.type.type == 'decimal':
            result.value = 0
        elif self.type.type == 'nvarchar' or self.type.type == 'nchar':
            result.value = ''

        symbol_table.add_variable(result)
