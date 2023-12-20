class NodoAST():
    def __init__(self, name, label, shape='oval', color='black'):
        self.name = name
        self.label = label
        self.shape = shape
        self.color = color

    def __str__(self):
        return f'{self.name} [label="{self.label}" shape="{self.shape}", color="{self.color}"];\n'

class Graficador():
    def __init__(self):
        self.name = 'AST'
        self.nodos = []
        self.relaciones = []

    def agregarNode(self, label):
        nodo = NodoAST(self.getNameNode(), label)
        self.nodos.append(nodo)
        return nodo

    def agregarRelacion(self, nodo1, nodo2):
        self.relaciones.append([nodo1, nodo2])
        
    def getNameNode(self):
        return f"node{len(self.nodos)}"

    def obtenerDefNodos(self):
        defNodos = ''
        for nodo in self.nodos:
            defNodos += f'{nodo.name} [label="{nodo.label}" shape="{nodo.shape}", color="{nodo.color}"];\n'
        return defNodos
    
    def obtenerDefRelaciones(self):
        defRelaciones = ''
        for relacion in self.relaciones:
            defRelaciones += f'{relacion[0].name} -> {relacion[1].name};\n'
        return defRelaciones

    def generarDOT(self):
        dot = f"digraph {self.name}"+"{\n"
        dot += self.obtenerDefNodos()
        dot += self.obtenerDefRelaciones()
        dot += '}'
        print(dot)
        #self.escribirDOT(dot)
    
    def escribirDOT(self, dot):
        with open('graphviz/ast.dot', 'w') as file:
            file.write(dot)
