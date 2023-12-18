from tkinter import RIGHT, BOTTOM
from tkinter.constants import Y, X, BOTH
from tkinter.ttk import Notebook, Treeview, Frame, Scrollbar


class FrameSalida:

    def __init__(self, ventana_padre, width, height, row, column, rowspan=1, columnspan=1,titulo="Salida"):
        self.notebook = Notebook(ventana_padre, width=width, height=height)
        self.notebook.grid(row=row, column=column, rowspan=rowspan, columnspan=columnspan)
        self.pestana = Frame(self.notebook)
        self.pestana.pack()
        self.__inicializar_tabla(self.pestana)
        self.notebook.add(self.pestana, text=titulo)
        self.notebook.select(self.pestana)
        self.contadorColumnas=1

    def __inicializar_tabla(self, pestana):
        scrollbar_y = Scrollbar(pestana)
        scrollbar_y.pack(side=RIGHT, fill=Y)
        scrollbar_x = Scrollbar(pestana)
        scrollbar_x.pack(side=BOTTOM, fill=X)
        self.tabla = Treeview(pestana, xscrollcommand=scrollbar_x.set, yscrollcommand=scrollbar_y.set)
        self.tabla.pack(expand=True, fill=BOTH)
        scrollbar_x.config(command=self.tabla.xview)
        scrollbar_y.config(command=self.tabla.yview)


    def crear_encabezado(self, nombreEncabezado):
        idColumna = f'#{self.contadorColumnas}'
        self.tabla.heading(idColumna, text=nombreEncabezado)
        self.contadorColumnas+=1
        self.tabla.pack()

    #El parámetro 'columnas' será un arreglo con los nombres de las columnas
    # que tendrá nuestra tabla
    def definir_tabla(self, encabezados):
        self.tabla.config(columns=encabezados)
        self.tabla.column("#0",width=0)


        self.tabla.pack()

    # Para ingresar una fila o 'registro' a nuestra tabla, necesitaremos recibir como parametro
    # un arreglo de valores para ir agregandolos a la tabla
    def insertar_fila(self, valores):
        self.tabla.insert("","end",values=valores)
        self.tabla.pack()


    def construir_tabla(self,matriz):
        encabezados = matriz[0]
        self.definir_tabla(encabezados)
        valores : []
        for encabezado in encabezados:
            self.crear_encabezado(encabezado)

        indice = 0
        filas = []
        for fila in matriz :
            if indice > 0 :
                filas.append(fila)
            indice += 1

        self.llenar_filas(filas)
        self.contadorColumnas = 1
        #self.__inicializar_tabla(self.pestana)


    def llenar_filas(self,filas):

        for fila in filas :
            self.insertar_fila(fila)

    def limpiar_tabla(self):
        # Elimina todas las filas existentes en el TreeView
        for item in self.tabla.get_children():
            self.tabla.delete(item)
