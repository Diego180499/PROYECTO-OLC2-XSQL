from .Instruction import Instruction
from .symbolTable.SymbolTable import SymbolTable
from .Variable import Variable


class ReturnStatement(Instruction):

    def __init__(self, line, column, instruction: Instruction):
        super().__init__(line, column)
        self.instruction = instruction

    def execute(self, symbol_table: SymbolTable):

        is_in_fun_scope = symbol_table.is_in_fun_scope()

        if not is_in_fun_scope:
            print(f"return statement isn't in function scope {self.line}, {self.column}")
            return None

        result: Variable = self.instruction.execute(symbol_table)

        if result is None:
            print('A value was expected')

        return result
    
    def dot(self,nodo_padre, graficador):
        pass
        
    def c3d(self,scope):
        pass