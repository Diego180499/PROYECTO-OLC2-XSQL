from .Instruction import Instruction
from .symbolTable.SymbolTable import SymbolTable
from .symbolTable.ScopeType import ScopeType


class OrdenEjecucion(Instruction):
    def __init__(self, line, column, left, right):
        super().__init__(line, column)
        self.left = left
        self.right = right

    def execute(self, symbol_table: SymbolTable, errors):
        if self.left is not None:
            left_result = self.left.execute(symbol_table, errors)

            if left_result is not None:
                return left_result
        if self.right is not None:
            right_result = self.right.execute(symbol_table, errors)

            if right_result is not None:
                return right_result

    def __str__(self):
        return f'[{self.left} {self.right}]'

    def dot(self, nodo_padre, graficador):
        current_node = graficador.agregarNode('inst')
        if nodo_padre is not None:
            graficador.agregarRelacion(nodo_padre, current_node)
        if self.left is not None:
            nodo_left = self.left.dot(current_node, graficador)
        if self.right is not None:
            nodo_right = self.right.dot(current_node, graficador)

    def c3d(self, scope, generador):
        if self.left is not None:
            self.left.c3d(scope, generador)
        if self.right is not None:
            self.right.c3d(scope, generador)
