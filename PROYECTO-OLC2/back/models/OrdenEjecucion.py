from .Instruction import Instruction
from .symbolTable.SymbolTable import SymbolTable
from .symbolTable.ScopeType import ScopeType

class OrdenEjecucion(Instruction):
    def __init__(self, line, column, left, right):
        super().__init__(line, column)
        self.left = left
        self.right = right
    
    def execute(self, symbol_table: SymbolTable):
        if self.left is not None:
            self.left.execute(symbol_table)
        if self.right is not None:
            self.right.execute(symbol_table)
        
    def __str__(self):
        return f'[{self.left} {self.right}]'
    
    def dot(self,nodo_padre, graficador):
        current_node = graficador.agregarNode('inst')
        if nodo_padre is not None:
            graficador.agregarRelacion(nodo_padre, current_node)
        if self.left is not None:
            nodo_left = self.left.dot(current_node, graficador)
            if nodo_left is not None:
                graficador.agregarRelacion(current_node, nodo_left)
        if self.right is not None:
            nodo_right = self.right.dot(current_node, graficador)
            if nodo_right is not None:
                graficador.agregarRelacion(current_node, nodo_right)
        return current_node
    
    def c3d(self,scope):
        pass