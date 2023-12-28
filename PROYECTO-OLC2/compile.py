from src.utilities.utilities import errors_to_matrix, tabla_simbolos_a_matriz
from src.models.symbolTable.SymbolTable import SymbolTable
from src.models.symbolTable.ScopeType import ScopeType
from grammar import *
from src.models.graphviz.Graficador import Graficador


def parsear():
    resultados_finales = []

    contenido_1 = '''
        create data base school;
        
        use school;
        
        create table students(
            id int primary key,
            first_name nvarchar(100) not null,
            last_name nvarchar(100) not null
        );
        
        create table professors(
            id int primary key,
            name nvarchar(100) not null
        );
        
        create table courses(
            id int primary key,
            name nvarchar(100) not null,
            professor_id int reference professors(id)
        );
        
        insert into students(id, first_name, last_name) values(1, 'José', 'Castro');
        insert into students(id, first_name, last_name) values(2, 'Raquel', 'Rodriguez');
        insert into students(id, first_name, last_name) values(3, 'Martin', 'Monterroso');
        
        insert into professors(id, name) values (1, 'Ernesto');
        insert into professors(id, name) values (2, 'Moises');
        insert into professors(id, name) values (3, 'Julio');
        
        insert into courses(id, name, professor_id) values(1, 'Physics', 1);
        insert into courses(id, name, professor_id) values(2, 'Programming', 2);
        insert into courses(id, name, professor_id) values(3, 'Math', 3);
        
        select id, first_name, contar() conteo, suma(id) sumas, 
        if(first_name == 'Raquel', 'Verdadero', 'Falso') condicion, 10 + 5 operacion_fija from students;
    '''

    inst = parse("""
        use school;
        
        update students set first_name = 10, last_name= 'Cifuentes' where id == 2;
        select * from students;
    """)
    # inst = parse(contenido_1)
    print('Errores sintacticos:')
    if len(errores_sintacticos) > 0:
        print(errors_to_matrix(errores_sintacticos))
        resultados_finales.append(errors_to_matrix(errores_sintacticos))
        return resultados_finales
    print('Resultado del analisis sintactico:')
    symbol_table = SymbolTable(ScopeType().GLOBAL)
    # Imprecion del ast en formato string
    # print(inst)
    # Generacion del dot para el ast
    graficador = Graficador()
    inst.dot(None, graficador)
    graficador.generarDOT()
    # Ejecucion del codigo
    result = inst.execute(symbol_table, errores_sintacticos)
    matriz_tabla_simbolos = tabla_simbolos_a_matriz(symbol_table)
    if isinstance(result, list):
        tabla_select = result
        resultados_finales.append(tabla_select)
    resultados_finales.append(matriz_tabla_simbolos)

    for symbol in symbol_table.symbols:
        print(symbol.id, symbol.symbol_type, symbol.variable_type.type, symbol.value)
    return resultados_finales


parsear()
