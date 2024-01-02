from .Instruction import Instruction
from .Retorno import Retorno
from .symbolTable.SymbolTable import SymbolTable
from .OperationType import OperationType
from .Variable import Variable
from .VariableType import VariableType
from ..error.xsql_error import xsql_error


class BinaryOperation(Instruction):

    def __init__(self, line, column, left_operation: Instruction, right_operation: Instruction, operator):
        super().__init__(line, column)
        self.left_operation = left_operation
        self.right_operation = right_operation
        self.operator = operator

    def execute(self, symbol_table: SymbolTable, errors):
        left: Variable = self.left_operation.execute(symbol_table, errors)
        right: Variable = self.right_operation.execute(symbol_table, errors)

        if left is None or right is None:
            print("The operation couldn't be executed")
            errors.append(self.semantic_error("The operation couldn't be executed"))
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
                errors.append(self.semantic_error("Plus operation only can be executed by int and decimal values"))
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
                errors.append(self.semantic_error("Minus operation only can be executed by int and decimal values"))
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
                errors.append(self.semantic_error("Times operation only can be executed by int and decimal values"))
                return None

            result = Variable()

            result.variable_type = VariableType('decimal', 32)

            result.value = left.value * right.value

            return result
        elif self.operator == OperationType().DIVIDE:

            if left.variable_type.type != 'int' and left.variable_type.type != 'decimal' or right.variable_type.type != 'int' \
                    and right.variable_type.type != 'decimal':
                print("Divide operation only can be executed by int and decimal values")
                errors.append(self.semantic_error("Divide operation only can be executed by int and decimal values"))
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
            return result

        elif self.operator == OperationType().OR:

            result = Variable()
            result.variable_type = VariableType('int', 32)
            result.value = 1 if int(left.value or right.value) > 0 else 0
            return result

    def semantic_error(self, description):
        return xsql_error(description, '', 'Error Semantico', f'Linea {self.line} Columna {self.column}')

    def dot(self, nodo_padre, graficador):
        current_node = graficador.agregarNode(self.operator)
        graficador.agregarRelacion(nodo_padre, current_node)
        if self.left_operation is not None:
            self.left_operation.dot(current_node, graficador)
        if self.right_operation is not None:
            self.right_operation.dot(current_node, graficador)

    def c3d(self, symbol_table, generador):
        left = self.left_operation.c3d(symbol_table, generador)
        right = self.right_operation.c3d(symbol_table, generador)

        if left is None or right is None:
            print("The operation couldn't be executed")
            return None

        if left.type == 'ID':
            left = symbol_table.find_var_by_id(left.get_value())
            left = Retorno(f't{left.pos}', 'ID', True, None)
        if right.type == 'ID':
            right = symbol_table.find_var_by_id(right.get_value())
            right = Retorno(f't{right.pos}', 'ID', True, None)

        if self.operator == OperationType().PLUS:
            temp = generador.add_temp()
            generador.add_exp(temp, left.get_value(), right.get_value(), OperationType().PLUS)
            return Retorno(temp, VariableType('decimal', 32), True, None)
        elif self.operator == OperationType().MINUS:
            temp = generador.add_temp()
            generador.add_exp(temp, left.get_value(), right.get_value(), OperationType().MINUS)
            return Retorno(temp, VariableType('decimal', 32), True, None)
        elif self.operator == OperationType().TIMES:
            temp = generador.add_temp()
            generador.add_exp(temp, left.get_value(), right.get_value(), OperationType().TIMES)
            return Retorno(temp, VariableType('decimal', 32), True, None)
        elif self.operator == OperationType().DIVIDE:
            temp = generador.add_temp()
            generador.add_exp(temp, left.get_value(), right.get_value(), OperationType().DIVIDE)
            return Retorno(temp, VariableType('decimal', 32), True, None)
        elif self.operator == OperationType().EQUALS:
            temp = generador.add_temp()
            generador.add_exp(temp, left.get_value(), right.get_value(), OperationType().EQUALS)
            return Retorno(temp, VariableType('int', 32), True, None)
        elif self.operator == OperationType().NOT_EQ:
            temp = generador.add_temp()
            generador.add_exp(temp, left.get_value(), right.get_value(), OperationType().NOT_EQ)
            return Retorno(temp, VariableType('int', 32), True, None)
        elif self.operator == OperationType().LESS_THAN:
            temp = generador.add_temp()
            generador.add_exp(temp, left.get_value(), right.get_value(), OperationType().LESS_THAN)
            return Retorno(temp, VariableType('int', 32), True, None)
        elif self.operator == OperationType().GREATER_THAN:
            temp = generador.add_temp()
            generador.add_exp(temp, left.get_value(), right.get_value(), OperationType().GREATER_THAN)
            return Retorno(temp, VariableType('int', 32), True, None)
        elif self.operator == OperationType().LESS_EQ:
            temp = generador.add_temp()
            generador.add_exp(temp, left.get_value(), right.get_value(), OperationType().LESS_EQ)
            return Retorno(temp, VariableType('int', 32), True, None)
        elif self.operator == OperationType().GREATER_EQ:
            temp = generador.add_temp()
            generador.add_exp(temp, left.get_value(), right.get_value(), OperationType().GREATER_EQ)
            return Retorno(temp, VariableType('int', 32), True, None)
        elif self.operator == OperationType().AND:
            temp = generador.add_temp()
            generador.add_exp(temp, left.get_value(), right.get_value(), OperationType().AND)
            return Retorno(temp, VariableType('int', 32), True, None)
        elif self.operator == OperationType().OR:
            temp = generador.add_temp()
            generador.add_exp(temp, left.get_value(), right.get_value(), OperationType().OR)
            return Retorno(temp, VariableType('int', 32), True, None)
