from FILES.manager_db.record_file_manager import obtener_registros_tabla
from back.models.symbolTable.SymbolTable import SymbolTable
from back.utilities.utilities import errors_to_matrix

from back.grammar import *


matriz_errores = []
def parsear(contenido):
    inst = parse(contenido)

    if len(errores_sintacticos) > 0:
        print(errors_to_matrix(errores_sintacticos))
        matriz_errores = errors_to_matrix(errores_sintacticos)
        limpiar_lista_errores()
        return matriz_errores

    len_matriz = len(obtener_matriz_resultante())
    ### esta matriz se genera si no hay errores sintacticos, pueda que si existan errores semanticos
    ### devuelve tanto errores semanticos como resultados de ejecuciones correctas.
    if len(obtener_matriz_resultante())>0 :
        matriz_resultado = obtener_matriz_resultante()[len_matriz-1]
        return matriz_resultado
    print(obtener_db_en_uso())

    symbol_table = SymbolTable()
    for i in inst:
        if i is not None:
            i.execute(symbol_table)

    for symbol in symbol_table.symbols:
        print(symbol.id, symbol.variable_type.type, symbol.symbol_type, symbol.value)

    return [["encabezado"],["fila"]]

