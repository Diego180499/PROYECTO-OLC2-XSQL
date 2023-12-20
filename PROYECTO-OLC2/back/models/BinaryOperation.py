from .Instruction import Instruction
from .symbolTable.SymbolTable import SymbolTable
from .OperationType import OperationType
from .Variable import Variable
from .VariableType import VariableType


class BinaryOperation(Instruction):

    def __init__(self, line, column, left_operation: Instruction, right_operation: Instruction, operator):
        super().__init__(line, column)
        self.left_operation = left_operation
        self.right_operation = right_operation
        self.operator = operator

    def execute(self, symbol_table: SymbolTable):
        left: Variable = self.left_operation.execute(symbol_table)
        right: Variable = self.right_operation.execute(symbol_table)

        if left is None or right is None:
            print("The operation couldn't be executed")
            return None

        if self.operator == OperationType().PLUS:

            result = Variable()

            if left.variable_type.type == 'nchar' or left.variable_type.type == 'nvarchar' or right.variable_type.type == 'nchar' \
                or right.variable_type.type == 'nvarchar':
                result.value = str(left.value) + str(right.value)
                result.variable_type = VariableType('nchar', len(result.value))
                return result


            if left.variable_type.type != 'int' and left.variable_type.type != 'decimal' or right.variable_type.type != 'int' \
                    and right.variable_type.type != 'decimal':
                print("Plus operation only can be executed by int and decimal values")
                return None


            if left.variable_type.type == 'decimal' or right.variable_type.type == 'decimal':
                result.variable_type = VariableType('decimal', 32)
            else:
                result.variable_type = VariableType('int', 32)

            result.value = left.value + right.value

            return result

        elif self.operator == OperationType().MINUS:

            if (left.variable_type.type != 'int' and left.variable_type.type != 'decimal' or
                    right.variable_type.type != 'int' and right.variable_type.type != 'decimal'):
                print("Minus operation only can be executed by int and decimal values")
                return None

            result = Variable()

            if left.variable_type.type == 'decimal' or right.variable_type.type == 'decimal':
                result.variable_type = VariableType('decimal', 32)
            else:
                result.variable_type = VariableType('int', 32)

            result.value = left.value - right.value

            return result

        elif self.operator == OperationType().TIMES:

            if (left.variable_type.type != 'int' and left.variable_type.type != 'decimal' or
                    right.variable_type.type != 'int' and right.variable_type.type != 'decimal'):
                print("Times operation only can be executed by int and decimal values")
                return None

            result = Variable()

            result.variable_type = VariableType('decimal', 32)

            result.value = left.value * right.value

            return result
        elif self.operator == OperationType().DIVIDE:

            if left.variable_type.type != 'int' and left.variable_type.type != 'decimal' or right.variable_type.type != 'int' \
                    and right.variable_type.type != 'decimal':
                print("Divide operation only can be executed by int and decimal values")
                return None

            result = Variable()

            result.variable_type = VariableType('decimal', 32)

            result.value = left.value / right.value

            return result

        elif self.operator == OperationType().EQUALS:

            result = Variable()
            result.variable_type = VariableType('int', 32)
            result.value = int(left.value == right.value)
            return result

        elif self.operator == OperationType().NOT_EQ:

            result = Variable()
            result.variable_type = VariableType('int', 32)
            result.value = int(left.value != right.value)
            return result

        elif self.operator == OperationType().LESS_THAN:

            result = Variable()
            result.variable_type = VariableType('int', 32)
            result.value = int(left.value < right.value)
            return result

        elif self.operator == OperationType().GREATER_THAN:

            result = Variable()
            result.variable_type = VariableType('int', 32)
            result.value = int(left.value > right.value)
            return result

        elif self.operator == OperationType().LESS_EQ:

            result = Variable()
            result.variable_type = VariableType('int', 32)
            result.value = int(left.value <= right.value)
            return result
        elif self.operator == OperationType().GREATER_EQ:

            result = Variable()
            result.variable_type = VariableType('int', 32)
            result.value = int(left.value >= right.value)
            return result
        elif self.operator == OperationType().AND:

            result = Variable()
            result.variable_type = VariableType('int', 32)
            result.value = 1 if int(left.value and right.value) > 0 else 0
            print('and result:', result.value)

            return result

        elif self.operator == OperationType().OR:

            result = Variable()
            result.variable_type = VariableType('int', 32)
            result.value = 1 if int(left.value or right.value) > 0 else 0
            print('or result:', result.value)
            return result

    def dot(self):
        pass
        
    def c3d(self,scope):
        pass