from Instruction import Instruction
from ValueType import ValueType


class Value(Instruction):

    def __init__(self, line, column, value, value_type: ValueType, length):
        super().__init__(line, column)
        self.value = value
        self.value_type = value_type
        self.length = length

    def execute(self):
        pass
