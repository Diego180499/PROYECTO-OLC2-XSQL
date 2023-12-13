from Instruction import Instruction


class Value(Instruction):

    def __init__(self, line, column, value, valueType):
        super().__init__(line, column)
        self.value = value
        self.valueType = valueType

    def execute(self):
        pass