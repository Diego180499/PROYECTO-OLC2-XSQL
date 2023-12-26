from .Instruction import Instruction
from .symbolTable.SymbolTable import SymbolTable
from .Variable import Variable
from ..repository.records.record_repository import RecordRepository
from ..FILES.manager_db.db_file_manager import get_table_field_by_name, obtener_campos_tabla
from ..FILES.Campo import Campo

class InsertStatement(Instruction):

    def __init__(self, line, column, table_name: str, column_names: [str], values: [Instruction]):
        super().__init__(line, column)
        self.column_names: [str] = column_names
        self.table_name: str = table_name
        self.values: [Instruction] = values

    def execute(self, symbol_table: SymbolTable, errors):
        db: Variable = symbol_table.find_database()

        if db is None:
            print("There's no database selected.")
            return None

        if len(self.column_names) != len(self.values):
            print(f"You declare {len(self.column_names)} columns and assign {len(self.values)} values.")
            return None

        table_fields = obtener_campos_tabla(db.value, self.table_name)

        for column_name in self.column_names:
            declared = any((f == column_name) for f in table_fields)

            if not declared:
                print(f"Field: {column_name} not found in table: {self.table_name}")
                return None

        for table_field in table_fields:
            field: Campo = get_table_field_by_name(db.value, self.table_name, table_field)
            field_declared = any((c == table_field) for c in self.column_names)

            if int(field.nulo) == 0 and not field_declared:
                print(f"The field: {table_field} cannot be null.")
                return None

    def dot(self, nodo_padre, graficador):
        current_node = graficador.agregarNode("insert")
        graficador.agregarRelacion(nodo_padre, current_node)
        table_node = graficador.agregarNode(self.table_name)
        graficador.agregarRelacion(current_node, table_node)
        if self.column_names is not None or len(self.column_names) > 0:
            columns_node = graficador.agregarNode("columns")
            graficador.agregarRelacion(current_node, columns_node)
            for column_name in self.column_names:
                column_node = graficador.agregarNode(column_name)
                graficador.agregarRelacion(columns_node, column_node)
        if self.values is not None or len(self.values) > 0:
            values_node = graficador.agregarNode("values")
            graficador.agregarRelacion(current_node, values_node)
            for value in self.values:
                value.dot(values_node, graficador)


    def c3d(self, scope):
        pass