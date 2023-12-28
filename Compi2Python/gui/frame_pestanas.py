from tkinter import *
from tkinter.ttk import Notebook

from gui.editor_texto import EditorTexto
from src.utils.archivo import Archivo


class FramePestanas:

    def __init__(self, ventana_padre, width, height, row, column, rowspan=1, columnspan=1):
        self.control_pestanas = Notebook(ventana_padre, width=width, height=height)
        self.control_pestanas.bind("<<NotebookTabChanged>>", self.evento_seleccionar_tab)
        self.control_pestanas.grid(row=row, column=column, rowspan=rowspan, columnspan=columnspan)

    def agregar_pestana(self, archivo):
        pestana = Frame(self.control_pestanas)
        pestana.pack()
        self.__inicializar_editor(pestana, archivo)
        self.control_pestanas.add(pestana, text=archivo.nombre)
        self.control_pestanas.select(pestana)

    def __inicializar_editor(self, pestana, archivo):
        Label(pestana, text=archivo.ubicacion).pack()
        scrollbar_y = Scrollbar(pestana)
        scrollbar_y.pack(side=RIGHT, fill=Y)
        scrollbar_x = Scrollbar(pestana)
        scrollbar_x.pack(side=BOTTOM, fill=X)
        text = EditorTexto(pestana, xscrollcommand=scrollbar_x.set, yscrollcommand=scrollbar_y.set, wrap="none")
        if archivo.ubicacion is not None:
            text.insert(END, archivo.abrir_archivo())
        text.pack(fill=BOTH)
        scrollbar_x.config(command=text.xview)
        scrollbar_y.config(command=text.yview)

    def guardar_pestana_activa(self, nueva_ubicacion=None):
        ubicacion, contenido = self.obtener_ubicacion_contenido_desde_pestana_activa()
        if nueva_ubicacion is None and ubicacion is None:
            # no se puede guardar dado que no tiene una ubicacion correcta
            return None
        if nueva_ubicacion == None:
            # se guarda con la ubicacion obtenida desde el label
            return Archivo(ubicacion).guardar(contenido)
        else:
            # se guarda con la ubicacion recibida por parametro
            archivo = Archivo(nueva_ubicacion).guardar(contenido)
            self.modificar_pestana_activa(archivo)
            return archivo

    def cerrar_pestana_activa(self, forzar_cerrar=False):
        """cierra la pestaña solo si no hay cambios, o si es forzaco mediante 'cerrar_sin_guardar' """
        if forzar_cerrar:
            self.control_pestanas.forget(self.control_pestanas.select())
            return None, True

        ubicacion, contenido_pestana = self.obtener_ubicacion_contenido_desde_pestana_activa()

        # si es una pestana de archivo nuevo
        if ubicacion is None:
            # si no tiene contenido
            if len(contenido_pestana) == 0:
                self.control_pestanas.forget(self.control_pestanas.select())
                return None, True

            # retornamos False, que signfica que no pudo cerrar la pestaña dado que hay cambios
            return None, False

        # si llega aqui es que no es un archivo nuevo, cuya ubicacion viene del label de la pestana
        archivo = Archivo(ubicacion)
        contenido_archivo = archivo.abrir_archivo()

        # si no hay cambios se puede cerrar la pestaña
        if contenido_archivo == contenido_pestana:
            self.control_pestanas.forget(self.control_pestanas.select())
            return ubicacion, True

        # retornamos False, que signfica que no pudo cerrar la pestaña dado que hay cambios
        return ubicacion, False

    def obtener_ubicacion_contenido_desde_pestana_activa(self):
        pestana_seleccionado = self.control_pestanas.nametowidget(self.control_pestanas.select())
        contenido = None
        ubicacion = None
        for widget in pestana_seleccionado.winfo_children():
            if isinstance(widget, Label):
                ubicacion = widget.cget("text")
                if ubicacion == '':
                    ubicacion = None
            if isinstance(widget, Text):
                # se remueve el ultimo caracter con [:-1], dado que se añade solo por el widget
                contenido = widget.get("1.0", END)[:-1]
        return ubicacion, contenido

    def hay_pestanas(self):
        for i in self.control_pestanas.tabs():
            return True
        return False

    def modificar_pestana_activa(self, archivo):
        if archivo.ubicacion is None:
            return
        pestana_seleccionado = self.control_pestanas.nametowidget(self.control_pestanas.select())
        self.control_pestanas.tab(pestana_seleccionado, text=archivo.nombre)
        for widget in pestana_seleccionado.winfo_children():
            if isinstance(widget, Label):
                widget["text"] = archivo.ubicacion
            if isinstance(widget, Text):
                widget.delete("1.0", END)
                widget.insert("1.0", archivo.abrir_archivo())

    def evento_seleccionar_tab(self, evento):
        pass
