from src.FILES.import_to_xml_ddl import *
from src.FILES.manager_db.record_file_manager import *
from compile import *

from compile import parsear


class Conector:

    def __init__(self):
        pass


    ### AQUI RECIBO EL CONTENIDO DEL EDITOR DE TEXTO DEL FRONT...
    def compilar(self, contenido):        
        matriz_resultante = parsear(contenido)

        return matriz_resultante

    def cargar_arbol(self,url):
        ''' Recibe el XML que contiene los datos de la base de datos y retorna un diccionario'''

        return self.construir_diccionario(url)



    ####TEST
    def construir_matriz_errores(self):
        matriz = [['descripcion', 'valor', 'tipo', 'fila'], ['Error sintactico', 'data', 'DATA', 0], ['Error sintactico', 'use', 'USE', 1], ['Error sintactico', 'into', 'INTO', 3]]
        return matriz

    def construir_diccionario(self,url):
        diccionario = xml_to_diccionario(url)
        return  diccionario
