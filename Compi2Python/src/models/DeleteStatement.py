from .Instruction import Instruction
from .Variable import Variable
from .VariableType import VariableType
from .SymbolType import SymbolType
from .symbolTable.SymbolTable import SymbolTable
from .symbolTable.ScopeType import ScopeType
from ..repository.table.table_repository import TableRepository
from ..repository.records.record_repository import RecordRepository
from ..FILES.Registro import Registro
from ..FILES.Campo import Campo
from ..FILES.manager_db.record_file_manager import existe_archivo_registros
from ..FILES.manager_db.db_file_manager import obtener_nombres_campos_tabla, get_table_field_by_name

class DeleteStatement(Instruction):

    def __init__(self, line, column, table_name: str, where_instruction: Instruction):
        super().__init__(line, column)
        self.table_name = table_name
        self.where_instruction = where_instruction

    def execute(self, symbol_table: SymbolTable, errors):
        db: Variable = symbol_table.find_database()

        if db is None:
            print("There's no database selected.")
            return None

        table_exists = TableRepository().existe_tabla_en_bd(db.value, self.table_name)

        if not table_exists:
            print(f"Table: {self.table_name} not found in database: {db.value}.")
            return None

        if not existe_archivo_registros(db.value, self.table_name):
            return None

        symbol_table = SymbolTable(ScopeType().DELETE, symbol_table)

        record_repository = RecordRepository();
        records: [Registro] = record_repository.obtener_registros_de_tabla(db.value, self.table_name)
        field_names = obtener_nombres_campos_tabla(db.value, self.table_name)

        for field_name in field_names:
            field: Campo = get_table_field_by_name(db.value, self.table_name, field_name)

            result = Variable()
            result.id = field.nombre
            result.symbol_type = SymbolType().COLUMN
            result.variable_type = VariableType(field.tipoDato, 32)
            symbol_table.add_variable(result)

        records_to_delete: [Registro] = []

        for record in records:
            for i in range(len(record.campos)):
                column_in_table: Variable = symbol_table.find_column_by_id(record.campos[i])
                if column_in_table is not None:
                    if column_in_table.variable_type.type == 'int' or column_in_table.variable_type.type == 'decimal':
                        column_in_table.value = int(record.valores[i])
                        continue
                    column_in_table.value = record.valores[i]

            where_result: Variable = self.where_instruction.execute(symbol_table, errors)

            if where_result is None:
                print("Where doesn't return anything.")
                symbol_table = symbol_table.parent
                return None

            if where_result.variable_type.type != 'int':
                print("Where statement only allows int values.")
                symbol_table = symbol_table.parent
                return None

            if where_result.value < 1:
                continue

            records_to_delete.append(record)
        record_repository.eliminar_registro(db.value, self.table_name, records_to_delete)
        print("Records deleted :D")
        symbol_table = symbol_table.parent

    def dot(self, nodo_padre, graficador):
        pass

    def c3d(self, scope,generador):
        pass