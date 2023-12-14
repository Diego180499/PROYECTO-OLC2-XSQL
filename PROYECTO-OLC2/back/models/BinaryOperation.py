from .Instruction import Instruction


class BinaryOperation(Instruction):

    def __init__(self, line, column, left_operation: Instruction, right_operation: Instruction, operator):
        super().__init__(line, column)
        self.left_operation = left_operation
        self.right_operation = right_operation
        self.operator = operator


    def execute(self):
        left = self.left_operation.execute()
        right = self.right_operation.execute()
        print("Binary op operator:", self.operator)