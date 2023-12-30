from .Instruction import Instruction
from .Retorno import Retorno
from .VariableType import VariableType
from .symbolTable.SymbolTable import SymbolTable
from .Variable import Variable
from .OperationType import OperationType
from .SymbolType import SymbolType
from ..error.xsql_error import xsql_error


class UnaryOperation(Instruction):

    def __init__(self, line, column, left_operation: Instruction, operator):
        super().__init__(line,column)
        self.left_operation = left_operation
        self.operator = operator

    def execute(self, symbol_table: SymbolTable, errors):
        left: Variable = self.left_operation.execute(symbol_table, errors)

        if left is None:
            print("A value was expected")
            errors.append(self.semantic_error("A value was expected"))
            return None

        if self.operator == OperationType().MINUS:

            if left.variable_type.type != 'int' and left.variable_type.type != 'decimal':
                print("Minus operator is only allowed for int and decimal data type.")
                errors.append(self.semantic_error("Minus operator is only allowed for int and decimal data type."))
                return None

            result = Variable()
            result.variable_type = left.variable_type
            result.symbol_type = SymbolType().VARIABLE
            result.value = left.value * -1

            return result

        elif self.operator == OperationType().NOT:
            if left.variable_type.type != 'int':
                print("Not operator is only allowed for int data type.")
                errors.append(self.semantic_error("Not operator is only allowed for int data type."))
                return None

            result = Variable()
            result.variable_type = left.variable_type
            result.symbol_type = SymbolType().VARIABLE
            result.value = int(not left.value)
            return result

    def semantic_error(self, description):
        return xsql_error(description, '', 'Error Semantico', f'Linea {self.line} Columna {self.column}')

    def dot(self,nodo_padre, graficador):
        current_node = graficador.agregarNode(self.operator)
        graficador.agregarRelacion(nodo_padre, current_node)
        if self.left_operation is not None:
            self.left_operation.dot(current_node, graficador)
        
    def c3d(self,symbol_table,generador):
        left: Retorno = self.left_operation.c3d(symbol_table,generador)
        if left is None:
            print("A value was expected")
            return None
        if self.operator == OperationType().MINUS:
            temp = generador.add_temp()
            generador.add_exp(temp, left.get_value(), "-1", OperationType().TIMES)
            return Retorno(temp, VariableType('decimal', 32), True, None)
        elif self.operator == OperationType().NOT:
            temp = generador.add_temp()
            generador.add_exp(temp, "", left.get_value(), OperationType().NOT)
            return Retorno(temp, VariableType('int', 32), True, None)