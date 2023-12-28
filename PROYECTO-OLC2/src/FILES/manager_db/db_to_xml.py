from src.FILES.BaseDatos import BaseDatos
from src.FILES.Campo import Campo
from src.FILES.Procedimiento import Procedimiento
from src.FILES.Tabla import Tabla


######## ESCRITURA DE UN ARCHIVO XML CON LA ESTRUCTURA DE UNA BASE DE DATOS   ###########
def data_base_to_xml(base_datos: BaseDatos):
    tabs="\t"
    contenido = f'<base>\n'
    contenido+=f'{tabs}<nombre>{base_datos.nombre}</nombre>\n'
    contenido+=f'{tablas_to_xml(tabs,base_datos.tablas)}'
    contenido+=f'{procedimientos_to_xml(tabs,base_datos.procedimientos)}'
    contenido+=f'</base>'

    return contenido


def campos_to_xml(tabs,campos=None):
    if campos is None:
        campos = []
    contenidoCampos = ""
    for campo in campos:
        contenidoCampos +=  f'{tabs}<campo>\n'
        contenidoCampos +=  f'{tabs}\t<nombre>{campo.nombre}</nombre>\n'
        contenidoCampos +=  f'{tabs}\t<tipo_dato>{campo.tipoDato}</tipo_dato>\n'
        contenidoCampos +=  f'{tabs}\t<llave_primaria>{campo.llavePrim}</llave_primaria>\n'
        contenidoCampos +=  f'{tabs}\t<nulo>{campo.nulo}</nulo>\n'
        contenidoCampos +=  f'{tabs}\t<tabla_referencia>{campo.tablaRef}</tabla_referencia>\n'
        contenidoCampos +=  f'{tabs}\t<campo_referencia>{campo.campoRef}</campo_referencia>\n'
        contenidoCampos +=  f'{tabs}</campo>\n'
    return contenidoCampos


def tablas_to_xml(tabs, tablas=None):
    if tablas is None:
        tablas = []
    contenidoTablas = ""

    tabs_children=tabs+"\t"
    for tabla in tablas:
        contenidoTablas += f'{tabs}<tabla>\n'
        contenidoTablas += f'{tabs}\t<nombre>{tabla.nombre}</nombre>\n'
        contenidoTablas += f'{campos_to_xml(tabs_children,tabla.campos)}'
        contenidoTablas += f'{tabs}</tabla>\n'
    return contenidoTablas


def procedimientos_to_xml(tabs, procedimientos=None):  ### agregar al back
    if procedimientos is None:
        procedimientos = []
    contenido_procedimientos = f''
    for procedimiento in procedimientos:
        contenido_procedimientos += f'{tabs}<procedimiento>\n'
        contenido_procedimientos += f'{tabs}\t<nombre>{procedimiento.nombre}</nombre>\n'
        contenido_procedimientos += f'{tabs}</procedimiento>\n'
    return contenido_procedimientos

######## FIN ESCRITURA ###########
