def errors_to_matrix(errors: []):

    matriz = [["descripcion", "valor", "tipo", "fila"]]

    for error in errors:
        new_error = [error.descripcion, error.valor,
                     error.tipo, error.linea]
        matriz.append(new_error)
    return matriz





