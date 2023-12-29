from .Instruction import Instruction
from .Variable import Variable
from .VariableType import VariableType
from .symbolTable.SymbolTable import SymbolTable
from .symbolTable.ScopeType import ScopeType
from .ProcedureModel import ProcedureModel
from .FunctionModel import FunctionModel
import re

from ..error.xsql_error import xsql_error


class ExecStatement(Instruction):

    def __init__(self, line, column, id, args: [Instruction]):
        super().__init__(line, column)
        self.id = id
        self.args = args

    def execute(self, symbol_table: SymbolTable, errors):

        fun_in_table = symbol_table.find_function_by_id(self.id)

        if fun_in_table is None:
            procedure_in_table = symbol_table.find_procedure_by_id(self.id)

            if procedure_in_table is None:
                print(f"fun/procedure with name: {self.id} doesn't found")
                errors.append(self.semantic_error(f"fun/procedure with name: {self.id} doesn't found"))
                return None
            self.exec_procedure(procedure_in_table, symbol_table, errors)
            return None

        fun_result = self.exec_function(fun_in_table, symbol_table, errors)

        if fun_result is None:
            print("The function doesn't return anything.")
            errors.append(self.semantic_error(f'The function doesnt return anything.'))

        return fun_result

    def exec_procedure(self, procedure_in_table: Variable, symbol_table: SymbolTable, errors):
        procedure: ProcedureModel = procedure_in_table.value
        args_result: [Variable] = []
        for arg in self.args:
            arg_result: Variable = arg.execute(symbol_table, errors)

            if arg_result is None:
                print("The argument couldn't be executed")
                errors.append(self.semantic_error(f"The argument couldn't be executed"))
                return None

            if arg_result.id is not None:
                find = any((a.id == arg_result.id) for a in args_result)

                if find:
                    print('The argument already exists')
                    errors.append(self.semantic_error("The argument already exists"))
                    return None

            args_result.append(arg_result)

        if len(args_result) != len(procedure.parameters):
            print("The arguments and parameters number doesn't match")
            errors.append(self.semantic_error("The arguments and parameters number doesn't match"))
            return None

        symbol_table = SymbolTable(ScopeType().PROC, symbol_table)
        if len(args_result) > 0 and args_result[0].id is not None:

            for arg in args_result:
                find = None
                for param in procedure.parameters:
                    if param.id == arg.id:
                        find = param
                        break

                if find is None:
                    print(f"The parameter {arg.id} doesn't exist")
                    errors.append(self.semantic_error(f"The parameter {arg.id} doesn't exist"))
                    symbol_table = symbol_table.parent

                    return None

                if find.variable_type.type == 'nchar' or find.variable_type.type == 'nvarchar':
                    if find.variable_type.length < arg.variable_type.length:
                        print("The length value is too long")
                        errors.append(self.semantic_error("The length value is too long"))
                        symbol_table = symbol_table.parent

                        return None
                    find.value = arg.value
                    symbol_table.add_variable(find)
                    continue

                if find.variable_type.type == 'date':
                    if not re.search("\d{2}-\d{2}-\d{4}", arg.value):
                        print('Date value was expected')
                        errors.append(self.semantic_error('Date value was expected'))
                        symbol_table = symbol_table.parent

                        return None

                    find.value = arg.value
                    symbol_table.add_variable(find)
                    continue

                if find.variable_type.type == 'datetime':
                    if not re.search("\d{2}-\d{2}-\d{4} (\d{2}:\d{2}:\d{2}|\d{2}:\d{2})", arg.value):
                        print('Datetime value was expected')
                        errors.append(self.semantic_error('Datetime value was expected'))
                        symbol_table = symbol_table.parent

                        return None

                    find.value = arg.value
                    symbol_table.add_variable(find)
                    continue

                if find.variable_type.type != arg.variable_type.type:
                    print(f"Variable type doesn't match")
                    errors.append(self.semantic_error(f"Variable type doesn't match"))
                    symbol_table = symbol_table.parent

                    return None

                find.value = arg.value
                symbol_table.add_variable(find)

        else:

            for i in range(len(procedure.parameters)):
                parameter: Variable = procedure.parameters[i]

                if parameter.variable_type.type == 'nchar' or parameter.variable_type.type == 'nvarchar':
                    if parameter.variable_type.length < args_result[i].variable_type.length:
                        print("The length value is too long")
                        errors.append(self.semantic_error("The length value is too long"))
                        symbol_table = symbol_table.parent

                        return None
                    parameter.value = args_result[i].value
                    symbol_table.add_variable(parameter)
                    continue
                if parameter.variable_type.type == 'date':
                    if not re.search("\d{2}-\d{2}-\d{4}", args_result[i].value):
                        print('Date value was expected')
                        errors.append(self.semantic_error('Date value was expected'))
                        symbol_table = symbol_table.parent

                        return None

                    parameter.value = args_result[i].value
                    symbol_table.add_variable(parameter)
                    continue

                if parameter.variable_type.type == 'datetime':
                    if not re.search("\d{2}-\d{2}-\d{4} (\d{2}:\d{2}:\d{2}|\d{2}:\d{2})", args_result[i].value):
                        print('Datetime value was expected')
                        errors.append(self.semantic_error('Datetime value was expected'))
                        symbol_table = symbol_table.parent

                        return None

                    parameter.value = args_result[i].value
                    symbol_table.add_variable(parameter)
                    continue

                if parameter.variable_type.type != args_result[i].variable_type.type:
                    print(f"Variable type doesn't match")
                    errors.append(self.semantic_error(f"Variable type doesn't match"))
                    symbol_table = symbol_table.parent

                    return None

                parameter.value = args_result[i].value
                symbol_table.add_variable(parameter)

        procedure.block.execute(symbol_table, errors)
        symbol_table = symbol_table.parent

    def exec_function(self, fun_in_table: Variable, symbol_table: SymbolTable, errors):
        function: FunctionModel = fun_in_table.value
        args_result: [Variable] = []
        for arg in self.args:
            arg_result: Variable = arg.execute(symbol_table, errors)

            if arg_result is None:
                print("The argument couldn't be executed")
                errors.append(self.semantic_error("The argument couldn't be executed"))
                return None

            if arg_result.id is not None:
                find = any((a.id == arg_result.id) for a in args_result)

                if find:
                    print('The argument already exists')
                    errors.append(self.semantic_error('The argument already exists'))
                    return None

            args_result.append(arg_result)

        if len(args_result) != len(function.parameters):
            print("The arguments and parameters number doesn't match")
            errors.append(self.semantic_error("The arguments and parameters number doesn't match"))
            return None

        symbol_table = SymbolTable(ScopeType().FUN, symbol_table)
        if len(args_result) > 0 and args_result[0].id is not None:

            for arg in args_result:
                find = None
                for param in function.parameters:
                    if param.id == arg.id:
                        find = param
                        break

                if find is None:
                    print(f"The parameter {arg.id} doesn't exist")
                    errors.append(self.semantic_error(f"The parameter {arg.id} doesn't exist"))
                    symbol_table = symbol_table.parent
                    return None

                if find.variable_type.type == 'nchar' or find.variable_type.type == 'nvarchar':
                    if find.variable_type.length < arg.variable_type.length:
                        print("The length value is too long")
                        errors.append(self.semantic_error("The length value is too long"))
                        symbol_table = symbol_table.parent

                        return None
                    find.value = arg.value
                    symbol_table.add_variable(find)
                    continue

                if find.variable_type.type == 'date':
                    if not re.search("\d{2}-\d{2}-\d{4}", arg.value):
                        print('Date value was expected')
                        errors.append(self.semantic_error('Date value was expected'))
                        symbol_table = symbol_table.parent

                        return None

                    find.value = arg.value
                    symbol_table.add_variable(find)
                    continue

                if find.variable_type.type == 'datetime':
                    if not re.search("\d{2}-\d{2}-\d{4} (\d{2}:\d{2}:\d{2}|\d{2}:\d{2})", arg.value):
                        print('Datetime value was expected')
                        errors.append(self.semantic_error('Datetime value was expected'))
                        symbol_table = symbol_table.parent
                        return None

                    find.value = arg.value
                    symbol_table.add_variable(find)
                    continue

                if find.variable_type.type != arg.variable_type.type:
                    print(f"Variable type doesn't match")
                    errors.append(self.semantic_error(f"Variable type doesn't match"))
                    symbol_table = symbol_table.parent
                    return None

                find.value = arg.value
                symbol_table.add_variable(find)

        else:

            for i in range(len(function.parameters)):
                parameter: Variable = function.parameters[i]

                if parameter.variable_type.type == 'nchar' or parameter.variable_type.type == 'nvarchar':
                    if parameter.variable_type.length < args_result[i].variable_type.length:
                        print("The length value is too long")
                        errors.append(self.semantic_error("The length value is too long"))
                        symbol_table = symbol_table.parent
                        return None
                    parameter.value = args_result[i].value
                    symbol_table.add_variable(parameter)
                    continue

                if parameter.variable_type.type == 'date':
                    if not re.search("\d{2}-\d{2}-\d{4}", args_result[i].value):
                        print('Date value was expected')
                        errors.append(self.semantic_error('Date value was expected'))
                        symbol_table = symbol_table.parent

                        return None

                    parameter.value = args_result[i].value
                    symbol_table.add_variable(parameter)
                    continue

                if parameter.variable_type.type == 'datetime':
                    if not re.search("\d{2}-\d{2}-\d{4} (\d{2}:\d{2}:\d{2}|\d{2}:\d{2})", args_result[i].value):
                        print('Datetime value was expected')
                        errors.append(self.semantic_error('Datetime value was expected'))
                        symbol_table = symbol_table.parent

                        return None

                    parameter.value = args_result[i].value
                    symbol_table.add_variable(parameter)
                    continue

                if parameter.variable_type.type != args_result[i].variable_type.type:
                    print(f"Variable type doesn't match")
                    errors.append(self.semantic_error(f"Variable type doesn't match"))
                    symbol_table = symbol_table.parent

                    return None

                parameter.value = args_result[i].value
                symbol_table.add_variable(parameter)

        return_result: Variable = function.block.execute(symbol_table, errors)

        if return_result is not None:

            if function.return_type.type == 'nchar' \
                    or function.return_type.type == 'nvarchar':

                if return_result.variable_type.type != 'nchar' and return_result.variable_type.type != 'nvarchar':
                    print("The return type doesn't match")
                    errors.append(self.semantic_error("The return type doesn't match"))
                    return None

                if function.return_type.length < return_result.variable_type.length:
                    print("The value is too long")
                    errors.append(self.semantic_error("The value is too long"))
                    symbol_table = symbol_table.parent
                    return None

                return return_result

            if return_result.variable_type.type != function.return_type.type:
                print("The return type doesn't match")
                errors.append(self.semantic_error("The return type doesn't match"))
                symbol_table = symbol_table.parent
                return None

            symbol_table = symbol_table.parent
            return return_result


        symbol_table = symbol_table.parent

    def semantic_error(self, description):
        return xsql_error(description, '', 'Error Semantico', f'Linea {self.line} Columna {self.column}')

    def dot(self,nodo_padre, graficador):
        current_node = graficador.agregarNode('exec')
        graficador.agregarRelacion(nodo_padre,current_node)
        lable_exec = graficador.agregarNode(self.id)
        args = graficador.agregarNode('args')
        graficador.agregarRelacion(current_node,lable_exec)
        graficador.agregarRelacion(current_node,args)
        for arg in self.args:
            arg.dot(args,graficador)

        
    def c3d(self,symbol_table,generador):
        pass