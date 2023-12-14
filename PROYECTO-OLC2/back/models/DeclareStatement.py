from .Instruction import Instruction


class DeclareStatement(Instruction):

    def __init__(self, line, column, id: str, type: str):
        super().__init__(line, column)
        self.type = type
        self.id = id

    def execute(self):
        print('Execute DeclareStatement')
