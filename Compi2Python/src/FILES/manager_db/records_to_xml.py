from src.FILES.import_to_xml_dml import *


def records_to_xml(registros: Registros):
    string_registros = ''
    tabs_children = "\t"
    for registro in registros.registros:
        string_registros += record_to_xml(tabs_children, registro.campos, registro.valores)

    contenido_registros = f'<registros>\n'
    contenido_registros += f'{tabs_children}<base_datos>{registros.baseDatos}</base_datos>\n'
    contenido_registros += f'{tabs_children}<tabla>{registros.tabla}</tabla>\n'
    contenido_registros += f'{string_registros}'
    contenido_registros += f'</registros>\n'
    return contenido_registros


def record_to_xml(tabs, campos: [], valores: []):
    tabs_children = tabs + "\t"
    contenido_registro = f'{tabs}<registro>\n'
    contenido_registro += f'{campos_to_xml(tabs_children, campos)}'
    contenido_registro += f'{valores_to_xml(tabs_children, valores)}'
    contenido_registro += f'{tabs}</registro>\n'
    return contenido_registro


def campos_to_xml(tabs, campos: []):
    if campos is None:
        campos = []

    contenido_campos = ""
    for campo in campos:
        contenido_campos += f'{tabs}<campo>{campo}</campo>\n'
    return contenido_campos


def valores_to_xml(tabs, valores: []):
    if valores is None:
        valores = []

    contenido_valores = ""

    for valor in valores:
        contenido_valores += f'{tabs}<valor>{valor}</valor>\n'
    return contenido_valores
