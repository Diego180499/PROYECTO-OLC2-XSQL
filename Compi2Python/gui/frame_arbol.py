from tkinter import *
from tkinter.ttk import Treeview, Notebook


class FrameArbol:

    def __init__(self, ventana_padre, width, height, row, column, rowspan=1, columnspan=1, titulo="Arbol"):
        self.notebook = Notebook(ventana_padre, width=width, height=height)
        self.notebook.grid(row=row, column=column, rowspan=rowspan, columnspan=columnspan)
        pestana = Frame(self.notebook)
        pestana.pack()
        self.__inicializar_arbol(pestana)
        self.notebook.add(pestana, text=titulo)
        self.notebook.select(pestana)

    def __inicializar_arbol(self, pestana):
        scrollbar_y = Scrollbar(pestana)
        scrollbar_y.pack(side=RIGHT, fill=Y)
        scrollbar_x = Scrollbar(pestana)
        scrollbar_x.pack(side=BOTTOM, fill=X)
        self.arbol = Treeview(pestana, xscrollcommand=scrollbar_x.set, yscrollcommand=scrollbar_y.set)
        self.arbol.pack(expand=True, fill=BOTH)
        scrollbar_x.config(command=self.arbol.xview)
        scrollbar_y.config(command=self.arbol.yview)

    def __insertar_padre(self, nombre_padre):
        elemento = self.arbol.insert("", END, text=nombre_padre)
        return elemento

    def __insertar_hijo(self, nombre_hijo, elemento_padre):
        elemento = self.arbol.insert(elemento_padre, END, text=nombre_hijo)
        return elemento

    def generar_arbol(self, raiz=None, diccionario=None):
        if diccionario is None:
            diccionario = dict()
        for key, value in diccionario.items():
            if raiz is None:
                elemento_padre = self.__insertar_padre(key)
            else:
                elemento_padre = self.__insertar_hijo(str(key), raiz)
            if isinstance(value, dict):
                self.generar_arbol(elemento_padre, value)
            elif isinstance(value, list):
                self.__generar_arbol_desde_lista(elemento_padre, value)
            else:
                self.__insertar_hijo(str(value), elemento_padre)
        self.__expandir_arbol__(self.arbol.focus())

    def __generar_arbol_desde_lista(self, elemento_padre, lista):
        for elemento in lista:
            if isinstance(elemento, dict):
                self.generar_arbol(elemento_padre, elemento)
            elif isinstance(elemento, list):
                nuevo_padre = self.__insertar_hijo("[..]", elemento_padre)
                self.__generar_arbol_desde_lista(nuevo_padre, elemento)
            else:
                self.__insertar_hijo(str(elemento), elemento_padre)

    def limpiar_arbol(self):
        # Elimina todas las filas existentes en el TreeView
        for item in self.arbol.get_children():
            self.arbol.delete(item)

    def __expandir_arbol__(self,nodo):
        self.arbol.item(nodo, open=True)
        for child in self.arbol.get_children(nodo):
            self.__expandir_arbol__(child)
