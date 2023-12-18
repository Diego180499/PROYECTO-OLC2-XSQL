from FILES.Registro import Registro
from FILES.Registros import Registros
from FILES.import_to_xml_dml import *
from utils.archivo import *


def records_to_xml(registros : Registros):
    string_registros = ''
    for registro in registros.registros :
        string_registros += record_to_xml(registro.campos,registro.valores)

    contenido_registros = f'''
    <registros>
        <base_datos>{registros.baseDatos}</base_datos>        
        <tabla>{registros.tabla}</tabla>
        {string_registros}
    </registros>
    '''
    return contenido_registros


def record_to_xml(campos : [] , valores : []):
    contenido_registro = f'''
        <registro>
            {campos_to_xml(campos)}
            {valores_to_xml(valores)}
        </registro>                    
    '''
    return contenido_registro


def campos_to_xml(campos : []):
    contenido_campos = f''

    for campo in campos :
        contenido_campos+=f'''
        <campo>{campo}</campo>
        '''
    return contenido_campos


def valores_to_xml(valores : []):

    contenido_valores = f''

    for valor in valores :
        contenido_valores += f'''
        <valor>{valor}</valor>
        '''
    return contenido_valores