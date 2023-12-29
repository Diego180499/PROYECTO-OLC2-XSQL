from .Instruction import Instruction
from .symbolTable.SymbolTable import SymbolTable


class EOF(Instruction):
    def __init__(self, line, column):
        super().__init__(line, column)
        self.line = line
        self.column = column

    def execute(self, symbol_table: SymbolTable, errors):
        pass

    def __str__(self):
        return f"EOF"

    def dot(self, nodo_padre, graficador):
        current_node = graficador.agregarNode("EOF")
        graficador.agregarRelacion(nodo_padre, current_node)

    def c3d(self, scope,generador):
        pass
