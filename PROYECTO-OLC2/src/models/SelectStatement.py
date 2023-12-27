from .Instruction import Instruction
from .Variable import Variable
from .VariableType import VariableType
from .symbolTable.SymbolTable import SymbolTable
from .symbolTable.ScopeType import ScopeType
from .SymbolType import SymbolType
from .Value import Value
from ..FILES.manager_db.db_file_manager import obtener_nombres_campos_tabla, get_table_field_by_name
from ..FILES.manager_db.record_file_manager import existe_archivo_registros
from ..FILES.Campo import Campo
from ..FILES.Registro import Registro
from ..repository.records.record_repository import RecordRepository
from ..repository.table.table_repository import TableRepository
from ..utilities.utilities import tabla_select_a_matriz

class SelectStatement(Instruction):

    def __init__(self, line, column, table_columns: [Instruction], table_name: str, where_instruction: Instruction):
        super().__init__(line, column)
        self.table_columns: [Instruction] = table_columns
        self.table_name: str = table_name
        self.where_instruction: Instruction = where_instruction

    def execute(self, symbol_table: SymbolTable, errors):

        db: Variable = symbol_table.find_database()

        if db is None:
            print("There's no database selected")
            return None

        exist = TableRepository().existe_tabla_en_bd(db.value, self.table_name)

        if not exist:
            print(f"The table: {self.table_name} doesn't exist in db: {db.value}.")
            return None

        symbol_table = SymbolTable(ScopeType().SELECT, symbol_table)
        table_fields = obtener_nombres_campos_tabla(db.value, self.table_name)
        table_result: [[str], [Registro]] = [[], []]

        for table_column in self.table_columns:
            if table_column.column_name == '*':

                for table_field in table_fields:
                    column_in_table: Variable = symbol_table.find_column_by_id(table_field)

                    if column_in_table is not None:
                        print(f"The column: {table_field} has already been declared.")
                        symbol_table = symbol_table.parent
                        return None

                    field: Campo = get_table_field_by_name(db.value, self.table_name, table_field)
                    field_result = Variable()
                    field_result.id = table_field
                    field_result.symbol_type = SymbolType().COLUMN
                    field_result.variable_type = VariableType(field.tipoDato, 32)
                    symbol_table.add_variable(field_result)
                    table_result[0].append(table_field)

                continue
            if table_column.table_name is not None and table_column.table_name != self.table_name:
                print(f"Table name: '{table_column.table_name}'.{table_column.column_name} doesn't match with: "
                      f"{self.table_name}.")
                symbol_table = symbol_table.parent
                return None

            if not isinstance(table_column.value, Value):
                table_result[0].append(table_column.column_name)
                continue

            field: Campo = get_table_field_by_name(db.value, self.table_name, table_column.column_name)

            if field is None:
                print(f"The field: {table_column.column_name} doesn't exist in table: {self.table_name}")
                symbol_table = symbol_table.parent
                return None

            column_in_table: Variable = symbol_table.find_column_by_id(table_column.column_name)

            if column_in_table is not None:
                print(f"The column: {table_column.column_name} has already been declared.")
                symbol_table = symbol_table.parent
                return None

            field_result = Variable()
            field_result.id = table_column.column_name
            field_result.symbol_type = SymbolType().COLUMN
            field_result.variable_type = VariableType(field.tipoDato, 32)
            symbol_table.add_variable(field_result)
            table_result[0].append(table_column.column_name)

        for table_field in table_fields:
            column_in_table: Variable = symbol_table.find_column_by_id(table_field)

            if column_in_table is None:
                field: Campo = get_table_field_by_name(db.value, self.table_name, table_field)
                field_result = Variable()
                field_result.id = table_field
                field_result.symbol_type = SymbolType().COLUMN
                field_result.variable_type = VariableType(field.tipoDato, 32)
                symbol_table.add_variable(field_result)

        exist = existe_archivo_registros(db.value, self.table_name)

        if not exist:
            symbol_table = symbol_table.parent
            return table_result

        table_records: [Registro] = RecordRepository().obtener_registros_de_tabla(db.value, self.table_name)

        for table_record in table_records:
            for i in range(len(table_record.campos)):
                column_in_table: Variable = symbol_table.find_column_by_id(table_record.campos[i])
                if column_in_table is not None:
                    column_in_table.value = table_record.valores[i]

            if self.where_instruction is not None:
                where_result: Variable = self.where_instruction.execute(symbol_table, errors)
                if where_result is None:
                    print("Where statement should return a value.")
                    symbol_table = symbol_table.parent
                    return None

                if where_result.variable_type.type != 'int':
                    print("An int value was expected.")
                    symbol_table = symbol_table.parent
                    return None

                if where_result.value < 1:
                    continue

            column_names = []
            column_values = []

            for table_column in self.table_columns:
                result: Variable = table_column.execute(symbol_table, errors)

                if result is None:
                    print("The column doesn't return anything.")
                    symbol_table = symbol_table.parent
                    return None

                if result.id == 'all':
                    for i in range(len(table_record.campos)):
                        column_names.append(table_record.campos[i])
                        column_values.append(table_record.valores[i])
                    continue

                column_names.append(result.id)
                column_values.append(result.value)

            record = Registro(column_names, column_values)
            table_result[1].append(record)

        print("Fields added to symbol table :D")
        symbol_table = symbol_table.parent
        matriz_select = tabla_select_a_matriz(table_result)
        print(table_result[0])
        for t_r in table_result[1]:
            print(t_r)
        return matriz_select


    def dot(self, nodo_padre, graficador):
        pass

    def c3d(self, scope):
        pass