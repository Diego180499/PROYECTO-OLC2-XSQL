from .Instruction import Instruction
from .symbolTable.SymbolTable import SymbolTable
from ..error.xsql_error import xsql_error


class ElseStatement(Instruction):

    def __init__(self, line, column, instruction: Instruction):
        super().__init__(line, column)
        self.instruction = instruction

    def execute(self, symbol_table: SymbolTable, errors):
        result = self.instruction.execute(symbol_table, errors)

        if result is None:
            print('A value was expected')
            errors.append(self.semantic_error('A value was expected'))

        return result

    def semantic_error(self, description):
        return xsql_error(description, '', 'Error Semantico', f'Linea {self.line} Columna {self.column}')

    def dot(self,nodo_padre, graficador):
        current_node = graficador.agregarNode("else")
        graficador.agregarRelacion(nodo_padre, current_node)
        if self.instruction is not None:
            self.instruction.dot(current_node, graficador)
        
    def c3d(self,scope,generador):
        pass