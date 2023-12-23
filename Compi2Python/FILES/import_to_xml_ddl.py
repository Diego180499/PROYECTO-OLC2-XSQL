import xml.etree.ElementTree as ET
from FILES.BaseDatos import *
from FILES.Procedimiento import Procedimiento
from FILES.Tabla import *
from FILES.Campo import *
from FILES.ManejadorDB import *

#Crea Objetos Tablas
def fillTablas(tablas):
    tablasRet = []
    for tabla in tablas:
        nombre = tabla.find('nombre').text
        campos = tabla.findall('campo')
        newTab = Tabla(nombre, fillCampos(campos))
        tablasRet.append(newTab)
    return tablasRet
#Crea Objetos Campos
def fillCampos(campos):
    camposRet = []
    for campo in campos:
        nombre = campo.find('nombre').text
        tipoDato = campo.find('tipo_dato').text
        llavePrim = campo.find('llave_primaria').text
        nulo = campo.find('nulo').text
        tablaRef = campo.find('tabla_referencia').text
        campoRef =  campo.find('campo_referencia').text
        newCamp = Campo(nombre, tipoDato, nulo, llavePrim, tablaRef, campoRef)
        camposRet.append(newCamp)
    return camposRet

def fillProcedimientos(procedimientos):  ### agregar al back
    procedimientos_list = []

    for procedimiento in procedimientos :
        nombre_procedimiento = procedimiento.find('nombre').text
        procedimiento_objeto : Procedimiento = Procedimiento(nombre_procedimiento)
        procedimientos_list.append(procedimiento_objeto)
    return procedimientos_list

def xml_to_diccionario(url):
    manejadorDB = ManejadorDB()
    try:
        # Creamos el Manejador de Bases de Datos
        # en open, ponemos el path del archivo.
        xml_file = open(url)
        # Evaluamos si se lee el archivo
        if xml_file.readable():
            xml_data = ET.fromstring(xml_file.read())
            # Crea objeto Base de Datos
            nombreDB = xml_data.find('nombre').text
            ## se buscan sus tablas
            tablas = xml_data.findall('tabla')
            ## se buscan sus procedimientos
            procedimientos = xml_data.findall('procedimiento')  ### agregar al back
            baseDatos = BaseDatos(nombreDB, fillTablas(tablas))
            baseDatos.set_procedimientos(fillProcedimientos(procedimientos)) ### agregar en el back
            # Ingresa nueva base de datos al Manejador DB
            manejadorDB.addBaseDatos(baseDatos)
            diccionario = manejadorDB.getDiccionario()
            print(diccionario)
        else:
            print(False)
    except Exception as err:
        print("Error: ", err)
    finally:
        xml_file.close()
    return manejadorDB.getDiccionario()


    # en la url debe estar especificado el nombre de la base de datos,
    # ya que solo una en específico vamos a obtener.
def xml_to_base_de_datos(url):
    #manejadorDB = ManejadorDB()
    try:
        # en open, ponemos el path del archivo.
        xml_file = open(url)
        # Evaluamos si se lee el archivo
        if xml_file.readable():
            xml_data = ET.fromstring(xml_file.read())
            # Crea objeto Base de Datos
            nombreDB = xml_data.find('nombre').text
            tablas = xml_data.findall('tabla')
            baseDatos = BaseDatos(nombreDB, fillTablas(tablas))
            procedimientos = xml_data.findall('procedimiento')  ### agregar al back
            baseDatos.set_procedimientos(fillProcedimientos(procedimientos))  ### agregar en el back
        else:
            print(False)
    except Exception as err:
        print("Error: ", err)
    finally:
        xml_file.close()
    return baseDatos


#result = xml_to_diccionario(f'U:/Universidad/Ciclo 2023\EDV-DICIEMBRE/LAB - OLC2/REPO-PROYECTO-OLC2-XSQL/Compi2Python/resources/BASES_DE_DATOS_XML/colegio.xml')
#print(result)