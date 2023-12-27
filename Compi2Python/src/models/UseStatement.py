from .Instruction import Instruction
from .symbolTable.SymbolTable import SymbolTable
from src.repository.data_base.data_base_repository import DataBaseRepository
from .Variable import Variable
from .VariableType import VariableType
from .SymbolType import SymbolType
from ..error.xsql_error import xsql_error


class UseStatement(Instruction):

    def __init__(self, line, column, db_name: str):
        super().__init__(line, column)
        self.db_name = db_name

    def execute(self, symbol_table: SymbolTable, errors):
        db_exists = DataBaseRepository().existe_bd(self.db_name)

        if not db_exists:
            print(f"The database: {self.db_name} doesn't exist")
            errors.append(self.semantic_error(f"The database: {self.db_name} doesn't exist"))
            return None

        db_in_table: Variable = symbol_table.find_database()

        if db_in_table is not None:
            db_in_table.id = self.db_name
            db_in_table.value = self.db_name
            db_in_table.variable_type.length = len(self.db_name)
            return None

        result = Variable()
        result.variable_type = VariableType('nchar', len(self.db_name))
        result.value = self.db_name
        result.id = self.db_name
        result.symbol_type = SymbolType().DB_NAME
        symbol_table.add_variable(result)

    def semantic_error(self, description):
        return xsql_error(description, '', 'Error Semantico', f'Linea {self.line} Columna {self.column}')

    def dot(self, nodo_padre, graficador):
        curren_node = graficador.agregarNode('use')
        graficador.agregarRelacion(nodo_padre, curren_node)
        table = graficador.agregarNode(self.db_name)
        graficador.agregarRelacion(curren_node, table)

    def c3d(self, scope):
        pass