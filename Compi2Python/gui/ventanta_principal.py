import errno
import os
import pathlib
from tkinter import *


from gui.conector import Conector
from gui.frame_arbol import FrameArbol
from gui.frame_pestanas import FramePestanas
from gui.frame_salida import FrameSalida
from gui.menu_archivo import MenuArchivo
from gui.menu_ayuda import MenuAyuda
from gui.menu_herramientas import MenuHerramientas


class VentanaPrincipal:

    def __init__(self):
        # creacion de la ventana principal
        self.ventana = Tk()
        self.ventana.geometry("1200x640")
        self.ventana.resizable(False, False)
        self.ventana.iconbitmap('')
        self.ventana.title("Proyecto Compiladores 2")
        self.ventana.iconphoto(True, PhotoImage(file=f'gui/resources/icono.png'))
        # añadimos los 3 frames principales
        self.frame_arbol = FrameArbol(self.ventana, width=350, height=600, row=0, column=0, rowspan=2)
        self.frame_pestanas = FramePestanas(self.ventana, width=750, height=270, row=0, column=1)
        self.frame_salida = FrameSalida(self.ventana, width=750, height=270, row=1, column=1)
        self.iconos = dict()
        imagenes = self.__listar_imagenes__()
        for imagen in imagenes:
            path_imagen = f'gui/resources/'
            self.iconos[imagen] = PhotoImage(file=path_imagen + imagen + '.png')

        # añadimos la barra de menú
        self.menu = Menu(self.ventana)
        self.menu_archivo = MenuArchivo(self)
        self.menu_herramientas = MenuHerramientas(self)
        self.menu_ayuda = MenuAyuda(self)
        self.menu.add_cascade(label='Archivo', menu=self.menu_archivo)
        self.menu.add_cascade(label='Herramientas', menu=self.menu_herramientas)
        self.menu.add_cascade(label='Ayuda', menu=self.menu_ayuda)
        self.ventana.config(menu=self.menu)

        # añadirmos evento del cierre de ventana
        self.ventana.protocol("WM_DELETE_WINDOW", self.menu_archivo.evento_menu_salir)

    def ejecutar(self):
        conector = Conector()
        ### listar archivos de las bases de datos ###
        self.__listar_nombres_bd__(conector)
        self.ventana.mainloop()

    def __listar_nombres_bd__(self, conector):
        url_proyecto = f'resources/BASES_DE_DATOS_XML'
        nombres_bd = os.listdir(url_proyecto)  # obtiene una lista con todos los archivos que contenga mi carpeta
        diccionario=dict()
        bases_de_datos=[]
        for nombre_bd in nombres_bd:
            bases_de_datos.append(conector.cargar_arbol(f'{url_proyecto}/{nombre_bd}'))
        diccionario["bases_de_datos"]=bases_de_datos
        self.frame_arbol.generar_arbol(diccionario=diccionario)

    def __listar_imagenes__(self):
        lista_imagenes = os.listdir(f'gui/resources')
        imagenes = []
        for path_imagen in lista_imagenes:
            nombre_imagen = path_imagen.split(".")[0]
            if nombre_imagen != '':
                imagenes.append(nombre_imagen)
        return imagenes
