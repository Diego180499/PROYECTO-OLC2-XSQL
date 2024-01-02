def obtener_colores_disponibles():
    """listado de todos los colores disponibles, con su nombre de etiqueta"""
    return {
        "green": "marca_verde",
        "blue": "marca_azul",
        "red": "marca_roja",
        "orange": "marca_naranja",
    }


def litado_palabras_reservadas():
    colores = obtener_colores_disponibles()

    return [
        ("CREATE", colores["blue"]), ("create", colores["blue"]),
        ("USE", colores["blue"]), ("use", colores["blue"]),
        ("ALTER", colores["blue"]), ("alter", colores["blue"]),
        ("DROP", colores["blue"]), ("drop", colores["blue"]),
        ("CASE", colores["green"]), ("case", colores["green"]),
        ("COLUMN", colores["blue"]), ("column", colores["blue"]),
        ("TRUNCATE", colores["blue"]), ("truncate", colores["blue"]),
        ("EXEC", colores["green"]), ("exec", colores["green"]),
        ("SELECT", colores["blue"]), ("select", colores["blue"]),
        ("FROM", colores["blue"]), ("from", colores["blue"]),
        ("WHERE", colores["blue"]), ("where", colores["blue"]),
        ("UPDATE", colores["blue"]), ("update", colores["blue"]),
        ("INSERT", colores["blue"]), ("insert", colores["blue"]),
        ("INTO", colores["blue"]), ("into", colores["blue"]),
        ("VALUES", colores["blue"]), ("values", colores["blue"]),
        ("IF", colores["green"]), ("if", colores["green"]),
        ("WHEN", colores["green"]), ("when", colores["green"]),
        ("THEN", colores["green"]), ("then", colores["green"]),
        ("ELSE", colores["green"]), ("else", colores["green"]),
        ("DECLARE", colores["green"]), ("declare", colores["green"]),
        ("FUNCTION", colores["green"]), ("function", colores["green"]),
        ("AS", colores["green"]), ("as", colores["green"]),
        ("BEGIN", colores["green"]), ("begin", colores["green"]),
        ("END", colores["green"]), ("end", colores["green"]),
        ("NOT", colores["blue"]), ("not", colores["blue"]),
        ("NULL", colores["blue"]), ("null", colores["blue"]),
        ("PRIMARY", colores["blue"]), ("primary", colores["blue"]),
        ("KEY", colores["blue"]), ("key", colores["blue"]),
        ("DATA", colores["blue"]), ("data", colores["blue"]),
        ("BASE", colores["blue"]), ("base", colores["blue"]),
        ("TABLE", colores["blue"]), ("table", colores["blue"]),
        ("PROCEDURE", colores["green"]), ("procedure", colores["green"]),
        ("REFERENCE", colores["blue"]), ("reference", colores["blue"]),
        ("ADD", colores["blue"]), ("add", colores["blue"]),
        ("INT", colores["orange"]), ("int", colores["orange"]),
        ("DECIMAL", colores["orange"]), ("decimal", colores["orange"]),
        ("DATE", colores["orange"]), ("date", colores["orange"]),
        ("DATETIME", colores["orange"]), ("datetime", colores["orange"]),
        ("NCHAR", colores["orange"]), ("nchar", colores["orange"]),
        ("NVARCHAR", colores["orange"]), ("nvarchar", colores["orange"]),
        ("CONCATENA", colores["green"]), ("concatena", colores["green"]),
        ("SUBSTRAER", colores["green"]), ("substraer", colores["green"]),
        ("HOY", colores["green"]), ("hoy", colores["green"]),
        ("CONTAR", colores["green"]), ("contar", colores["green"]),
        ("SUMA", colores["green"]), ("suma", colores["green"]),
        ("CAS", colores["green"]), ("cas", colores["green"]),
        ("SET", colores["green"]), ("set", colores["green"]),
        ("WHILE", colores["green"]), ("while", colores["green"]),
        ("DELETE", colores["green"]), ("delete", colores["green"])
    ]
