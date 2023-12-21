from .Instruction import Instruction
from .symbolTable.SymbolTable import SymbolTable


class Node(Instruction):
    def __init__(self, line, column, left, right):
        super().__init__(line, column)
        self.left = left
        self.right = right
    
    def execute(self, symbol_table: SymbolTable, errors):
        pass
    
    def __str__(self):
        #Value isn't declared
        return f"Node: {self.value}"

    def dot(self,nodo_padre, graficador):
        pass
        
    def c3d(self,scope):
        pass