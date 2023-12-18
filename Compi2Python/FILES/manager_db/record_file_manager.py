from FILES.import_to_xml_dml import *
from FILES.manager_db.records_to_xml import *
from utils.archivo import Archivo

url_records_xml = f'resources/REGISTROS_XML'

def obtener_registros_tabla(nombre_db, nombre_tabla):
    registros : Registros = xml_to_records(f'{url_records_xml}/{nombre_db}/{nombre_tabla}.xml')
    matriz_registros = registros.matriz()
    return matriz_registros


def insertar_registro(nombre_db, nombre_tabla, registro : Registro):
    registros: Registros = xml_to_records(f'{url_records_xml}/{nombre_db}/{nombre_tabla}.xml')
    registros.registros.append(registro)
    registros_xml = records_to_xml(registros)
    archivo: Archivo = Archivo(f'{url_records_xml}/{nombre_db}/{nombre_tabla}.xml')
    archivo.guardar(registros_xml)
    print(registros_xml)


## eliminar registros: se recibe como parametro una lista de objetos REGISTRO, ya que en la lista puede venir uno o varios
## objetos REGISTRO que deseamos eliminar de una lista.
def eliminar_registro(nombre_db, nombre_tabla, lista_registros_a_eliminar : Registro = []):
    registros: Registros = xml_to_records(f'{url_records_xml}/{nombre_db}/{nombre_tabla}.xml')
    registros_actuales = registros.registros

    for registro_a_eliminar in lista_registros_a_eliminar :
        eliminar_registro_individual(registros_actuales, registro_a_eliminar)

    registros_xml = records_to_xml(registros)
    archivo: Archivo = Archivo(f'{url_records_xml}/{nombre_db}/{nombre_tabla}.xml')
    archivo.guardar(registros_xml)

def eliminar_registro_individual(registros_actuales : Registro = [], registro_a_eliminar : Registro = None):
    for registro_actual in registros_actuales :
        if registro_actual.valores == registro_a_eliminar.valores :
            registros_actuales.remove(registro_actual)



