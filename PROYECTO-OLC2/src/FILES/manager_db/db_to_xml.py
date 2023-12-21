from src.FILES.BaseDatos import BaseDatos
from src.FILES.Campo import Campo
from src.FILES.Tabla import Tabla


######## ESCRITURA DE UN ARCHIVO XML CON LA ESTRUCTURA DE UNA BASE DE DATOS   ###########
def data_base_to_xml(base_datos : BaseDatos):
    contenidoTablas = tablas_to_xml(base_datos.tablas)
    contenido = f'''
        <base>
            <nombre>{base_datos.nombre}</nombre>
            {contenidoTablas}
        </base>        
    '''
    return contenido

def campos_to_xml(campos : Campo = []):
    contenidoCampos = ""

    for campo in campos :
        contenidoCampos+= f'''
        <campo>
            <nombre>{campo.nombre}</nombre>
            <tipo_dato>{campo.tipoDato}</tipo_dato>
            <llave_primaria>{campo.llavePrim}</llave_primaria>
            <nulo>{campo.nulo}</nulo>
            <tabla_referencia>{campo.tablaRef}</tabla_referencia>
            <campo_referencia>{campo.campoRef}</campo_referencia>
        </campo>
        '''
    return contenidoCampos


def tablas_to_xml(tablas : Tabla = []):

    contenidoTablas = ""

    for tabla in tablas :
        contenidoCampos = campos_to_xml(tabla.campos)
        contenidoTablas += f'''
        <tabla>
            <nombre>{tabla.nombre}</nombre>
            {contenidoCampos}
        </tabla>
        '''
    return contenidoTablas

######## FIN ESCRITURA ###########

