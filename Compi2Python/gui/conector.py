from src.FILES.import_to_xml_ddl import *
from src.FILES.manager_db import db_file_manager
from src.FILES.manager_db.record_file_manager import *
from compile import *

from compile import parsear


class Conector:

    def __init__(self):
        pass


    ### AQUI RECIBO EL CONTENIDO DEL EDITOR DE TEXTO DEL FRONT...
    def compilar(self, contenido):        
        matriz_resultante = parsear(contenido)
        limpiar_lista_errores()
        return matriz_resultante

    def cargar_arbol(self,url):
        ''' Recibe el XML que contiene los datos de la base de datos y retorna un diccionario'''

        return self.construir_diccionario(url)



    ####TEST
    def construir_matriz_errores(self):
        matriz = [['descripcion', 'valor', 'tipo', 'fila'], ['Error sintactico', 'data', 'DATA', 0], ['Error sintactico', 'use', 'USE', 1], ['Error sintactico', 'into', 'INTO', 3]]
        return matriz

    def construir_diccionario(self,url):
        return xml_to_diccionario(url)


    def eliminar_bbdd(self,nombre_bbdd):
        try:
            db_file_manager.eliminar_base_de_datos(nombre_bbdd)
            return True
        except:
            return False
