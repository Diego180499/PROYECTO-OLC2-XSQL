from .Instruction import Instruction


class CaseStatement(Instruction):

    def node_name(self):
        return f'if_{self.line}_{self.column}'

    def node_value(self):
        return f'If_statement'

    def condition_name(self):
        return f'condition_{self.line}_{self.column}'

    def condition_value(self):
        return f'condition'

    def true_name(self):
        return f'true_{self.line}_{self.column}'

    def true_value(self):
        return f'true_block'

    def false_name(self):
        return f'false_{self.line}_{self.column}'

    def false_value(self):
        return f'false_block'

    def accept(self, visitor):
        return visitor.visit_if(self)

    def __init__(self, line, column, condition, bloque_else, columnName):
        super().__init__(line, column)
        self.conditions = condition #When statements
        self.bloque_else = bloque_else
        self.columnName = columnName

    def __str__(self):
        return f"""{{"CaseState": {self.conditions}, {self.bloque_else}, {self.columnName}}}"""