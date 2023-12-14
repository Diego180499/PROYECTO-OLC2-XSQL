from VariableType import VariableType
from SymbolType import SymbolType


class Variable:

    def __init__(self, id: str, variable_type: VariableType, symbol_type: SymbolType, value):
        self.id = id
        self.variable_type = variable_type
        self.symbol_type = symbol_type
        self.value = value
