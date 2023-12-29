from .Instruction import Instruction
from .symbolTable.SymbolTable import SymbolTable
from .Variable import Variable
from .SymbolType import SymbolType

from ..error.xsql_error import xsql_error


class Assignment(Instruction):

    def __init__(self, line, column, id: str, value: Instruction):
        super().__init__(line, column)
        self.id = id
        self.value = value

    def execute(self, symbol_table: SymbolTable, errors):
        result = Variable()
        result.id = self.id
        result_val: Variable = self.value.execute(symbol_table, errors)

        if result_val is None:
            print('A value was expected')
            errors.append(self.semantic_error('A value was expected'))
            return None

        result.value = result_val.value
        if "@" in self.id:
            result.symbol_type = SymbolType().VARIABLE
        else:
            result.symbol_type = SymbolType().COLUMN
        result.variable_type = result_val.variable_type

        return result

    def semantic_error(self, description):
        return xsql_error(description, '', 'Error Semantico', f'Linea {self.line} Columna {self.column}')

    def dot(self, nodo_padre, graficador):
        current_node = graficador.agregarNode("=")
        graficador.agregarRelacion(nodo_padre, current_node)
        id_node = graficador.agregarNode(self.id)
        graficador.agregarRelacion(current_node, id_node)
        if self.value is not None:
            self.value.dot(current_node, graficador)

    def c3d(self, symbol_table, generador):
        generador.add_comment(f"Inicia Asignacion {self.id}")
        result = None
        if self.value is not None:
            result = self.value.c3d(symbol_table, generador)
            if isinstance(result, Exception):
                return result
        variable = symbol_table.find_var_by_id(self.id)
        # Variables temporales de manejo de punteros
        temp_pos1 = variable.pos
        temp_pos2 = variable.pos
        # obtenemos si es una variable global o local
        is_global = symbol_table.is_global_var(self.id)
        if not is_global:
            temp_pos1 = generador.add_temp()
            generador.add_exp(temp_pos1, 'P', temp_pos2, '+')
        if result is not None:
            generador.set_stack(temp_pos1, result.value)
        else:
            generador.set_stack(temp_pos1, 0)
        generador.add_comment(f'Finaliza Asignacion {self.id}')
