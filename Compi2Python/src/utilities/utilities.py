from src.models.symbolTable.SymbolTable import SymbolTable


def errors_to_matrix(errors: []):

    matriz = [["descripcion", "valor", "tipo", "fila"]]

    for error in errors:
        new_error = [error.descripcion, error.valor,
                     error.tipo, error.linea]
        matriz.append(new_error)
    return matriz

def tabla_simbolos_a_matriz(tabla_simbolos : SymbolTable):
    matriz = []
    variables = tabla_simbolos.symbols
    encabezados = ['id','tipo simbolo','valor','longitud','tipo de dato']
    matriz.append(encabezados)

    for variable in variables :
        fila = [variable.id, variable.symbol_type, variable.value, variable.variable_type.length, variable.variable_type.type]
        matriz.append(fila)

    return matriz

def tabla_select_a_matriz(tabla_result):
    matriz_select = []
    encabezados = tabla_result[0]
    matriz_select.append(encabezados)

    filas = tabla_result[1]

    for fila in filas :
        matriz_select.append(fila)

    return matriz_select



