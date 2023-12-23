from .Instruction import Instruction
from .symbolTable.SymbolTable import SymbolTable
from .Variable import Variable
from ..repository.table.table_repository import TableRepository


class DropTableStatement(Instruction):

    def __init__(self, line, column, table_name: str):
        super().__init__(line, column)
        self.table_name = table_name

    def execute(self, symbol_table: SymbolTable, errors):
        db: Variable = symbol_table.find_database()

        if db is None:
            print("There's no database selected")
            return None

        exists = TableRepository().existe_tabla_en_bd(db.value, self.table_name)

        if not exists:
            print(f"The table: {self.table_name} doesn't exist in the database: {db.value}.")
            return None



    def dot(self, nodo_padre, graficador):
        pass

    def c3d(self, scope):
        pass