from .Instruction import Instruction
from .symbolTable.SymbolTable import SymbolTable
from .Variable import Variable
from .VariableType import VariableType
from .SymbolType import SymbolType
from ..error.xsql_error import xsql_error


class ParameterStatement(Instruction):

    def __init__(self, line, column, id, type: VariableType):
        super().__init__(line, column)
        self.id = id
        self.type = type

    def execute(self, symbol_table: SymbolTable, errors):

        result = Variable()

        result.symbol_type = SymbolType().VARIABLE
        result.id = self.id

        length = 0
        if isinstance(self.type.length, Instruction):
            length_result: Variable = self.type.length.execute(symbol_table, errors)

            if length_result is None:
                print("The operation doesn't return anything")
                errors.append(self.semantic_error("The operation doesn't return anything"))
                return None

            if length_result.variable_type.type != 'int':
                print("int type was expected")
                errors.append(self.semantic_error("int type was expected"))
                return None

            length = length_result.value

        result.variable_type = VariableType(self.type.type, length)

        return result

    def semantic_error(self, description):
        return xsql_error(description, '', 'Error Semantico', f'Linea {self.line} Columna {self.column}')

    def dot(self,nodo_padre, graficador):
        pass

    def c3d(self,scope,generador):
        pass