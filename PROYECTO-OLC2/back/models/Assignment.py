from Instruction import Instruction


class Assignment(Instruction):

    def __init__(self, line, column, id: str, value: Instruction):
        super().__init__(line, column)
        self.id = id
        self.value = value

    def execute(self):
        pass