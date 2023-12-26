from .Instruction import Instruction
from .Variable import Variable
from .VariableType import VariableType
from .symbolTable.SymbolTable import SymbolTable


class SelectStatement(Instruction):

    def __init__(self, line, column, column_names: [str, str], table_name: str, where_instruction: Instruction):
        super().__init__(line, column)
        self.column_names: [str, str] = column_names
        self.table_name: str = table_name
        self.where_instruction: Instruction = where_instruction

    def execute(self, symbol_table: SymbolTable, errors):
        pass

    def dot(self, nodo_padre, graficador):
        pass

    def c3d(self, scope):
        pass