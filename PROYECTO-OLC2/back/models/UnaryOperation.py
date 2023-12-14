from .Instruction import Instruction


class UnaryOperation(Instruction):

    def __init__(self, line, column, left_operation, operator):
        super().__init__(line,column)
        self.left_operation = left_operation
        self.operator = operator

    def execute(self):
        pass