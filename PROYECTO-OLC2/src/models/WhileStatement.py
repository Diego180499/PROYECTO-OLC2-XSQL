from .Instruction import Instruction
from .Variable import Variable
from .symbolTable.SymbolTable import SymbolTable
from .symbolTable.ScopeType import ScopeType


class WhileStatement(Instruction):

    def __init__(self, line, column, condition: Instruction, block: Instruction):
        super().__init__(line, column)
        self.condition = condition
        self.block = block

    def execute(self, symbol_table: SymbolTable, errors):
        result: Variable = self.condition.execute(symbol_table, errors)

        if result is None:
            print("The condition couldn't be executed")
            return None

        if result.variable_type.type != 'int':
            print('int type was expected')
            return None

        while result.value > 0:

            symbol_table = SymbolTable(ScopeType().WHILE, symbol_table)
            return_result = self.block.execute(symbol_table, errors)

            if return_result is not None:
                symbol_table = symbol_table.parent
                return return_result

            symbol_table = symbol_table.parent

            result = self.condition.execute(symbol_table, errors)

            if result is None:
                print("The condition couldn't be executed")
                return None

            if result.variable_type.type != 'int':
                print('int type was expected')
                return None

    def dot(self,nodo_padre, graficador):
        pass
        
    def c3d(self,scope):
        pass