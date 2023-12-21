from .Instruction import Instruction
from .symbolTable.SymbolTable import SymbolTable
from .Variable import Variable
from .VariableType import VariableType
from .SymbolType import SymbolType


class DeclareStatement(Instruction):

    def __init__(self, line, column, id: str, type: VariableType):
        super().__init__(line, column)
        self.type = type
        self.id = id

    def execute(self, symbol_table: SymbolTable, errors):
        var_in_table = symbol_table.find_var_by_id(self.id)
        if var_in_table is not None:
            print(f'The variable: {self.id} already exists')
            return None

        length = 0
        if isinstance(self.type.length, Instruction):
            result: Variable = self.type.length.execute(symbol_table, errors)

            if result is None:
                print('value cannot be set to the data type')
                return None

            if result.variable_type.type != 'int':
                print('int type was expected')
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

    def dot(self,nodo_padre, graficador):
        current_node = graficador.agregarNode('declare')
        graficador.agregarRelacion(nodo_padre, current_node)
        current_node_id = graficador.agregarNode(self.id)
        graficador.agregarRelacion(current_node, current_node_id)
        
    def c3d(self,scope):
        pass