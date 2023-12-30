from tkinter import Text
import re


class EditorTexto(Text):
    def __init__(self, pestana, xscrollcommand, yscrollcommand, wrap):
        super().__init__(pestana, xscrollcommand=xscrollcommand, yscrollcommand=yscrollcommand, wrap=wrap)
        self.__configurar_colores_palabras_reservadas__()
        self.bind("<KeyRelease>", self.__evento_escribir__)

    def insert(self, index, chars, *args):
        super().insert(index, chars)
        self.__aplicar_estilo_palabras_reservadas__(self.get(1.0, 'end-1c'))

    def __evento_escribir__(self, event):
        self.__aplicar_estilo_palabras_reservadas__(self.get(1.0, 'end-1c'))

    def __aplicar_estilo_palabras_reservadas__(self, text_content):
        self.__reset_colores_palabras_reservadas__()
        lineas = text_content.split("\n")
        numero_linea = 0
        palabras_reservadas=self.__litado_palabras_reservadas__()
        for linea in lineas:
            numero_linea += 1
            for palabra_reservada in palabras_reservadas:
                self.__aplicar_estilo_palabras_reservadas_por_linea__(palabra_reservada, linea.upper(), numero_linea)

    def __aplicar_estilo_palabras_reservadas_por_linea__(self, palabra_reservada, linea, numero_linea):
        indice_palabra_encontrada = 0
        while indice_palabra_encontrada != -1:
            indice_palabra_encontrada = linea.find(palabra_reservada[0], indice_palabra_encontrada)
            if indice_palabra_encontrada == -1:
                continue
            indice_inicial = indice_palabra_encontrada
            indice_final = indice_inicial + len(palabra_reservada[0])
            patron_caracteres_invalidos = re.compile("[0-9a-zA-Z]")
            siguiente_caracter_es_letra = patron_caracteres_invalidos.search(linea[indice_final:indice_final + 1])
            anterior_caracter_es_letra = patron_caracteres_invalidos.search(linea[indice_inicial - 1:indice_inicial])
            if not siguiente_caracter_es_letra and not anterior_caracter_es_letra:
                self.tag_add(palabra_reservada[1], str(numero_linea) + "." + str(indice_inicial),
                             str(numero_linea) + "." + str(indice_final))
            indice_palabra_encontrada = indice_final

    def __configurar_colores_palabras_reservadas__(self):
        """añade a la configuracion del widget text, los tags asociadios al listado de colores"""
        colores_palabras_reservadas = self.__obtener_colores_disponibles__()
        for color in colores_palabras_reservadas:
            self.tag_config(colores_palabras_reservadas[color], foreground=color)

    def __reset_colores_palabras_reservadas__(self):
        """quita el estilo aplicado al texto"""
        colores_palabras_reservadas = self.__obtener_colores_disponibles__()
        for color in colores_palabras_reservadas:
            self.tag_remove(colores_palabras_reservadas[color], "1.0", "end")

    def __obtener_colores_disponibles__(self):
        """listado de todos los colores disponibles, con su nombre de etiqueta"""
        return {
            "green": "marca_verde",
            "blue": "marca_azul",
            "red": "marca_roja",
            "orange": "marca_naranja",
        }

    def __litado_palabras_reservadas__(self):
        colores=self.__obtener_colores_disponibles__()

        return [
            ("CREATE",colores["blue"]),("create",colores["blue"]),
            ("USE", colores["blue"]),("use", colores["blue"]),
            ("ALTER", colores["blue"]),("alter", colores["blue"]),
            ("DROP", colores["blue"]),("drop", colores["blue"]),
            ("CASE", colores["green"]),("case", colores["green"]),
            ("COLUMN", colores["blue"]),("column", colores["blue"]),
            ("TRUNCATE", colores["blue"]),("truncate", colores["blue"]),
            ("EXEC", colores["green"]),("exec", colores["green"]),
            ("SELECT", colores["blue"]),("select", colores["blue"]),
            ("FROM", colores["blue"]),("from", colores["blue"]),
            ("WHERE", colores["blue"]),("where", colores["blue"]),
            ("UPDATE", colores["blue"]),("update", colores["blue"]),
            ("INSERT", colores["blue"]),("insert", colores["blue"]),
            ("INTO", colores["blue"]),("into", colores["blue"]),
            ("VALUES", colores["blue"]),("values", colores["blue"]),
            ("IF", colores["green"]),("if", colores["green"]),
            ("WHEN", colores["green"]),("when", colores["green"]),
            ("THEN", colores["green"]),("then", colores["green"]),
            ("ELSE", colores["green"]),("else", colores["green"]),
            ("DECLARE", colores["green"]),("declare", colores["green"]),
            ("FUNCTION", colores["green"]),("function", colores["green"]),
            ("AS", colores["green"]),("as", colores["green"]),
            ("BEGIN", colores["green"]),("begin", colores["green"]),
            ("END", colores["green"]),("end", colores["green"]),
            ("NOT", colores["blue"]),("not", colores["blue"]),
            ("NULL", colores["blue"]),("null", colores["blue"]),
            ("PRIMARY", colores["blue"]),("primary", colores["blue"]),
            ("KEY", colores["blue"]),("key", colores["blue"]),
            ("DATA", colores["blue"]),("data", colores["blue"]),
            ("BASE", colores["blue"]),("base", colores["blue"]),
            ("TABLE", colores["blue"]),("table", colores["blue"]),
            ("PROCEDURE", colores["green"]),("procedure", colores["green"]),
            ("REFERENCE", colores["blue"]),("reference", colores["blue"]),
            ("ADD", colores["blue"]),("add", colores["blue"]),
            ("INT", colores["orange"]),("int", colores["orange"]),
            ("DECIMAL", colores["orange"]),("decimal", colores["orange"]),
            ("DATE", colores["orange"]),("date", colores["orange"]),
            ("DATETIME", colores["orange"]),("datetime", colores["orange"]),
            ("NCHAR", colores["orange"]),("nchar", colores["orange"]),
            ("NVARCHAR", colores["orange"]),("nvarchar", colores["orange"]),
            ("CONCATENA", colores["green"]),("concatena", colores["green"]),
            ("SUBSTRAER", colores["green"]),("substraer", colores["green"]),
            ("HOY", colores["green"]),("hoy", colores["green"]),
            ("CONTAR", colores["green"]),("contar", colores["green"]),
            ("SUMA", colores["green"]),("suma", colores["green"]),
            ("CAS", colores["green"]),("cas", colores["green"]),
            ("SET", colores["green"]),("set", colores["green"]),
            ("WHILE", colores["green"]),("while", colores["green"]),
            ("DELETE", colores["green"]),("delete", colores["green"])
        ]
