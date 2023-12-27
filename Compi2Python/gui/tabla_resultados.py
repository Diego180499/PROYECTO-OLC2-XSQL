from tkinter import RIGHT, BOTTOM
from tkinter.constants import Y, X, BOTH
from tkinter.ttk import Treeview, Scrollbar


class TablaResultados(Treeview):

    def __init__(self, pestana):
        scrollbar_y = Scrollbar(pestana,)
        scrollbar_y.pack(side=RIGHT, fill=Y)
        scrollbar_x = Scrollbar(pestana)
        scrollbar_x.pack(side=BOTTOM, fill=X)
        super().__init__(pestana, xscrollcommand=scrollbar_x.set, yscrollcommand=scrollbar_y.set)
        self.pack(expand=True, fill=BOTH)
        scrollbar_x.config(command=self.xview)
        scrollbar_y.config(command=self.yview)
        self.contadorColumnas = 1

    def __crear_encabezado__(self, nombreEncabezado):
        idColumna = f'#{self.contadorColumnas}'
        self.heading(idColumna, text=nombreEncabezado)
        self.contadorColumnas += 1
        self.pack()

    # El parámetro 'columnas' será un arreglo con los nombres de las columnas
    # que tendrá nuestra tabla
    def __definir_tabla__(self, encabezados):
        self.config(columns=encabezados)
        self.column("#0", width=0)
        self.pack()

    # Para ingresar una fila o 'registro' a nuestra tabla, necesitaremos recibir como parametro
    # un arreglo de valores para ir agregandolos a la tabla
    def __insertar_fila__(self, valores):
        self.insert("", "end", values=valores)
        self.pack()

   

    def __llenar_filas__(self, filas):
        for fila in filas:
            self.__insertar_fila__(fila)

    def construir_tabla(self, matriz):
        encabezados = matriz[0]
        self.__definir_tabla__(encabezados)
        valores: []
        for encabezado in encabezados:
            self.__crear_encabezado__(encabezado)

        indice = 0
        filas = []
        for fila in matriz:
            if indice > 0:
                filas.append(fila)
            indice += 1

        self.__llenar_filas__(filas)
        self.contadorColumnas = 1
        # self.__inicializar_tabla(self.pestana)

    def limpiar_tabla(self):
        # Elimina todas las filas existentes en el TreeView
        for item in self.get_children():
            self.delete(item)
