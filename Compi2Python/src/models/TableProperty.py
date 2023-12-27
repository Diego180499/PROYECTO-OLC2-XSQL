from .Instruction import Instruction
from .Variable import Variable
from .VariableType import VariableType
from .symbolTable.SymbolTable import SymbolTable
from .SymbolType import SymbolType
from ..FILES.Campo import Campo
from ..FILES.manager_db.db_file_manager import get_table_field_by_name
from ..error.xsql_error import xsql_error


class TableProperty(Instruction):

    def __init__(self, line, column, property_name: str, variable_type: VariableType,
                 is_null: bool, is_primary_key: bool, parent: str, parent_field: str):
        super().__init__(line, column)
        self.property_name = property_name
        self.variable_type = variable_type
        self.is_null = is_null
        self.is_primary_key = is_primary_key
        self.parent = parent
        self.parent_field = parent_field

    def execute(self, symbol_table: SymbolTable, errors):
        db: Variable = symbol_table.find_database()

        if db is None:
            print("There's no database selected")
            errors.append(self.semantic_error("There's no database selected"))
            return None

        property_in_table: Variable = symbol_table.find_column_by_id(self.property_name)

        if property_in_table is not None:
            print(f"The field: {self.property_name} has already been declared")
            errors.append(self.semantic_error(f"The field: {self.property_name} has already been declared"))
            return None

        if self.is_null and self.is_primary_key:
            print("A primary key couldn't be null")
            errors.append(self.semantic_error("A primary key couldn't be null"))

        if isinstance(self.variable_type.length, Instruction):
            length_result: Variable = self.variable_type.length.execute(symbol_table, errors)

            if length_result is None:
                print("The length couldn't return anything")
                errors.append(self.semantic_error("The length couldn't return anything"))
                return None

            if length_result.variable_type.type != 'int':
                print('Int value was expected')
                errors.append(self.semantic_error('Int value was expected'))
                return None

        if self.parent != '-' and self.parent_field != '-':
            foreign_field: Campo = get_table_field_by_name(db.value, self.parent, self.parent_field)

            if foreign_field is None:
                print(f"The field: {self.parent_field} in {self.parent} doesn't exist")
                errors.append(self.semantic_error(f"The field: {self.parent_field} in {self.parent} doesn't exist"))
                return None

            if foreign_field.tipoDato != self.variable_type.type:
                print(f"The field: {self.parent_field} has {foreign_field.tipoDato} as data type. You declared: "
                      f"{self.property_name} as {self.variable_type.type}")
                errors.append(self.semantic_error(f"The field: {self.parent_field} has {foreign_field.tipoDato} as data type. You declared: "
                      f"{self.property_name} as {self.variable_type.type}"))
                return None

        result = Variable()
        result.id = self.property_name
        result.symbol_type = SymbolType().COLUMN

        result.value = Campo(self.property_name, self.variable_type.type, int(self.is_null), int(self.is_primary_key),
                             self.parent, self.parent_field)
        symbol_table.add_variable(result)
        return result

    def semantic_error(self, description):
        return xsql_error(description, '', 'Error Semantico', f'Linea {self.line} Columna {self.column}')

    def dot(self, nodo_padre, graficador):
        current_node = graficador.agregarNode("property")
        graficador.agregarRelacion(nodo_padre, current_node)
        id_node = graficador.agregarNode(self.property_name)
        graficador.agregarRelacion(current_node, id_node)
        if self.variable_type is not None:
            type_node = graficador.agregarNode(self.variable_type.type)
            graficador.agregarRelacion(current_node, type_node)
            if self.variable_type.length is not None:
                length_node = graficador.agregarNode(str(self.variable_type.length))
                graficador.agregarRelacion(type_node, length_node)
        if self.is_null is not None:
            null_node = graficador.agregarNode(str(self.is_null))
            graficador.agregarRelacion(current_node, null_node)
        if self.is_primary_key is not None:
            primary_node = graficador.agregarNode(str(self.is_primary_key))
            graficador.agregarRelacion(current_node, primary_node)
        if self.parent is not None:
            parent_node = graficador.agregarNode(self.parent)
            graficador.agregarRelacion(current_node, parent_node)
        if self.parent_field is not None:
            parent_field_node = graficador.agregarNode(self.parent_field)
            graficador.agregarRelacion(current_node, parent_field_node)

    def c3d(self, scope):
        pass