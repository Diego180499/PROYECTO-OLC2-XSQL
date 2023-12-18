from .Instruction import Instruction
from .symbolTable import SymbolTable
from .Variable import Variable
from .OperationType import OperationType
from .SymbolType import SymbolType


class UnaryOperation(Instruction):

    def __init__(self, line, column, left_operation: Instruction, operator):
        super().__init__(line,column)
        self.left_operation = left_operation
        self.operator = operator

    def execute(self, symbol_table: SymbolTable):
        left: Variable = self.left_operation.execute(symbol_table)

        if left is None:
            print("A value was expected")
            return None

        if self.operator == OperationType().MINUS:

            if left.variable_type.type != 'int' and left.variable_type.type != 'decimal':
                print("Minus operator is only allowed for int and decimal data type.")
                return None

            result = Variable()
            result.variable_type = left.variable_type
            result.symbol_type = SymbolType().VARIABLE
            result.value = left.value * -1

            return result

        elif self.operator == OperationType().NOT:
            if left.variable_type.type != 'int':
                print("Not operator is only allowed for int data type.")
                return None

            result = Variable()
            result.variable_type = left.variable_type
            result.symbol_type = SymbolType().VARIABLE
            result.value = int(not left.value)
            return result