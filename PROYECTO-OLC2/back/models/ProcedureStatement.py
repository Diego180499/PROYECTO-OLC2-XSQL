from .Instruction import Instruction
from .Variable import Variable
from .symbolTable import SymbolTable


class ProcedureStatement(Instruction):

    def __init__(self, line, column, id: str, parameters: [Instruction], instructions: [Instruction]):
        super().__init__(line, column)
        self.id = id
        self.parameters = parameters
        self.instructions = instructions

    def execute(self, symbol_table: SymbolTable):
        procedure_in_table = symbol_table.find_procedure_by_id(self.id)

        if procedure_in_table is not None:
            print('Procedure already exists')
            return None

