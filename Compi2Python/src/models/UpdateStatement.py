from .Instruction import Instruction
from .Variable import Variable
from .VariableType import VariableType
from .SymbolType import SymbolType
from .symbolTable.SymbolTable import SymbolTable
from .symbolTable.ScopeType import ScopeType
from ..repository.table.table_repository import TableRepository
from ..repository.records.record_repository import RecordRepository
from ..FILES.Campo import Campo
from ..FILES.Registro import Registro
from ..FILES.manager_db.record_file_manager import existe_archivo_registros
from ..FILES.manager_db.db_file_manager import obtener_nombres_campos_tabla, get_table_field_by_name
from re import search


class UpdateStatement(Instruction):

    def __init__(self, line, column, table_name: str, assignment_instructions: [Instruction],
                 where_instruction: Instruction):
        super().__init__(line, column)
        self.table_name = table_name
        self.assignment_instructions: [Instruction] = assignment_instructions
        self.where_instruction: Instruction = where_instruction

    def execute(self, symbol_table: SymbolTable, errors):
        db: Variable = symbol_table.find_database()

        if db is None:
            print("There's no database selected.")
            return None

        table_repository = TableRepository();
        table_exist = table_repository.existe_tabla_en_bd(db.value, self.table_name)
        if not table_exist:
            print(f"Table: {self.table_name} not found in database: {db.value}.")
            return None

        if not existe_archivo_registros(db.value, self.table_name):
            return None

        table_fields = obtener_nombres_campos_tabla(db.value, self.table_name)

        symbol_table = SymbolTable(ScopeType().UPDATE, symbol_table)
        fields_to_update: [Variable] = []
        field_names = []
        field_values = []
        for assignment in self.assignment_instructions:
            assignment_result: Variable = assignment.execute(symbol_table, errors)

            if assignment_result is None:
                print("The assignment doesn't return anything")
                symbol_table = symbol_table.parent
                return None

            column_declared = any((f.id == assignment_result.id) for f in fields_to_update)
            if column_declared:
                print(f"Column: {assignment_result.id} already declared.")
                symbol_table = symbol_table.parent
                return None

            field: Campo = get_table_field_by_name(db.value, self.table_name, assignment_result.id)

            if field is None:
                print(f"Column: {assignment_result.id} not found in table: {self.table_name}")
                symbol_table = symbol_table.parent
                return None

            if int(field.llavePrim) == 1:
                print("You can't update a primary key value.")
                symbol_table = symbol_table.parent
                return None

            if field.tipoDato == 'nchar' or field.tipoDato == 'nvarchar':
                if assignment_result.variable_type.type != 'nchar' and assignment_result.variable_type.type != 'nvarchar':
                    print("nchar or nvarchar value was expected")
                    symbol_table = symbol_table.parent
                    return None
                fields_to_update.append(assignment_result)
                field_names.append(assignment_result.id)
                field_values.append(assignment_result.value)
                continue

            if field.tipoDato == 'date':
                if not search("\d{2}-\d{2}-\d{4}", assignment_result.value):
                    print('Date value was expected')
                    symbol_table = symbol_table.parent
                    return None
                fields_to_update.append(assignment_result)
                field_names.append(assignment_result.id)
                field_values.append(assignment_result.value)
                continue

            if field.tipoDato == 'datetime':
                if not search("\d{2}-\d{2}-\d{4} (\d{2}:\d{2}:\d{2}|\d{2}:\d{2})", assignment_result.value):
                    print('Datetime value was expected')
                    symbol_table = symbol_table.parent
                    return None
                fields_to_update.append(assignment_result)
                field_names.append(assignment_result.id)
                field_values.append(assignment_result.value)
                continue

            if field.tipoDato != assignment_result.variable_type.type:
                print(f"Field: {field.nombre} has {field.tipoDato} as datatype, "
                      f"you declared: {assignment_result.variable_type.type}.")
                symbol_table = symbol_table.parent
                return None

            fields_to_update.append(assignment_result)
            field_names.append(assignment_result.id)
            field_values.append(assignment_result.value)

        for table_field in table_fields:
            field: Campo = get_table_field_by_name(db.value, self.table_name, table_field)

            result = Variable()
            result.id = field.nombre
            result.symbol_type = SymbolType().COLUMN
            result.variable_type = VariableType(field.tipoDato, 32)
            symbol_table.add_variable(result)

        record_repository = RecordRepository()
        records: [Registro] = record_repository.obtener_registros_de_tabla(db.value, self.table_name)
        records_to_update: [Registro] = []

        for record in records:
            for i in range(len(record.campos)):
                column_in_table: Variable = symbol_table.find_column_by_id(record.campos[i])

                if column_in_table is not None:
                    if column_in_table.variable_type.type == 'int':
                        column_in_table.value = int(record.valores[i])
                        continue
                    if column_in_table.variable_type.type == 'decimal':
                        column_in_table.value = float(record.valores[i])
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

            records_to_update.append(record)

        record_repository.actualizar_registro(db.value, self.table_name, field_names, field_values, records_to_update)
        print("Records updated :D")
        symbol_table = symbol_table.parent

    def dot(self, nodo_padre, graficador):
        pass

    def c3d(self, scope, generador):
        pass