class Archivo:

    def __init__(self, ubicacion=None):
        # en python no existe la sobre carga, así que el if simula los dos contructores
        self.ubicacion = ubicacion
        self.contenido = None
        if ubicacion is not None:
            partes_ubicacion = ubicacion.split("/")
            self.nombre = partes_ubicacion[len(partes_ubicacion) - 1]
        else:
            self.nombre = "Nuevo"

    def abrir_archivo(self):
        # este metodo no recibe ningún parametro, y devuelve el valor del contenido de un archivo
        try:
            with open(self.ubicacion, 'r') as archivo:
                self.contenido = archivo.read()
            print("abierto:", self.ubicacion)
            return self.contenido
        except Exception as e:
            print(str(e))
            return None

    def guardar(self, contenido):
        # recibe como parametro la variable contenido, guarda el contenido de dicho parametro en un archivo cuya ubicacion es el valor de la variable ubicacion, settea la variable global contenido con el valor del parametro y  devuelve true si el guardado ha sido correcto o false si ha sido incorrecto (por ejemplo, variable ubicacion vacia
        try:
            if self.ubicacion is None:
                return None
            with open(self.ubicacion, 'w') as archivo:
                self.contenido = contenido
                archivo.write(contenido)
            print("guardado: ", self.ubicacion)
            return self
        except Exception as e:
            print(str(e))
            return None

    def guardar_como(self, contenido, ubicacion):
        self.ubicacion = ubicacion
        return self.guardar(contenido)
