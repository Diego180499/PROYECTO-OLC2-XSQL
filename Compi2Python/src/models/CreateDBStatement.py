from .Instruction import Instruction
from .symbolTable.SymbolTable import SymbolTable
from src.repository.data_base.data_base_repository import DataBaseRepository
from ..error.xsql_error import xsql_error


class CreateDBStatement(Instruction):

    def __init__(self, line, column, db_name):
        super().__init__(line, column)
        self.db_name = db_name

    def execute(self, symbol_table: SymbolTable, errors):

        db_exists = DataBaseRepository().existe_bd(self.db_name)

        if db_exists:
            errors.append(self.semantic_error(f"The database: {self.db_name} already exists."))
            return None

        DataBaseRepository().crear_bd(self.db_name)

    def semantic_error(self, description):
        return xsql_error(description, '', 'Error Semantico', f'Linea {self.line} Columna {self.column}')


    def dot(self, nodo_padre, graficador):
        current_node = graficador.agregarNode("create_db")
        graficador.agregarRelacion(nodo_padre, current_node)
        name_node = graficador.agregarNode(f"name = {self.db_name}")
        graficador.agregarRelacion(current_node, name_node)

    def c3d(self, scope,generador):
        pass