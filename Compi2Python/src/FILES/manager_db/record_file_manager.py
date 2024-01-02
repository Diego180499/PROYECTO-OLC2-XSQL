from src.FILES.manager_db.records_to_xml import *
from src.utils.archivo import Archivo
from shutil import rmtree
import os

#url_records_xml = f'U:/Universidad/Ciclo 2023/EDV-DICIEMBRE/LAB - OLC2/REPO-PROYECTO-OLC2-XSQL/PROYECTO-OLC2/resources/REGISTROS_XML'
#url_records_xml = f'/home/isaac/Escritorio/2023/compi2/back/PROYECTO-OLC2-XSQL/PROYECTO-OLC2/resources/REGISTROS_XML'

project_path=os.path.abspath(os.path.dirname(__file__)).split("Compi2Python")[0]
url_records_xml =   resources_path=os.path.join(project_path,"Compi2Python","resources","REGISTROS_XML")

def obtener_matriz_registros_de_tabla(nombre_db, nombre_tabla):
    registros : Registros = xml_to_records(f'{url_records_xml}/{nombre_db}/{nombre_tabla}.xml')
    matriz_registros = registros.matriz()
    return matriz_registros

### se obtienen los registros de una tabla como un listado de OBJETOS DE TIPO REGISTRO
def obtener_registros_tabla_2(nombre_db, nombre_tabla):
    registros : Registros = xml_to_records(f'{url_records_xml}/{nombre_db}/{nombre_tabla}.xml')

    registro_lista = []

    for registro in registros.registros :
        registro_lista.append(registro)

    return registro_lista

def obtener_contenido_registros_tabla(nombre_bd, nombre_tabla):
    archivo = open(f'{url_records_xml}/{nombre_bd}/{nombre_tabla}.xml','r')

    if archivo.readable() :
        return archivo.read()

    return None


## unir dos o mas tablas para un select

def obtener_registros_de_varias_tablas(nombre_bd, nombres_tablas : []):
    matrices_registros = []
    matriz_resultante = []
    ## llenamos el arreglo de matrices segun la cantidad de tablas solicitadas
    for nombre_tabla in nombres_tablas :
        matriz = obtener_matriz_registros_de_tabla(nombre_bd, nombre_tabla)
        matrices_registros.append(matriz)

    encabezados_resultantes = []

    ### llenado de los encabezados
    for matriz_registro in matrices_registros :
        encabezados_matriz = matriz_registro[0]

        for encabezado in encabezados_matriz :
            encabezados_resultantes.append(encabezado)

    ### añadimos los encabezados a nuestra matriz resultante
    matriz_resultante.append(encabezados_resultantes)

    ### llenado de las filas
    cantidad_filas_resultantes = obtener_valor_mayor_tablas(matrices_registros)

    indice_fila_matriz_registro = 1

    while indice_fila_matriz_registro < cantidad_filas_resultantes :
        filas_resultantes = []
        for matriz_registro in matrices_registros :
            if indice_fila_matriz_registro >= len(matriz_registro):
                for valor in matriz_registro[0] :
                    filas_resultantes.append("-")
            else:
                fila_matriz = matriz_registro[indice_fila_matriz_registro]
                for valor in fila_matriz:
                    filas_resultantes.append(valor)
        indice_fila_matriz_registro += 1
        matriz_resultante.append(filas_resultantes)

    return matriz_resultante


def obtener_valor_mayor_tablas(tablas : []):

    valores = []
    for tabla in tablas :
        valores.append(len(tabla))

    mayor = valores[0]
    for numero in valores :
        if numero > mayor :
            mayor = numero
    return mayor

def insertar_registro(nombre_db, nombre_tabla, registro : Registro):

    try:
        registros: Registros = xml_to_records(f'{url_records_xml}/{nombre_db}/{nombre_tabla}.xml')
        registros.registros.append(registro)
        registros_xml = records_to_xml(registros)
        archivo: Archivo = Archivo(f'{url_records_xml}/{nombre_db}/{nombre_tabla}.xml')
        archivo.guardar(registros_xml)
        print(registros_xml)
    except UnboundLocalError as ule:
        if not os.path.exists(f'{url_records_xml}/{nombre_db}'):
            os.mkdir(f'{url_records_xml}/{nombre_db}')

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



def existe_archivo_registros(nombre_bd, nombre_tabla):
    if os.path.exists(f'{url_records_xml}/{nombre_bd}/{nombre_tabla}.xml'):
        return True

    return False

def eliminar_archivo_registro(nombre_db, nombre_tabla):
    os.remove(f'{url_records_xml}/{nombre_db}/{nombre_tabla}.xml')


def eliminar_carpeta_registros_db(nombre_db):
    rmtree(f"{url_records_xml}/{nombre_db}")
### pruebas
# registro : Registro = Registro(['campo'],['valor de campo'])
# insertar_registro('prueba','tabla_prueba',registro)
