from .Instruction import Instruction
from .Variable import Variable
from .symbolTable.SymbolTable import SymbolTable
from .symbolTable.ScopeType import ScopeType


class WhileStatement(Instruction):

    def __init__(self, line, column, condition: Instruction, block: [Instruction]):
        super().__init__(line, column)
        self.condition = condition
        self.block = block

    def execute(self, symbol_table: SymbolTable):
        result: Variable = self.condition.execute(symbol_table)

        if result is None:
            print("The condition couldn't be executed")
            return None

        if result.variable_type.type != 'int':
            print('int type was expected')
            return None

        while result.value > 0:

            symbol_table = SymbolTable(ScopeType().IF, symbol_table)
            for instruction in self.block:
                instruction.execute(symbol_table)

            symbol_table = symbol_table.parent

            result = self.condition.execute(symbol_table)

            if result is None:
                print("The condition couldn't be executed")
                return None

            if result.variable_type.type != 'int':
                print('int type was expected')
                return None

    def dot(self):
        pass
        
    def c3d(self,scope):
        pass