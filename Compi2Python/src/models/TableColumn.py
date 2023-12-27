from .Instruction import Instruction
from .Variable import Variable
from .VariableType import VariableType
from .symbolTable.SymbolTable import SymbolTable


class TableColumn(Instruction):

    def __init__(self, line, column, table_name, column_name, value: Instruction):
        super().__init__(line, column)
        self.table_name = table_name
        self.column_name = column_name
        self.value: Instruction = value

    def execute(self, symbol_table: SymbolTable, errors):
        value_result: Variable = self.value.execute(symbol_table, errors)

        if value_result is None:
            print("The value doesn't return anything")
            return None

        result = Variable()
        result.id = self.column_name
        result.variable_type = value_result.variable_type
        result.value = value_result.value
        return result

    def dot(self, nodo_padre, graficador):
        pass

    def c3d(self, scope):
        pass