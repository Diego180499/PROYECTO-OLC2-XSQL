from os import *

from FILES.BaseDatos import BaseDatos
from FILES.Campo import Campo
from FILES.Tabla import Tabla
from FILES.import_to_xml_ddl import xml_to_base_de_datos
from utils.archivo import Archivo
from db_to_xml import data_base_to_xml


url_base_de_datos_xml = f'resources/BASES_DE_DATOS_XML'
def eliminar_base_de_datos(nombre_base_de_datos):
    remove(f'{url_base_de_datos_xml}/{nombre_base_de_datos}.xml')


def guardar_base_de_datos_xml(nombre_base_de_datos, base_de_datos : BaseDatos):
    archivo : Archivo = Archivo(f'{url_base_de_datos_xml}/{nombre_base_de_datos}.xml')
    contenido = data_base_to_xml(base_de_datos)
    archivo.guardar(contenido)




def obtener_base_de_datos(nombre_bd):
    base_de_datos : BaseDatos = xml_to_base_de_datos(f'{url_base_de_datos_xml}/{nombre_bd}.xml')
    return base_de_datos


# eliminar tabla: parametros: ( nombre base de datos  ,  nombre tabla )
def eliminar_tabla(nombre_bd, nombre_tabla):
    base_de_datos : BaseDatos = obtener_base_de_datos(nombre_bd)

    for tabla in base_de_datos.tablas :
        if nombre_tabla == tabla.nombre :
            base_de_datos.tablas.remove(tabla)

    guardar_base_de_datos_xml(base_de_datos.nombre, base_de_datos)


## agregar una columna a una tabla
## necesitamos: nombre base de datos, nombre tabla, objeto Campo para añadirlo al array de campos de
# una tabla.

def agregar_columna(nombre_base_de_datos, nombre_tabla, campo : Campo):
    base_de_datos : BaseDatos = obtener_base_de_datos(nombre_base_de_datos)

    indice = 0
    while indice < len(base_de_datos.tablas) :
        tabla : Tabla = base_de_datos.tablas[indice]
        if tabla.nombre == nombre_tabla :
            base_de_datos.tablas[indice].campos.append(campo)
        indice += 1
    guardar_base_de_datos_xml(base_de_datos.nombre, base_de_datos)


# eliminar campo:  parametros: ( nombre base de datos  ,  nombre tabla, nombre campo )
def eliminar_columna(nombre_base_de_datos, nombre_tabla, nombre_campo):
    base_de_datos : BaseDatos = obtener_base_de_datos(nombre_base_de_datos)

    indice = 0
    while indice < len(base_de_datos.tablas) :
        tabla : Tabla = base_de_datos.tablas[indice]
        if tabla.nombre == nombre_tabla :
            __eliminar_campo_2(base_de_datos.tablas[indice], nombre_campo)
        indice += 1
    guardar_base_de_datos_xml(base_de_datos.nombre, base_de_datos)

def __eliminar_campo_2(tabla: Tabla, nombre_campo):

    for campo in tabla.campos :
        if campo.nombre == nombre_campo:
            tabla.campos.remove(campo)



