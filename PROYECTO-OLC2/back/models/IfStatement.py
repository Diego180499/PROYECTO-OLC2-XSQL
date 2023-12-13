from Instruction import Instruction


class IfStatement(Instruction):

    def __init__(self, line, column, condition, trueBlock, falseBlock):
        super().__init__(line, column)
        self.condition = condition
        self.trueBlock = trueBlock
        self.falseBlock = falseBlock

    def execute(self):
        print('Execute ifStatement')

    def __str__(self):
        return f"""{{"IfStatement": {self.condition}, {self.trueBlock}, {self.falseBlock} }}"""
