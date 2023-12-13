from Instruction import Instruction


class SetStatement(Instruction):

    def __init(self, line, column, assignments: [Instruction]):
        super().__init__(line, column)
        self.assignments = assignments

    def execute(self):
        pass