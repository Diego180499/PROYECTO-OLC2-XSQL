class GenC3D:
    def __init__(self):
        # Contadores
        self.count_temp = 0
        self.count_label = 0
        # Label salida del programa
        self.label_out = ''

        # Codigo
        self.codigo = ''
        self.funcs = ''
        self.natives = ''
        self.in_func = False
        self.in_natives = False

        # Lista de temporales
        self.temps = []

    def clean_all(self):
        # Contadores
        self.count_temp = 0
        # codigo
        self.codigo = ""
        # Lista de temporales
        self.temps = []

    def get_header(self):
        code = '/* ---- HEADER ----- */\n'
        if len(self.temps) > 0:
            code += 'var '
            for temp in self.temps:
                code += temp + ','
            code = code[:-1]
            code += " float64;\n\n"
        code += "var P, H float64;\nvar stack[30101999] float64;\nvar heap[30101999] float64;\n\n"
        return code

    def get_code(self):
        return f'{self.get_header()}{self.natives}{self.funcs}\nfunc main(){{\n{self.codigo}\n}}'

    def code_in(self, code, tab="\t"):
        if self.in_natives:
            if self.natives == '':
                self.natives = self.natives + '/* --- NATIVAS --- */\n'
            self.natives = self.natives + tab + code
        elif self.in_func:
            if self.funcs == '':
                self.funcs = self.funcs + '/* --- FUNCION --- */\n'
            self.funcs = self.funcs + tab + code
        else:
            self.codigo = self.codigo + tab + code

    def add_comment(self, comment):
        self.code_in(f'/* {comment} */\n')

    def add_space(self):
        self.code_in('\n')

    #########################
    # Manejo de Temporales
    ########################

    def add_temp(self):
        temp = f't{self.count_temp}'
        self.count_temp += 1
        self.temps.append(temp)
        return temp  # t1 t2 t3 t4 t5

    #####################
    # Manejo de Labels
    #####################

    def new_label(self):
        label = f'L{self.count_label}'
        self.count_label += 1
        return label  # Agregamos un nuevo label L1 L2 L3 L4 L5

    def put_label(self, label):
        self.code_in(f'{label}:\n')  # Lo definimos en el codigo -> L1: L2: L3:

    def add_ident(self):
        self.code_in("")

    def add_space(self):
        self.code_in("\n")

    ###################
    # GOTO
    ###################

    def add_goto(self, label):
        self.code_in(f'goto {label};\n')

    def add_goto_out(self):
        self.code_in(f'goto {self.label_out};\n')

    ###################
    # IF
    ###################

    def add_if(self, left, right, op, label):
        self.code_in(f'if {left} {op} {right} {{goto {label};}}\n')

    ###################
    # EXPRESIONES
    ###################

    def add_exp(self, result, left, right, op):
        self.code_in(f'{result} =  {left} {op} {right};\n')

    def add_asig(self, result, left):
        self.code_in(f'{result} = {left};\n')

    ###############
    # FUNCS
    ###############

    def add_begin_func(self, id):
        if not self.in_natives:
            self.in_func = True
        self.code_in(f'func {id}(){{\n')

    def add_end_func(self):
        self.code_in('}\n')
        if not self.in_natives:
            self.in_func = False

    ###############
    # STACK
    ###############

    def set_stack(self, pos, value):
        self.code_in(f'stack[int({pos})] = {value};\n')

    def get_stack(self, place, pos):
        self.code_in(f'{place} = stack[int({pos})];\n')

    #############
    # ENTORNO
    #############

    def new_env(self, size):
        self.code_in('/* --- NUEVO ENTORNO --- */\n')
        self.code_in(f'P = P + {size};\n')

    def call_fun(self, id):
        self.code_in(f'{id}();\n')

    def ret_env(self, size):
        self.code_in(f'P = P - {size};\n')
        self.code_in('/* --- RETORNO DE ENTORNO --- */\n')

    ###############
    # HEAP
    ###############

    def set_heap(self, pos, value):
        self.code_in(f'heap[int({pos})] = {value};\n')

    def get_heap(self, place, pos):
        self.code_in(f'{place} = heap[int({pos})];\n')

    def next_heap(self):
        self.code_in('H = H + 1;\n')

    def write_c3d(self):
        code = ""
        code += f"STACK=[]\n"
        code += f"HEAP=[]\n"
        code += f"DECLARE "
        for tmp in self.temp:
            code += f"{tmp},"
        with open('c3d.txt', 'w') as file:
            file.write(f"{code}")
