from FILES.manager_db.record_file_manager import obtener_registros_tabla
from back.symbolTable.SymbolTable import SymbolTable
from back.utilities.utilities import errors_to_matrix

from back.grammar import *


def parsear(contenido):
    inst = parse(contenido)

    if len(errores_sintacticos) > 0:
        print(errors_to_matrix(errores_sintacticos))
        matriz_errores = errors_to_matrix(errores_sintacticos)
        limpiar_lista_errores()
        return matriz_errores

    symbol_table = SymbolTable()
    for i in inst:
        if i is not None:
            i.execute(symbol_table)

    for symbol in symbol_table.symbols:
        print(symbol.id, symbol.variable_type.type, symbol.symbol_type, symbol.value)
    matriz_registros = obtener_registros_tabla('escuela', 'usuario')
    return matriz_registros