from VariableType import VariableType


class Variable:

    def __init__(self, id: str, variable_type: VariableType, value):
        self.id = id
        self.variable_type = variable_type
        self.value = value
