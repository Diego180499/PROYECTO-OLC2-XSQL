from .Instruction import Instruction
from .symbolTable.SymbolTable import SymbolTable
from .Variable import Variable
from .VariableType import VariableType
from .SymbolType import SymbolType
from ..error.xsql_error import xsql_error


class DeclareStatement(Instruction):

    def __init__(self, line, column, id: str, type: VariableType):
        super().__init__(line, column)
        self.type = type
        self.id = id

    def execute(self, symbol_table: SymbolTable, errors):
        var_in_table = symbol_table.find_var_by_id(self.id)
        if var_in_table is not None:
            print(f'The variable: {self.id} already exists')
            errors.append(self.semantic_error(f'The variable: {self.id} already exists'))
            return None

        length = 0
        if isinstance(self.type.length, Instruction):
            result: Variable = self.type.length.execute(symbol_table, errors)

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
            length = int(self.type.length)

        result = Variable()
        result.variable_type = VariableType(self.type.type, length)
        result.symbol_type = SymbolType().VARIABLE
        result.id = self.id

        if self.type.type == 'int' or self.type.type == 'decimal':
            result.value = 0
        elif self.type.type == 'nvarchar' or self.type.type == 'nchar':
            result.value = ''
        elif self.type.type == 'date':
            result.value = '12-12-2000'
        elif self.type.type == 'datetime':
            result.value = '12-12-2000 23:00:00'

        symbol_table.add_variable(result)

    def __str__(self):
        return f"DeclareStatement: id: {self.id}, tipo: {self.type.type}"

    def semantic_error(self, description):
        return xsql_error(description, '', 'Error Semantico', f'Linea {self.line} Columna {self.column}')

    def dot(self, nodo_padre, graficador):
        current_node = graficador.agregarNode('declare')
        graficador.agregarRelacion(nodo_padre, current_node)
        current_node_id = graficador.agregarNode(self.id)
        graficador.agregarRelacion(current_node, current_node_id)

    def c3d(self, symbol_table, generador):
        generador.add_comment(f'Declaracion de variable {self.id}')
        var_in_table = symbol_table.find_var_by_id(self.id)
        if var_in_table is not None:
            print(f'The variable: {self.id} already exists')
            return None
        # Generamos la variable
        variable = Variable()
        variable.variable_type = VariableType(self.type.type, 0)
        variable.symbol_type = SymbolType().VARIABLE
        variable.id = self.id
        # Obtenemos el size del stack del generador
        pos = generador.count_temp
        # Asignamos la posicion a la variable de su pos en el stack
        variable.pos = str(pos)[:]
        # Agregamos el valor por defecto
        if self.type.type == 'int' or self.type.type == 'decimal':
            variable.value = 0
        elif self.type.type == 'nvarchar' or self.type.type == 'nchar':
            variable.value = ''
        elif self.type.type == 'date':
            variable.value = '12-12-2000'
        elif self.type.type == 'datetime':
            variable.value = '12-12-2000 23:00:00'
        # Guardamos la variable en la tabla de simbolos
        symbol_table.add_variable(variable)
        # Agregamos los parametros para c3d
        # Verificamos si es global o local
        is_global = symbol_table.is_global_var(self.id)
        # Guardamos la posicion del stack de la variable
        temp_pos1 = variable.pos
        temp_pos2 = variable.pos
        if not is_global:
            temp_pos1 = generador.add_temp()
            generador.add_exp(temp_pos1, 'P', temp_pos2, "+")
        generador.set_stack(temp_pos1, variable.value)
        generador.add_comment(f'Fin declaracion de variable {self.id}')
