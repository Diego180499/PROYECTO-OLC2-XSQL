import copy

from .Instruction import Instruction
from .ValueType import ValueType
from .Variable import Variable
from .VariableType import VariableType
from .symbolTable.SymbolTable import SymbolTable


class Value(Instruction):

    def __init__(self, line, column, value, value_type: ValueType):
        super().__init__(line, column)
        self.value = value
        self.value_type = value_type

    def execute(self, symbol_table: SymbolTable):
        variable = Variable()

        if self.value_type == ValueType().INTEGER_VALUE:
            variable.value = int(self.value)
            variable.variable_type = VariableType('int', 32)
            return variable

        elif self.value_type == ValueType().DECIMAL_VALUE:
            variable.value = float(self.value)
            variable.variable_type = VariableType('decimal', 32)
            return variable

        elif self.value_type == ValueType().STRING:
            variable.value = str(self.value)
            variable.variable_type = VariableType('nchar', len(self.value))
            return variable

        elif self.value_type == ValueType().COLUMN:
            var_in_table = symbol_table.find_column_by_id(self.value)
            if var_in_table is None:
                print("Column doesn't found")
                return None

            variable = copy.deepcopy(var_in_table)
            return variable

        elif self.value_type == ValueType().ID:
            var_in_table = symbol_table.find_var_by_id(self.value)
            if var_in_table is None:
                print("Variable doesn't found")
                return None

            variable = copy.deepcopy(var_in_table)
            return variable

    def dot(self):
        pass
        
    def c3d(self,scope):
        pass