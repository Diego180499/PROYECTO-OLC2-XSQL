from .Instruction import Instruction
from .Variable import Variable
from .VariableType import VariableType
from .symbolTable.SymbolTable import SymbolTable
from datetime import datetime

from ..error.xsql_error import xsql_error


class CallFunctionStatement(Instruction):

    def __init__(self, line, column, function_name: str, args: [Instruction]):
        super().__init__(line, column)
        self.function_name = function_name
        self.args = args

    def execute(self, symbol_table: SymbolTable, errors):
        if self.function_name == 'suma':
            if len(self.args) != 1:
                print('an arg was expected')
                errors.append(self.semantic_error('an arg was expected'))
                return None

        elif self.function_name == 'concatena':
            if len(self.args) != 2:
                print('two args were expected')
                errors.append(self.semantic_error('two args were expected'))
                return None

            left: Variable = self.args[0].execute(symbol_table, errors)
            right: Variable = self.args[1].execute(symbol_table, errors)

            if left is None or right is None:
                print('something went wrong')
                errors.append(self.semantic_error('something went wrong'))
                return None

            if left.variable_type.type != 'nchar' and left.variable_type.type != 'nvarchar' or \
                    right.variable_type.type != 'nchar' and right.variable_type.type != 'nvarchar':
                print('concatena function only allows nchar o nvarchar data types.')
                errors.append(self.semantic_error('concatena function only allows nchar o nvarchar data types.'))
                return None

            result = Variable()
            result.value = left.value + right.value
            result.variable_type = VariableType('nvarchar', len(result.value))
            return result

        elif self.function_name == 'substraer':
            if len(self.args) != 3:
                print('three args were expected')
                errors.append(self.semantic_error('three args were expected'))
                return None

            text: Variable = self.args[0].execute(symbol_table, errors)
            init: Variable = self.args[1].execute(symbol_table, errors)
            end: Variable = self.args[2].execute(symbol_table, errors)

            if text is None or init is None or end is None:
                print('something went wrong')
                errors.append(self.semantic_error('something went wrong'))
                return None

            if text.variable_type.type != 'nchar' and text.variable_type.type != 'nvarchar':
                print('substraer function only allows nchar or nvarchar data types')
                errors.append(self.semantic_error('substraer function only allows nchar or nvarchar data types'))
                return None

            if init.variable_type.type != 'int' or end.variable_type.type != 'int':
                print('int value was expected')
                errors.append(self.semantic_error('int value was expected'))
                return None

            if init.value < 1 or end.value < 1:
                print('positive value was expected')
                errors.append(self.semantic_error('positive value was expected'))
                return None

            if len(text.value) < end.value:
                print(f'Index out of range. {text.value} has: {len(text.value)} you want: {end.value}')
                errors.append(self.semantic_error(f'Index out of range. {text.value} has: {len(text.value)} you want: {end.value}'))

            result = Variable()
            result.variable_type = VariableType('nvarchar', end.value)
            result.value = text.value[init.value - 1: end.value]
            return result

        elif self.function_name == 'contar':
            # pendiente
            pass
        elif self.function_name == 'hoy':
            if len(self.args) > 0:
                print('no args were expected')
                errors.append(self.semantic_error('no args were expected'))
                return None
            result = Variable()
            result.variable_type = VariableType('datetime', 32)
            result.value = datetime.now().strftime('%d-%m-%Y %H:%M:%S')
            return result


    def semantic_error(self, description):
        return xsql_error(description,'','Error Semantico',f'Linea {self.line} Columna {self.column}')

    def dot(self,nodo_padre, graficador):
        concurrent_node = graficador.agregarNode('call_function')
        graficador.agregarRelacion(nodo_padre,concurrent_node)
        function_node = graficador.agregarNode(self.function_name)
        graficador.agregarRelacion(concurrent_node,function_node)
        if self.args is not None:
            args_node = graficador.agregarNode('args')
            for arg in self.args:
                arg.dot(args_node, graficador)

    def c3d(self, scope):
        pass
