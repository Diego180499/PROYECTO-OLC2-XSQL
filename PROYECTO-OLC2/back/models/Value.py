from .Instruction import Instruction
from .ValueType import ValueType


class Value(Instruction):

    def __init__(self, line, column, value, value_type: ValueType):
        super().__init__(line, column)
        self.value = value
        self.value_type = value_type

    def execute(self):
        print(f'{{Value: {self.value} {self.value_type} }}')
