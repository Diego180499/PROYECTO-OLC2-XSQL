from .Instruction import Instruction
from .symbolTable import SymbolTable
from .Variable import Variable
from .VariableType import VariableType
from .SymbolType import SymbolType


class FunctionStatement(Instruction):

    def __init__(self, line, column, id: str, parameters: [Instruction], instructions: [Instruction], type: VariableType):
        super().__init__(line, column)
        self.id = id
        self.parameters = parameters
        self.instructions = instructions
        self.return_type = type

    def execute(self, symbol_table: SymbolTable):
        fun_in_table: Variable = symbol_table.find_function_by_id(self.id)

        if fun_in_table is not None:
            print("Function already exists")
            return None

        params = []

        for param in self.parameters:
            param_result: Variable = param.execute(symbol_table)

            if param_result is None:
                print("The parameter couldn't be declared")
                return None

            find = any((p.id == param_result.id) for p in params)

            if find is not None:
                print('Variable already exists')
                return None

            params.append(param_result)


