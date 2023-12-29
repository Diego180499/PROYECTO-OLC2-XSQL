from .Instruction import Instruction
from .symbolTable.SymbolTable import SymbolTable
from .symbolTable.ScopeType import ScopeType
from .Variable import Variable
from ..error.xsql_error import xsql_error


class IfStatement(Instruction):

    def __init__(self, line, column, condition, true_block: Instruction, false_block: Instruction):
        super().__init__(line, column)
        self.condition = condition
        self.true_block = true_block
        self.false_block = false_block

    def execute(self, symbol_table: SymbolTable, errors):
        result: Variable = self.condition.execute(symbol_table, errors)

        if result is None:
            print("The condition didn't return anything")
            errors.append(self.semantic_error("The condition didn't return anything"))
            return None

        if result.variable_type.type != 'int':
            print("Only can use int type into conditions")
            errors.append(self.semantic_error("Only can use int type into conditions"))
            return None

        symbol_table = SymbolTable(ScopeType().IF, symbol_table)
        if result.value > 0:

            true_result = self.true_block.execute(symbol_table, errors)
            if true_result is not None:
                symbol_table = symbol_table.parent
                return true_result

        else:
            if self.false_block is None:
                symbol_table = symbol_table.parent
                return None
            false_result = self.false_block.execute(symbol_table, errors)
            if false_result is not None:
                symbol_table = symbol_table.parent
                return false_result

        symbol_table = symbol_table.parent

    def __str__(self):
        return f"""{{"IfStatement": {self.condition}, {self.true_block}, {self.false_block} }}"""

    def semantic_error(self, description):
        return xsql_error(description, '', 'Error Semantico', f'Linea {self.line} Columna {self.column}')

    def dot(self, nodo_padre, graficador):
        current_node = graficador.agregarNode("if")
        graficador.agregarRelacion(nodo_padre, current_node)
        condition_node = graficador.agregarNode("condition")
        graficador.agregarRelacion(current_node, condition_node)
        self.condition.dot(condition_node, graficador)
        if self.true_block is not None:
            true_node = graficador.agregarNode("true_code")
            graficador.agregarRelacion(current_node, true_node)
            self.true_block.dot(true_node, graficador)
        if self.false_block is not None:
            self.false_block.dot(current_node, graficador)

    def c3d(self, symbol_table, generador):
        symbol_table = SymbolTable(ScopeType().IF, symbol_table)
        generador.add_comment('If Statement')
        exit_label = generador.new_label()
        condicion = self.condition.c3d(symbol_table, generador)
        for label in condicion.true_labels:
            generador.put_label(label)
        if self.true_block is not None:
            self.true_block.c3d(symbol_table, generador)
        generador.add_goto(exit_label)
        for label in condicion.false_labels:
            generador.put_label(label)
        if self.false_block is not None:
            self.false_block.c3d(symbol_table, generador)
        generador.put_label(exit_label)
        generador.add_comment('End If Statement')
