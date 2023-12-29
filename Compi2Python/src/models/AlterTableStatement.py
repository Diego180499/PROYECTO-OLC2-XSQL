from .Instruction import Instruction
from .symbolTable.SymbolTable import SymbolTable
from .VariableType import VariableType
from .Variable import Variable
from ..FILES.manager_db.db_file_manager import get_table_field_by_name, agregar_campo_tabla, eliminar_campo
from ..error.xsql_error import xsql_error
from ..repository.table.table_repository import TableRepository
from ..FILES.Campo import Campo


class AlterTableStatement(Instruction):

    def __init__(self, line, column, table_name: str, property_name: str, variable_type: VariableType, alter_type: str):
        super().__init__(line, column)
        self.table_name: str = table_name
        self.property_name: str = property_name
        self.variable_type: VariableType = variable_type
        self.alter_type: str = alter_type

    def execute(self, symbol_table: SymbolTable, errors):
        db: Variable = symbol_table.find_database()

        if db is None:
            print("There's no database selected")
            errors.append(self.semantic_error("There's no database selected"))
            return None

        table_exists = TableRepository().existe_tabla_en_bd(db.value, self.table_name)

        if not table_exists:
            print(f"The table: {self.table_name} doesn't exist.")
            errors.append(self.semantic_error(f"The table: {self.table_name} doesn't exist."))
            return None

        if self.alter_type == 'add':
            self.add_column(db, symbol_table, errors)
        else:
            self.drop_column(db, symbol_table, errors)

    def add_column(self, db: Variable, symbol_table: SymbolTable, errors):
        table_field = get_table_field_by_name(db.value, self.table_name, self.property_name)

        if table_field is not None:
            print(f"The field: {self.property_name} already exists.")
            errors.append(self.semantic_error(f"The field: {self.property_name} already exists."))
            return None

        if isinstance(self.variable_type.length, Instruction):
            length_result: Variable = self.variable_type.length.execute(symbol_table, errors)

            if length_result is None:
                print("A value was expected")
                errors.append(self.semantic_error("A value was expected"))
                return None

            if length_result.variable_type.type != 'int':
                print("Int value was expected")
                errors.append(self.semantic_error("Int value was expected"))
                return None

        field: Campo = Campo(self.property_name, self.variable_type.type, 0, 0, "-", "-")
        agregar_campo_tabla(db.value, self.table_name, field)

    def drop_column(self, db: Variable, symbol_table: SymbolTable, errors):
        table_field = get_table_field_by_name(db.value, self.table_name, self.property_name)

        if table_field is None:
            print(f"The field: {self.property_name} doesn't exist.")
            errors.append(self.semantic_error("Int value was expected"))
            return None

        eliminar_campo(db.value, self.table_name, self.property_name)


    def semantic_error(self, description):
        return xsql_error(description, '', 'Error Semantico', f'Linea {self.line} Columna {self.column}')

    def dot(self, nodo_padre, graficador):
        current_node = graficador.agregarNode('alter_table')
        graficador.agregarRelacion(nodo_padre, current_node)
        table_node = graficador.agregarNode(self.table_name)
        graficador.agregarRelacion(current_node, table_node)
        property_node = graficador.agregarNode(self.property_name)
        graficador.agregarRelacion(current_node, property_node)
        type_node = graficador.agregarNode(self.variable_type.type)
        graficador.agregarRelacion(current_node, type_node)
        alter_node = graficador.agregarNode(self.alter_type)
        graficador.agregarRelacion(current_node, alter_node)

    def c3d(self, scope,graficador):
        pass