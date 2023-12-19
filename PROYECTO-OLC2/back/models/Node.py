class Node(Instruction):
    def __init__(self, line, column, value):
        super().__init__(line, column)
        self.value = value
    
    def execute(self, symbol_table: SymbolTable):
        pass
    
    def __str__(self):
        return f"Node: {self.value}"

    def dot(self):
        pass
        
    def c3d(self,scope):
        pass