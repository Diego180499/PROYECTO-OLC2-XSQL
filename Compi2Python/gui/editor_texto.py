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
                self.__aplicar_estilo_palabras_reservadas_por_linea__(palabra_reservada, linea, numero_linea)

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
            ("CREATE",colores["blue"]),
            ("USE", colores["blue"]),
            ("ALTER", colores["blue"]),
            ("DROP", colores["blue"]),
            ("case", colores["green"]),
            ("COLUMN", colores["blue"]),
            ("TRUNCATE", colores["blue"]),
            ("exec", colores["green"]),
            ("SELECT", colores["blue"]),
            ("FROM", colores["blue"]),
            ("WHERE", colores["blue"]),
            ("UPDATE", colores["blue"]),
            ("INSERT", colores["blue"]),
            ("INTO", colores["blue"]),
            ("VALUES", colores["blue"]),
            ("if", colores["green"]),
            ("when", colores["green"]),
            ("then", colores["green"]),
            ("else", colores["green"]),
            ("declare", colores["green"]),
            ("function", colores["green"]),
            ("as", colores["green"]),
            ("begin", colores["green"]),
            ("end", colores["green"]),
            ("NOT", colores["blue"]),
            ("NULL", colores["blue"]),
            ("PRIMARY", colores["blue"]),
            ("KEY", colores["blue"]),
            ("DATA", colores["blue"]),
            ("BASE", colores["blue"]),
            ("TABLE", colores["blue"]),
            ("procedure", colores["green"]),
            ("REFERENCE", colores["blue"]),
            ("ADD", colores["blue"]),
            ("int", colores["orange"]),
            ("decimal", colores["orange"]),
            ("date", colores["orange"]),
            ("datetiem", colores["orange"]),
            ("nchar", colores["orange"]),
            ("nvarchar", colores["orange"]),
            ("concatena", colores["green"]),
            ("substraer", colores["green"]),
            ("hoy", colores["green"]),
            ("contar", colores["green"]),
            ("suma", colores["green"]),
            ("cas", colores["green"]),
            ("set", colores["green"]),
            ("while", colores["green"]),
            ("DELETE", colores["green"])
        ]
