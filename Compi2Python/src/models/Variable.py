class Variable:

    def __init__(self):
        self.id = None
        self.variable_type = None
        self.symbol_type = None
        self.value = None
        self.pos = None

    def __str__(self):
        return f"""Variable: {self.id}, {self.variable_type}, {self.value} , {self.temp}, {self.label_true}, {self.label_false}"""
