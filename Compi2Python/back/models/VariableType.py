class VariableType:

    def __init__(self, type: str, length: any):
        self.type = type
        self.length = length

    def __str__(self):
        return f"""{self.type}, {self.length}"""
