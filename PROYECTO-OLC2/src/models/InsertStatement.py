from .Instruction import Instruction
from .symbolTable.SymbolTable import SymbolTable
from .Variable import Variable
from ..error.xsql_error import xsql_error
from ..repository.records.record_repository import RecordRepository
from ..FILES.manager_db.db_file_manager import get_table_field_by_name, obtener_nombres_campos_tabla
from ..FILES.manager_db.record_file_manager import existe_archivo_registros
from ..FILES.Campo import Campo
from ..FILES.Registro import Registro
from .symbolTable.ScopeType import ScopeType
from .SymbolType import SymbolType
from re import search


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
            errors.append(self.semantic_error("There's no database selected."))
            return None

        if len(self.column_names) != len(self.values):
            print(f"You declare {len(self.column_names)} columns and assign {len(self.values)} values.")
            errors.append(self.semantic_error(f"You declare {len(self.column_names)} columns and assign {len(self.values)} values."))
            return None

        symbol_table = SymbolTable(ScopeType().INSERT, symbol_table)
        table_fields = obtener_nombres_campos_tabla(db.value, self.table_name)

        for i in range(len(self.column_names)):
            column_declared = any((field == self.column_names[i]) for field in table_fields)

            if not column_declared:
                print(f"The column: {self.column_names[i]} doesn't exist in the table: {self.table_name}")
                errors.append(self.semantic_error(f"The column: {self.column_names[i]} doesn't exist in the table: {self.table_name}"))
                symbol_table = symbol_table.parent
                return None

            value_result: Variable = self.values[i].execute(symbol_table, errors)

            if value_result is None:
                print(f"The value for column: {self.column_names[i]} doesn't return anything.")
                errors.append(self.semantic_error(f"The value for column: {self.column_names[i]} doesn't return anything."))
                symbol_table = symbol_table.parent
                return None

            column_in_table = symbol_table.find_column_by_id(self.column_names[i])
            if column_in_table is not None:
                print(f"Column: {self.column_names[i]} already declared.")
                errors.append(self.semantic_error(f"Column: {self.column_names[i]} already declared."))
                symbol_table = symbol_table.parent
                return None

            column_result = Variable()
            column_result.id = self.column_names[i]
            column_result.variable_type = value_result.variable_type
            column_result.symbol_type = SymbolType().COLUMN
            column_result.value = value_result.value
            symbol_table.add_variable(column_result)

        field_names = []
        field_values = []
        record_repository = RecordRepository()

        for table_field in table_fields:
            field: Campo = get_table_field_by_name(db.value, self.table_name, table_field)
            column_in_table: Variable = symbol_table.find_column_by_id(table_field)

            if int(field.nulo) == 0 and column_in_table is None:
                print(f"The field: {table_field} can't be null.")
                errors.append(self.semantic_error(f"The field: {table_field} can't be null."))
                symbol_table = symbol_table.parent
                return None

            if int(field.llavePrim) == 1 and column_in_table is None:
                print(f"The primary key: {table_field} can't be null.")
                errors.append(self.semantic_error(f"The primary key: {table_field} can't be null."))
                symbol_table = symbol_table.parent
                return None

            if str(field.tablaRef) != "-" and column_in_table is None:
                print(f"The primary key: {table_field} can't be null.")
                errors.append(self.semantic_error(f"The primary key: {table_field} can't be null."))
                symbol_table = symbol_table.parent
                return None

            if column_in_table is None:
                field_names.append(table_field)
                field_values.append(0)
                continue

            if int(field.llavePrim) == 1:
                table_records: [Registro] = []

                if existe_archivo_registros(db.value, self.table_name):
                    table_records: [Registro] = record_repository.obtener_registros_de_tabla(db.value, self.table_name)

                already_exist = self.find_value(table_records, table_field, column_in_table.value)

                if already_exist:
                    print(f"The primary key: {table_field} is unique.")
                    errors.append(self.semantic_error(f"The primary key: {table_field} is unique."))
                    symbol_table = symbol_table.parent
                    return None

            if str(field.tablaRef) != "-":
                table_records: [Registro] = []
                if existe_archivo_registros(db.value, field.tablaRef):
                    table_records: [Registro] = record_repository.obtener_registros_de_tabla(db.value, field.tablaRef)

                find = self.find_value(table_records, field.campoRef, column_in_table.value)

                if not find:
                    print(f"The foreign key: {table_field} doesn't exist.")
                    errors.append(self.semantic_error(f"The foreign key: {table_field} doesn't exist."))
                    symbol_table = symbol_table.parent
                    return None

            if field.tipoDato == 'nvarchar' or field.tipoDato == 'nchar':
                if column_in_table.variable_type.type != 'nvarchar' and column_in_table.variable_type.type != 'nchar':
                    print("nchar or nvarchar value was expected.")
                    errors.append(self.semantic_error("nchar or nvarchar value was expected."))
                    symbol_table = symbol_table.parent
                    return None

                field_names.append(column_in_table.id)
                field_values.append(column_in_table.value)
                continue

            if field.tipoDato == 'date':
                if not search("\d{2}-\d{2}-\d{4}", column_in_table.value):
                    print('Date value was expected')
                    errors.append(self.semantic_error('Date value was expected'))
                    symbol_table = symbol_table.parent
                    return None

                field_names.append(column_in_table.id)
                field_values.append(column_in_table.value)

                continue

            if field.tipoDato == 'datetime':
                if not search("\d{2}-\d{2}-\d{4} (\d{2}:\d{2}:\d{2}|\d{2}:\d{2})", column_in_table.value):
                    print('Datetime value was expected')
                    errors.append(self.semantic_error('Datetime value was expected'))
                    symbol_table = symbol_table.parent
                    return None

                field_names.append(column_in_table.id)
                field_values.append(column_in_table.value)
                continue

            if field.tipoDato != column_in_table.variable_type.type:
                print(f"The field: {table_field} has: {field.tipoDato} as data type and you declared: "
                      f"{column_in_table.variable_type.type} instead.")
                errors.append(self.semantic_error(f"The field: {table_field} has: {field.tipoDato} as data type and you declared: "
                      f"{column_in_table.variable_type.type} instead."))
                symbol_table = symbol_table.parent
                return None

            field_names.append(column_in_table.id)
            field_values.append(column_in_table.value)

        message = record_repository.insertar_registro(db.value, self.table_name, field_names, field_values)
        print(f"Record saved in table: {self.table_name}")
        print(message[0], message[1])
        symbol_table = symbol_table.parent

    def find_value(self, table_records: [Registro], table_field: str, value: any):

        for table_record in table_records:
            index = 0
            for i in range(len(table_record.campos)):
                if table_record.campos[i] == table_field:
                    index = i
                    break

            if str(table_record.valores[index]) == str(value):
                return True
        return False

    def semantic_error(self, description):
        return xsql_error(description, '', 'Error Semantico', f'Linea {self.line} Columna {self.column}')


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
