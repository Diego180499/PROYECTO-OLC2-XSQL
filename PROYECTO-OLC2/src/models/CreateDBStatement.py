from .Instruction import Instruction
from .symbolTable.SymbolTable import SymbolTable
from src.repository.data_base.data_base_repository import DataBaseRepository



class CreateDBStatement(Instruction):

    def __init__(self, line, column, db_name):
        super().__init__(line, column)
        self.db_name = db_name

    def execute(self, symbol_table: SymbolTable, errors):
        response = DataBaseRepository().crear_bd(self.db_name)
        print(response)

    def dot(self, nodo_padre, graficador):
        pass

    def c3d(self, scope):
        pass