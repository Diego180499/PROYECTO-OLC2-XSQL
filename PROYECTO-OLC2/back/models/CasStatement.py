from .Instruction import Instruction
from .Variable import Variable
from .VariableType import VariableType
from .symbolTable.SymbolTable import SymbolTable
import re


class CasStatement(Instruction):

    def __init__(self, line, column, value: Instruction, type: VariableType):
        super().__init__(line, column)
        self.value = value
        self.type = type

    def execute(self, symbol_table: SymbolTable):

        value_result: Variable = self.value.execute(symbol_table)

        if value_result is None:
            print('A value was expected')
            return None

        variable_type = VariableType(self.type.type, 32)
        if isinstance(self.type.length, Instruction):
            length_result: Variable = self.type.length.execute(symbol_table)

            if length_result is None:
                print("A value was expected")
                return None

            if length_result.variable_type.type != 'int':
                print('Int type was expected')
                return None

            variable_type.length = length_result.value

        if variable_type.type == 'int':
            result = Variable()
            result.variable_type = variable_type

            if str(value_result.value).isnumeric():
                result.value = int(value_result.value)
            else:
                result.value = sum(ord(character) for character in str(value_result.value))

            return result
        elif variable_type.type == 'decimal':
            result = Variable()
            result.variable_type = variable_type

            if str(value_result.value).isnumeric():
                result.value = float(value_result.value)
            else:
                result.value = sum(ord(character) for character in str(value_result.value))

            return result
        elif variable_type.type == 'nchar' or variable_type.type == 'nvarchar':
            if len(value_result.value) > variable_type.length:
                print('the value is too long')
                return None

            result = Variable()
            result.variable_type = variable_type
            result.value = str(value_result.value)
            return result

        elif variable_type.type == 'date':
            if not re.search("\d{2}-\d{2}-\d{4}", value_result.value):
                print('Date value was expected')
                return None

            result = Variable()
            result.variable_type = variable_type
            result.value = value_result.value
            return result
        elif variable_type.type == 'datetime':
            if not re.search("\d{2}-\d{2}-\d{4} (\d{2}:\d{2}:\d{2}|\d{2}:\d{2})", value_result.value):
                print('Datetime value was expected')
                return None

            result = Variable()
            result.variable_type = variable_type
            result.value = value_result.value
            return result

    def dot(self,nodo_padre, graficador):
        pass

    def c3d(self, scope):
        pass