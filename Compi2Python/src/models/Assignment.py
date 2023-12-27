from .Instruction import Instruction
from .symbolTable.SymbolTable import SymbolTable
from .Variable import Variable
from .SymbolType import SymbolType
import re

from ..error.xsql_error import xsql_error


class Assignment(Instruction):

    def __init__(self, line, column, id: str, value: Instruction):
        super().__init__(line, column)
        self.id = id
        self.value = value

    def execute(self, symbol_table: SymbolTable, errors):
        result = Variable()
        result.id = self.id
        result_val: Variable = self.value.execute(symbol_table, errors)

        if result_val is None:
            print('A value was expected')
            errors.append(self.semantic_error('A value was expected'))
            return None

        result.value = result_val.value
        result.symbol_type = SymbolType().VARIABLE
        result.variable_type = result_val.variable_type

        return result


    def semantic_error(self, description):
        return xsql_error(description,'','Error Semantico',f'Linea {self.line} Columna {self.column}')


    def dot(self,nodo_padre, graficador):
        current_node = graficador.agregarNode("=")
        graficador.agregarRelacion(nodo_padre, current_node)
        id_node = graficador.agregarNode(self.id)
        graficador.agregarRelacion(current_node, id_node)
        if self.value is not None:
            self.value.dot(current_node, graficador)
        
    def c3d(self,scope):
        pass