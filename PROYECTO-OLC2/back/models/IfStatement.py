from Instruction import Instruction


class IfStatement(Instruction):

    def __init__(self, line, column, condition, true_block: [Instruction], false_block: [Instruction]):
        super().__init__(line, column)
        self.condition = condition
        self.true_block = true_block
        self.false_block = false_block

    def execute(self):
        print('Execute ifStatement')

    def __str__(self):
        return f"""{{"IfStatement": {self.condition}, {self.trueBlock}, {self.falseBlock} }}"""
