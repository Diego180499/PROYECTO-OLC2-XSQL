from .Instruction import Instruction


class SetStatement(Instruction):

    def __init__(self, line, column, assignments: [Instruction]):
        super().__init__(line, column)
        self.assignments = assignments

    def execute(self):
        for assignment in self.assignments:
            assignment.execute()
