from .Instruction import Instruction
from .symbolTable.SymbolTable import SymbolTable
from .Variable import Variable
from .VariableType import VariableType
from .SymbolType import SymbolType
from .ProcedureModel import ProcedureModel


class ProcedureStatement(Instruction):

    def __init__(self, line, column, id: str, parameters: [Instruction], instructions: [Instruction]):
        super().__init__(line, column)
        self.id = id
        self.parameters = parameters
        self.instructions = instructions

    def execute(self, symbol_table: SymbolTable):
        procedure_in_table = symbol_table.find_procedure_by_id(self.id)

        if procedure_in_table is not None:
            print('Procedure already exists')
            return None

        params = []

        for param in self.parameters:
            param_result: Variable = param.execute(symbol_table)

            if param_result is None:
                print("The parameter couldn't be declared")
                return None

            find = any((p.id == param_result.id) for p in params)

            if find:
                print('Parameter already exists')
                return None

            params.append(param_result)

        procedure_result = Variable()
        procedure_result.variable_type = VariableType('void', 0)
        procedure_result.symbol_type = SymbolType().PROCEDURE
        procedure_result.id = self.id
        procedure_result.value = ProcedureModel(self.id, params, self.instructions)

        symbol_table.add_variable(procedure_result)

    def dot(self,nodo_padre, graficador):
        pass

    def c3d(self,scope):
        pass