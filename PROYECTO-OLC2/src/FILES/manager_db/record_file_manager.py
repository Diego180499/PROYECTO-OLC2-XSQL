from src.FILES.manager_db.records_to_xml import *
from src.utils.archivo import Archivo

url_records_xml = f'U:/Universidad/Ciclo 2023/EDV-DICIEMBRE/LAB - OLC2/REPO-PROYECTO-OLC2-XSQL/PROYECTO-OLC2/resources/REGISTROS_XML'

def obtener_registros_tabla(nombre_db, nombre_tabla):
    registros : Registros = xml_to_records(f'{url_records_xml}/{nombre_db}/{nombre_tabla}.xml')
    matriz_registros = registros.matriz()
    return matriz_registros

### se obtienen los registros de una tabla como un listado de BOJETOS DE TIPO REGISTRO
def obtener_registros_tabla_2(nombre_db, nombre_tabla):
    registros : Registros = xml_to_records(f'{url_records_xml}/{nombre_db}/{nombre_tabla}.xml')

    registro_lista = []

    for registro in registros.registros :
        registro_lista.append(registro)

    return registro_lista



def insertar_registro(nombre_db, nombre_tabla, registro : Registro):

    try:
        registros: Registros = xml_to_records(f'{url_records_xml}/{nombre_db}/{nombre_tabla}.xml')
        registros.registros.append(registro)
        registros_xml = records_to_xml(registros)
        archivo: Archivo = Archivo(f'{url_records_xml}/{nombre_db}/{nombre_tabla}.xml')
        archivo.guardar(registros_xml)
        print(registros_xml)
    except UnboundLocalError as ule :
        registros: Registros = Registros(nombre_db,nombre_tabla,[])
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



