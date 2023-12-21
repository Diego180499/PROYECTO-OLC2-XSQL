from src.models.Variable import Variable
from src.models.SymbolType import SymbolType
from .ScopeType import ScopeType


class SymbolTable:

    def __init__(self, scope_type: ScopeType, parent=None):
        self.symbols = []
        self.scope_type = scope_type
        self.parent = parent

    def add_variable(self, variable: Variable):
        self.symbols.append(variable)

    def find_var_by_id(self, id: str):
        current_table = self

        while current_table is not None:

            for symbol in current_table.symbols:
                if symbol.id == id and symbol.symbol_type == SymbolType().VARIABLE:
                    return symbol

            current_table = current_table.parent

        return None

    def find_column_by_id(self, id: str):
        for symbol in self.symbols:
            if symbol.id == id and symbol.symbol_type == SymbolType().COLUMN:
                return symbol

        return None

    def find_function_by_id(self, id: str):
        current_table = self

        while current_table is not None:
            for symbol in current_table.symbols:

                if symbol.id == id and symbol.symbol_type == SymbolType().FUNCTION:
                    return symbol

            current_table = current_table.parent

        return None

    def find_procedure_by_id(self, id: str):
        current_table = self

        while current_table is not None:
            for symbol in current_table.symbols:
                if symbol.id == id and symbol.symbol_type == SymbolType().PROCEDURE:
                    return symbol

            current_table = current_table.parent

        return None

    def find_database(self):
        current_table = self

        while current_table is not None:
            for symbol in current_table.symbols:
                if symbol.symbol_type == SymbolType().DB_NAME:
                    return symbol
            current_table = current_table.parent
        return None

    def is_in_fun_scope(self):
        current_table = self

        while current_table is not None:
            if current_table.scope_type == ScopeType().GLOBAL or current_table.scope_type == ScopeType().PROC:
                return False

            if current_table.scope_type == ScopeType().FUN:
                return True

            current_table = current_table.parent

        return False
