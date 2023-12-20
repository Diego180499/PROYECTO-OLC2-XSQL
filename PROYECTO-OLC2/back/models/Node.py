class Node(Instruction):
    def __init__(self, line, column, left, right):
        super().__init__(line, column)
        self.left = left
        self.right = right
    
    def execute(self, symbol_table: SymbolTable):
        pass
    
    def __str__(self):
        return f"Node: {self.value}"

    def dot(self,nodo_padre, graficador):
        pass
        
    def c3d(self,scope):
        pass