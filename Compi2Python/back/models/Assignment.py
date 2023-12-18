from .Instruction import Instruction
from .Variable import Variable
from ..symbolTable.SymbolTable import SymbolTable


class Assignment(Instruction):

    def __init__(self, line, column, id: str, value: Instruction):
        super().__init__(line, column)
        self.id = id
        self.value = value

    def execute(self, symbol_table: SymbolTable):
        var_in_table: Variable = symbol_table.find_var_by_id(self.id)

        if var_in_table is None:
            print(f"The variable: {self.id} doesn't exists")
            return None

        result: Variable = self.value.execute(symbol_table)

        if result is None:
            print("Assignation couldn't be executed")
            return

        if var_in_table.variable_type.type != result.variable_type.type:
            print("Variable type doesn't match")
            return None

        if var_in_table.variable_type.type == 'nchar' or var_in_table.variable_type.type == 'nvarchar':
            if var_in_table.variable_type.length < result.variable_type.length:
                print("The length value is too long")
                return None

        var_in_table.value = result.value
        return var_in_table
