from os import *

from FILES.BaseDatos import BaseDatos
from FILES.Campo import Campo
from FILES.Tabla import Tabla
from FILES.import_to_xml_ddl import *
from FILES.manager_db.db_to_xml import data_base_to_xml
from utils.archivo import Archivo

url_base_de_datos_xml = f'U:/Universidad/Ciclo 2023/EDV-DICIEMBRE/LAB - OLC2/REPO-PROYECTO-OLC2-XSQL/PROYECTO-OLC2/resources/BASES_DE_DATOS_XML'
def eliminar_base_de_datos(nombre_base_de_datos):
    remove(f'{url_base_de_datos_xml}/{nombre_base_de_datos}.xml')


def guardar_base_de_datos_xml(nombre_base_de_datos, base_de_datos : BaseDatos):
    archivo : Archivo = Archivo(f'{url_base_de_datos_xml}/{nombre_base_de_datos}.xml')
    contenido = data_base_to_xml(base_de_datos)
    archivo.guardar(contenido)


def obtener_base_de_datos(nombre_bd):
    base_de_datos : BaseDatos = xml_to_base_de_datos(f'{url_base_de_datos_xml}/{nombre_bd}.xml')
    return base_de_datos


def obtener_nombres_de_bases_de_datos():
    nombres_bases_de_datos : [] = listdir(f'{url_base_de_datos_xml}')
    print(nombres_bases_de_datos)
    return nombres_bases_de_datos

####### ACCIONES DE UNA TABLA   #######

# eliminar tabla: parametros: ( nombre base de datos  ,  nombre tabla )
def eliminar_tabla(nombre_bd, nombre_tabla):
    base_de_datos : BaseDatos = obtener_base_de_datos(nombre_bd)

    for tabla in base_de_datos.tablas :
        if nombre_tabla == tabla.nombre :
            base_de_datos.tablas.remove(tabla)

    guardar_base_de_datos_xml(base_de_datos.nombre, base_de_datos)


def crear_tabla(nombre_bd, tabla:Tabla):
    base_de_datos: BaseDatos = obtener_base_de_datos(nombre_bd)

    base_de_datos.tablas.append(tabla)

    guardar_base_de_datos_xml(base_de_datos.nombre, base_de_datos)


### devuelve los nombres de las tablas de una bd
def obtener_tablas_de_bd(nombre_bd):
    base_datos : BaseDatos = obtener_base_de_datos(nombre_bd)
    nombres_tablas : [] = []

    for tabla in base_datos.tablas :
        nombres_tablas.append(tabla.nombre)

    return nombres_tablas


def obtener_tabla(nombre_bd, nombre_tabla):
    base_datos : BaseDatos = obtener_base_de_datos(nombre_bd)
    tablas : [] = base_datos.tablas

    for tabla in tablas :
        if tabla.nombre == nombre_tabla :
            return tabla

    return None

## agregar una columna a una tabla
## necesitamos: nombre base de datos, nombre tabla, objeto Campo para añadirlo al array de campos de
# una tabla.

def agregar_campo_tabla(nombre_base_de_datos, nombre_tabla, campo : Campo):
    base_de_datos : BaseDatos = obtener_base_de_datos(nombre_base_de_datos)

    indice = 0
    while indice < len(base_de_datos.tablas) :
        tabla : Tabla = base_de_datos.tablas[indice]
        if tabla.nombre == nombre_tabla :
            base_de_datos.tablas[indice].campos.append(campo)
        indice += 1
    guardar_base_de_datos_xml(base_de_datos.nombre, base_de_datos)


# eliminar campo:  parametros: ( nombre base de datos  ,  nombre tabla, nombre campo )
def eliminar_campo(nombre_base_de_datos, nombre_tabla, nombre_campo):
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


## devuelve un array con los nombres de los campos de una tabla.
def obtener_campos_tabla(nombre_bd, nombre_tabla):
    tabla : Tabla = obtener_tabla(nombre_bd, nombre_tabla)
    campos_tabla : [] = []

    for campo in tabla.campos :
        campos_tabla.append(campo.nombre)
    return campos_tabla
