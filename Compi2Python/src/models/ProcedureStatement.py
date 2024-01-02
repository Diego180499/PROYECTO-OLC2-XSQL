from .Instruction import Instruction
from .symbolTable.SymbolTable import SymbolTable
from .Variable import Variable
from .VariableType import VariableType
from .SymbolType import SymbolType
from .ProcedureModel import ProcedureModel
from ..error.xsql_error import xsql_error
from src.repository.data_base.data_base_repository import *


class ProcedureStatement(Instruction):

    def __init__(self, line, column, id: str, parameters: [Instruction], block: Instruction):
        super().__init__(line, column)
        self.id = id
        self.parameters = parameters
        self.block = block
        self.data_base_repository = DataBaseRepository()

    def execute(self, symbol_table: SymbolTable, errors):
        procedure_in_table = symbol_table.find_procedure_by_id(self.id)

        if procedure_in_table is not None:
            print('Procedure already exists')
            errors.append(self.semantic_error('Procedure already exists'))
            return None

        params = []

        for param in self.parameters:
            param_result: Variable = param.execute(symbol_table, errors)

            if param_result is None:
                print("The parameter couldn't be declared")
                errors.append(self.semantic_error("The parameter couldn't be declared"))
                return None

            find = any((p.id == param_result.id) for p in params)

            if find:
                print('Parameter already exists')
                errors.append(self.semantic_error('Parameter already exists'))
                return None

            params.append(param_result)

        procedure_result = Variable()
        procedure_result.variable_type = VariableType('void', 0)
        procedure_result.symbol_type = SymbolType().PROCEDURE
        procedure_result.id = self.id
        procedure_result.value = ProcedureModel(self.id, params, self.block)
        res = self.data_base_repository.guardar_procedimiento(symbol_table.find_database().id,procedure_result.id)
        if not res  :
            errors.append(self.semantic_error(f'The procedure {procedure_result.id} already exist in data base {symbol_table.find_database().id}'))
            return None
        symbol_table.add_variable(procedure_result)


    def semantic_error(self, description):
        return xsql_error(description, '', 'Error Semantico', f'Linea {self.line} Columna {self.column}')

    def dot(self,nodo_padre, graficador):
        current_node = graficador.agregarNode("procedure")
        graficador.agregarRelacion(nodo_padre, current_node)
        id_node = graficador.agregarNode(self.id)
        graficador.agregarRelacion(current_node, id_node)
        if self.parameters is not None:
            params_node = graficador.agregarNode("params")
            graficador.agregarRelacion(current_node, params_node)
            for param in self.parameters:
                param.dot(params_node, graficador)
        if self.block is not None:
            block_node = graficador.agregarNode("block")
            graficador.agregarRelacion(current_node, block_node)
            self.block.dot(block_node, graficador)

    def c3d(self,symbol_table,generador):
        pass