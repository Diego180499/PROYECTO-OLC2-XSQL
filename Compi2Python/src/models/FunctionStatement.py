from .Instruction import Instruction
from .symbolTable.SymbolTable import SymbolTable
from .Variable import Variable
from .VariableType import VariableType
from .SymbolType import SymbolType
from .FunctionModel import FunctionModel
from ..error.xsql_error import xsql_error


class FunctionStatement(Instruction):

    def __init__(self, line, column, id: str, parameters: [Instruction], block: Instruction, type: VariableType):
        super().__init__(line, column)
        self.id = id
        self.parameters = parameters
        self.block = block
        self.return_type = type

    def execute(self, symbol_table: SymbolTable, errors):
        fun_in_table: Variable = symbol_table.find_function_by_id(self.id)

        if fun_in_table is not None:
            print("Function already exists")
            errors.append(self.semantic_error("Function already exists"))
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

        length = 0
        if isinstance(self.return_type.length, Instruction):
            result: Variable = self.return_type.length.execute(symbol_table, errors)

            if result is None:
                print('value cannot be set to the data type')
                errors.append(self.semantic_error('value cannot be set to the data type'))
                return None

            if result.variable_type.type != 'int':
                print('int type was expected')
                errors.append(self.semantic_error('int type was expected'))
                return None

            length = int(result.value)
        else:
            length = int(self.return_type.length)

        function_result = Variable()
        function_result.variable_type = VariableType(self.return_type.type, length)
        function_result.symbol_type = SymbolType().FUNCTION
        function_result.id = self.id
        function_result.value = FunctionModel(self.id, params, self.block, function_result.variable_type)

        symbol_table.add_variable(function_result)

    def __str__(self):
        return f"FunctionStatement: id: {self.id}, tipo: {self.return_type.type}"


    def semantic_error(self, description):
        return xsql_error(description, '', 'Error Semantico', f'Linea {self.line} Columna {self.column}')

    def dot(self,nodo_padre, graficador):
        current_node = graficador.agregarNode(self.id)
        graficador.agregarRelacion(nodo_padre, current_node)
        code = graficador.agregarNode('code')
        args = graficador.agregarNode('args')
        graficador.agregarRelacion(current_node, args)
        graficador.agregarRelacion(current_node, code)
        for arg in self.parameters:
            arg.dot(args, graficador)
        self.block.dot(code, graficador)
        
    def c3d(self,scope,generador):
        pass