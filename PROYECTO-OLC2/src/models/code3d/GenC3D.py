class GenC3D:
    def __init__(self):
        self.stack = []
        self.heap = []
        self.temp = []
        self.labels = []

    def agregar_temp(self):
        cantidad = len(self.temp)
        label = f"t{cantidad}"
        self.temp.append(label)
        return label

    def agregar_label(self):
        cantidad = len(self.labels)
        label = f"L{cantidad}"
        self.labels.append(label)

    def has_label(self, label):
        return label in self.labels

    def get_top_label(self):
        return self.labels[-1]

    def get_top_temp(self):
        return self.temp[-1]

    def write_c3d(self):
        code = ""
        code += f"STACK=[]\n"
        code += f"HEAP=[]\n"
        code += f"DECLARE "
        for tmp in self.temp:
            code += f"{tmp},"
        with open('c3d.txt', 'w') as file:
            file.write(f"{code}")
