from .Instruction import Instruction
from ..symbolTable.SymbolTable import SymbolTable
from .Variable import Variable


class IfStatement(Instruction):

    def __init__(self, line, column, condition, true_block: [Instruction], false_block: [Instruction]):
        super().__init__(line, column)
        self.condition = condition
        self.true_block = true_block
        self.false_block = false_block

    def execute(self, symbol_table: SymbolTable):
        result: Variable = self.condition.execute(symbol_table)

        if result is None:
            print("The condition didn't return anything")
            return None

        if result.variable_type.type != 'int':
            print("Only can use int type into conditions")
            return None

        if result.value > 0:
            for instruction in self.true_block:
                true_result = instruction.execute(symbol_table)
                if true_result is not None:
                    return true_result

        else:
            for instruction in self.false_block:
                false_result = instruction.execute(symbol_table)
                if false_result is not None:
                    return false_result

    def __str__(self):
        return f"""{{"IfStatement": {self.condition}, {self.true_block}, {self.false_block} }}"""
