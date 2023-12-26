from .Instruction import Instruction
from .symbolTable.SymbolTable import SymbolTable
from .Variable import Variable
from .VariableType import VariableType
import re

from ..error.xsql_error import xsql_error


class SetStatement(Instruction):

    def __init__(self, line, column, assignments: [Instruction]):
        super().__init__(line, column)
        self.assignments = assignments

    def execute(self, symbol_table: SymbolTable, errors):
        for assignment in self.assignments:
            result: Variable = assignment.execute(symbol_table, errors)

            if result is None:
                print("Couldn't assign a value")
                return None

            var_in_table: Variable = symbol_table.find_var_by_id(result.id)

            if var_in_table is None:
                print(f"The variable: {result.id} doesn't exists")
                errors.append(self.semantic_error(f"The variable: {result.id} doesn't exists"))
                continue

            if var_in_table.variable_type.type == 'nchar' or var_in_table.variable_type.type == 'nvarchar':
                if var_in_table.variable_type.length < result.variable_type.length:
                    print("The length value is too long")
                    errors.append(self.semantic_error("The length value is too long"))
                    continue

                var_in_table.value = result.value
                continue

            if var_in_table.variable_type.type == 'date':
                if not re.search("\d{2}-\d{2}-\d{4}", result.value):
                    print('Date value was expected')
                    errors.append(self.semantic_error('Date value was expected'))
                    continue

                var_in_table.value = result.value
                continue

            if var_in_table.variable_type.type == 'datetime':
                if not re.search("\d{2}-\d{2}-\d{4} (\d{2}:\d{2}:\d{2}|\d{2}:\d{2})", result.value):
                    print('Datetime value was expected')
                    errors.append(self.semantic_error('Datetime value was expected'))
                    continue

                var_in_table.value = result.value
                continue

            if var_in_table.variable_type.type != result.variable_type.type:
                print("Variable type doesn't match")
                errors.append(self.semantic_error("Variable type doesn't match"))
                continue

            var_in_table.value = result.value

    def __str__(self):
        return f"SetStatement: assignments: {self.assignments}"

    def semantic_error(self, description):
        return xsql_error(description, '', 'Error Semantico', f'Linea {self.line} Columna {self.column}')

    def dot(self,nodo_padre, graficador):
        current_node = graficador.agregarNode('set')
        graficador.agregarRelacion(nodo_padre, current_node)
        for assignment in self.assignments:
            result: Variable = assignment
            if result is not None:
                node_equal = graficador.agregarNode('=')
                node_var = graficador.agregarNode(result.id)
                graficador.agregarRelacion(current_node, node_equal)
                graficador.agregarRelacion(node_equal,node_var)
                result.value.dot(node_equal,graficador)
    def c3d(self,scope):
        pass