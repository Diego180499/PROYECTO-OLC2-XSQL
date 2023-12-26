from .Instruction import Instruction
from .symbolTable.SymbolTable import SymbolTable
from .Variable import Variable
from ..error.xsql_error import xsql_error


class WhenStatement(Instruction):

    def __init__(self, line, column, condition: Instruction, true_block: Instruction, false_block: Instruction):
        super().__init__(line, column)
        self.condition = condition
        self.true_block = true_block
        self.false_block = false_block

    def execute(self, symbol_table: SymbolTable, errors):
        result: Variable = self.condition.execute(symbol_table, errors)

        if result is None:
            print('A value was expected')
            errors.append(self.semantic_error('A value was expected'))
            return None

        if result.variable_type.type != 'int':
            print('int type was expected')
            errors.append(self.semantic_error('int type was expected'))
            return None

        if result.value > 0:
            true_result = self.true_block.execute(symbol_table, errors)

            if true_result is None:
                print('A value was expected in when then statement')
                errors.append(self.semantic_error('A value was expected in when then statement'))
                return None

            return true_result
        else:
            if self.false_block is not None:
                return self.false_block.execute(symbol_table, errors)

    def __str__(self):
        return f"""{{"WhenState": {self.condition}, {self.false_block}}}"""

    def semantic_error(self, description):
        return xsql_error(description, '', 'Error Semantico', f'Linea {self.line} Columna {self.column}')

    def dot(self,nodo_padre, graficador):
        pass
        
    def c3d(self,scope):
        pass