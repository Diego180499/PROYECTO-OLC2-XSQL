from .Instruction import Instruction
from src.repository.table.table_repository import TableRepository
from .symbolTable.SymbolTable import SymbolTable
from .symbolTable.ScopeType import ScopeType
from .Variable import Variable


class CreateTableStatement(Instruction):

    def __init__(self, line, column, table_name: str, properties: [Instruction]):
        super().__init__(line, column)
        self.table_name = table_name
        self.properties: [Instruction] = properties

    def execute(self, symbol_table: SymbolTable, errors):
        db: Variable = symbol_table.find_database()

        if db is None:
            print("There's no database selected")
            return None

        table_exist = TableRepository().existe_tabla_en_bd(db.value, self.table_name)

        if table_exist:
            print(f"The table: {self.table_name} already exists")
            return None

        table_properties: [Variable] = []

        symbol_table = SymbolTable(ScopeType().CREATE, symbol_table)
        for property in self.properties:
            property_result: Variable = property.execute(symbol_table, errors)

            if property_result is None:
                print("The property couldn't be declared")
                symbol_table = symbol_table.parent
                return None

            table_properties.append(property_result)

        message = TableRepository().crear_tabla(self.table_name, db.value)
        print(message)

        for table_prop in table_properties:
            message = TableRepository().agregar_campos_tabla(db.value, self.table_name, table_prop.value)
            print(message)

        symbol_table = symbol_table.parent

    def dot(self, nodo_padre, graficador):
        pass

    def c3d(self, scope):
        pass