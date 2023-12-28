import xml.etree.ElementTree as ET

from src.FILES.Registro import Registro
from src.FILES.Registros import Registros


#Crea Objetos Tablas
def fillRegistros(registros):
    registrosRet = []
    for registro in registros:
        campos = registro.findall('campo')
        valores = registro.findall('valor')
        campos_str = campo_xml_to_string(campos)
        valores_str = valor_xml_to_string(valores)
        newRegistro = Registro(campos_str, valores_str)
        registrosRet.append(newRegistro)
    return registrosRet

###### CONVERTIR A MATRIZ  ######
def xml_to_matriz(url):
    #Crea Objetos Campos

    try:
        #en open, ponemos el path del archivo.
        xml_file = open(url)
        #Evaluamos si se lee el archivo
        if xml_file.readable():
            xml_data = ET.fromstring(xml_file.read())
            #Crea objeto Base de Datos
            nombreDB = xml_data.find('base_datos').text
            nombreTab = xml_data.find('tabla').text
            registros =  xml_data.findall('registro')
            newRegistros = Registros(nombreDB, nombreTab, fillRegistros(registros))
            matriz_registros = newRegistros.matriz()
        else:
            print(False)
    except Exception as err:
        print("Error: ", err)
    finally:
        xml_file.close()
    return matriz_registros



##### CONVERTIR A OBJETOS REGISTRO   #####
def xml_to_records(url):
    # Crea Objetos Campos
    try:
        # en open, ponemos el path del archivo.
        xml_file = open(url)
        # Evaluamos si se lee el archivo
        if xml_file.readable():
            xml_data = ET.fromstring(xml_file.read())
            # Crea objeto Base de Datos
            nombreDB = xml_data.find('base_datos').text
            nombreTab = xml_data.find('tabla').text
            registros = xml_data.findall('registro')
            newRegistros = Registros(nombreDB, nombreTab, fillRegistros(registros))

        else:
            print(False)
    except Exception as err:
        print("Error: ", err)
    finally:
        xml_file.close()
    return newRegistros


#### CONVERTIR ARRAY DE ETIQUETAS A SUS VALORES STRING  #####
def campo_xml_to_string(campos : []):
    valor_campos = []

    for campo in campos :
        valor_campos.append(campo.text)

    return valor_campos


def valor_xml_to_string(valores: []):
    string_valores = []

    for valor in valores:
        string_valores.append(valor.text)

    return string_valores