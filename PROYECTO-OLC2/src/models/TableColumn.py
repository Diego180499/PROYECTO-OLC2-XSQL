from .Instruction import Instruction
from .Variable import Variable
from .VariableType import VariableType
from .CallFunctionStatement import CallFunctionStatement
from .symbolTable.SymbolTable import SymbolTable
from .SymbolType import SymbolType


class TableColumn(Instruction):

    def __init__(self, line, column, table_name, column_name, value: Instruction):
        super().__init__(line, column)
        self.table_name = table_name
        self.column_name = column_name
        self.value: Instruction = value

    def execute(self, symbol_table: SymbolTable, errors):

        if self.column_name == "*":
            result = Variable()
            result.id = "all"
            return result

        value_result: Variable = self.value.execute(symbol_table, errors)

        if value_result is None:
            print("The value doesn't return anything")
            return None

        if isinstance(self.value, CallFunctionStatement) and value_result.variable_type.type == 'int':
            column_in_table: Variable = symbol_table.find_column_by_id(self.column_name)

            if column_in_table is None:
                result = Variable()
                result.id = self.column_name
                result.symbol_type = SymbolType().COLUMN
                result.value = value_result.value
                result.variable_type = value_result.variable_type
                symbol_table.add_variable(result)
                return result

            column_in_table.value += value_result.value
            return column_in_table

        result = Variable()
        result.id = self.column_name
        result.variable_type = value_result.variable_type
        result.value = value_result.value
        return result

    def dot(self, nodo_padre, graficador):
        pass

    def c3d(self, scope):
        pass