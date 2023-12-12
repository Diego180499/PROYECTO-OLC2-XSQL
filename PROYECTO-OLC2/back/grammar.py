import re

# here start grammar
# --------------------------------------------------------------
# 04-06-2023: Created by Daniel Morales
# proyecto 1 - compiladores 2 usac 2023
# --------------------------------------------------------------
# Definimos las palabras reservadas de nuestro lenguaje
global_arr = []

reservadas = {
    'create': 'CREATE',
    'use': 'USE',
    'alter': 'ALTER',
    'drop': 'DROP',
    'case': 'CASE',
    'column': 'COLUMN',
    'truncate': 'TRUNCATE',
    'exec': 'EXEC',
    'select': 'SELECT',
    'from': 'FROM',
    'where': 'WHERE',
    'update': 'UPDATE',
    'insert': 'INSERT',
    'into': 'INTO',
    'values': 'VALUES',
    'if': 'IF',
    'when': 'WHEN',
    'then': 'THEN',
    'else': 'ELSE',
    'declare': 'DECLARE',
    'function': 'FUNCTION',
    'returns': 'RETURNS',
    'as': 'AS',
    'begin': 'BEGIN',
    'end': 'END',
    'return': 'RETURN',
    'not': 'NOT',
    'null': 'NULL',
    'primary': 'PRIMARY',
    'key': 'KEY',
    'data': 'DATA',
    'base': 'BASE',
    'table': 'TABLE',
    'procedure': 'PROCEDURE',
    'foregin': 'FOREIGN',
    'reference': 'REFERENCE',
    'add': 'ADD',
    'int': 'INT',
    'bit': 'BIT',
    'decimal': 'DECIMAL',
    'date': 'DATE',
    'datetime': 'DATETIME',
    'nchar': 'NCHAR',
    'nvarchar': 'NVARCHAR',
    'concatenar': 'CONCATENAR',
    'substraer': 'SUBSTRAER',
    'hoy': 'HOY',
    'contar': 'CONTAR',
    'suma': 'SUMA',
    'cast': 'CAST',
    'set': 'SET',
    'while': 'WHILE'
}
tokens = [
    'ID',
    'INTEGER_VALUE',
    'DECIMAL_VALUE',
    'SEMICOLON',
    'NAME',
    'STRING',
    'L_PAREN',
    'R_PAREN',
    'COMMA',
    'ASSIGN',
    'EQUALS',
    'NOT_EQ',
    'LESS_THAN',
    'GREATER_THAN',
    'LESS_EQ',
    'GREATER_EQ',
    'AND',  
    'OR',
    'NOT_SIGN',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE'
] + list(reservadas.values())

# Tokens
t_EQUALS = r'=='
t_LESS_EQ = r'<='
t_GREATER_EQ = r'>='
t_LESS_THAN = r'<'
t_GREATER_THAN = r'>'
t_NOT_EQ = r'!=='
t_NOT_SIGN = r'!'
t_AND = r'&&'
t_OR = r'\|\|'
t_L_PAREN = r'\('
t_R_PAREN = r'\)'
t_PLUS = r'\+'
t_MINUS = r'-'
t_DIVIDE = r'/'
t_TIMES = r'\*'
t_ASSIGN = r'='
t_SEMICOLON = r';'
t_COMMA = r','


# Expresiones Regulares de las cadenas con "" o ''
def t_STRING(t):
    r'(\"(\\\'|\\"|\\\\|\\n|\\t|[^\'\\\"])*?\")|(\'(\\\'|\\"|\\\\|\\n|\\t|[^\'\\\"])*?\')'
    t.value = t.value[1:-1]  # remuevo las comillas

    print(str(t.value))
    t.value = t.value.replace('\\n', '\n')
    t.value = t.value.replace('\\r', '\r')
    t.value = t.value.replace('\\t', '\t')
    t.value = t.value.replace('\\"', '\"')
    t.value = t.value.replace("\\'", '\'')
    t.value = t.value.replace('\\\\', '\\')
    return t


# Expersion Regular para decimal
def t_DECIMAL_VALUE(t):
    r'\d+\.\d+'
    try:
        t.value = float(t.value)
    except ValueError:
        # global_arr.append(ExceptionPyType(str(t.value) + " DEMASIADO GRANDE", t.lexer.lineno, -1))
        t.value = 0
    return t


# Expresion Regular para Entero
def t_INTEGER_VALUE(t):
    r'\d+'
    try:
        t.value = int(t.value)
    except ValueError:
        # global_arr.append(ExceptionPyType(str(t.value) + " DEMASIADO GRANDE", t.lexer.lineno, -1))
        t.value = 0
    return t

# Expresion Regular para IDS
def t_ID(t):
    r'@[a-zA-Z][a-zA-Z_0-9]*'
    t.type = reservadas.get(t.value, 'ID')
    return t

# ignorar espacios
t_ignore = " \t"


#Expresion regular para los nombre de las tablas, bases de datos, columnas
def t_NAME(t):
    r'[a-zA-Z][a-zA-Z0-9_]*'
    t.type = reservadas.get(t.value, 'NAME')
    return t

# Manejo de Linea
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


# Manejo de columna
def find_column(inp, token):
    line_start = str(inp).rfind('\n', 0, token.lexpos) + 1
    return (token.lexpos - line_start) + 1


def t_error(t):
    # errores.append(Excepcion("Lexico","Error léxico." + t.value[0] , t.lexer.lineno, find_column(input, t)))
    t.lexer.skip(1)


# Se construye el analizador lexico
import ply.lex as lex

lexer = lex.lex(reflags=re.IGNORECASE)

import sys

sys.setrecursionlimit(10000000)


def p_init(t):
    'init   : statements'


def p_statements(t):
    'statements : statements statement'


def p_statements_2(t):
    'statements : '


def p_statement(t):
    '''statement    : create_database_statement
                    | use_statement
                    | declare_statement
                    | set_statement
                    | create_table_statement
                    | select_statement
                    | insert_statement
                    | create_function_statement
                    | create_procedure_statement
                    | alter_table_statement
                    | if_statement
                    | exec_statement
                    | drop_table_statement
                    | case_statement
                    | update_statement
                    | while_statement'''


##### CREATE DATABASE #####

def p_create_database_statement(t):
    'create_database_statement    : CREATE DATA BASE NAME SEMICOLON'

#### USE ####

def p_use_statement(t):
    'use_statement   : USE NAME SEMICOLON'

#### DECLARE ####

def p_declare_statement(t):
    'declare_statement   : DECLARE ID AS type SEMICOLON'

#### SET ####

def p_set_statement(t):
    'set_statement   : SET assignments SEMICOLON'



def p_assignments(t):
    'assignments    : assignments COMMA ID ASSIGN a'


def p_assignments_2(t):
    'assignments    : ID ASSIGN a'

#### CREATE TABLE ####

def p_create_table_statement(t):
    'create_table_statement : CREATE TABLE NAME L_PAREN properties R_PAREN SEMICOLON'


def p_properties(t):
    'properties : properties COMMA property'

def p_properties_2(t):
    'properties : property'


def p_property(t):
    'property   : NAME type null_prod PRIMARY KEY'

    
def p_property_2(t):
    'property   : NAME type null_prod'


def p_property_3(t):
    'property   : NAME type null_prod REFERENCE NAME L_PAREN NAME R_PAREN'


def p_null_prod(t):
    'null_prod  : NOT NULL'

def p_null_prod_2(t):
    'null_prod  : NULL'


def p_null_prod_3(t):
    'null_prod  : '

#### SELECT ####

def p_select_statement(t):
    'select_statement   : SELECT columns FROM NAME SEMICOLON'


def p_select_statement_2(t):
    'select_statement   : SELECT columns FROM NAME WHERE a SEMICOLON'


def p_select_statement_3(t):
    'select_statement   : SELECT TIMES FROM NAME SEMICOLON'


def p_select_statement_4(t):
    'select_statement    : SELECT TIMES FROM NAME WHERE a SEMICOLON'


#### INSERT ####

def p_insert_statement(t):
    'insert_statement   : INSERT INTO NAME L_PAREN columns R_PAREN VALUES L_PAREN vals R_PAREN SEMICOLON'


#### COLUMNS AND VALS PRODS ####

def p_columns(t):
    'columns    : columns COMMA NAME'


def p_columns_2(t):
    'columns    : NAME'


def p_vals(t):
    'vals   : vals COMMA a'


def p_vals_2(t):
    'vals   : a'

#### CREATE FUNCTION AND PROCEDURE ####

def p_create_function_statement(t):
    'create_function_statement  : CREATE FUNCTION NAME L_PAREN parameters R_PAREN RETURN type AS BEGIN statements END SEMICOLON'


def p_create_procedure_statement(t):
    'create_procedure_statement : CREATE PROCEDURE NAME L_PAREN parameters R_PAREN AS BEGIN statements END SEMICOLON'

def p_parameters(t):
    'parameters : parameters COMMA ID AS type'


def p_parameters_2(t):
    'parameters : ID AS type'

#### ALTER TABLE, FUNCTION AND PROCEDURE ####
def p_alter_table_statement(t):
    'alter_table_statement  : ALTER TABLE NAME ADD COLUMN NAME type SEMICOLON'


def p_alter_table_statement_2(t):
    'alter_table_statement  : ALTER TABLE NAME DROP COLUMN NAME SEMICOLON'


# def p_alter_function_statement(t):
#     'alter_function_statement   : ALTER FUNCTION NAME AS BEGIN statements END SEMICOLON'
#
#
# def p_alter_procedure_statement(t):
    # 'alter_procedure_statement  : ALTER PROCEDURE '


#### IF STATEMENT ####
def p_if_statement(t):
    'if_statement   : IF L_PAREN a COMMA a COMMA a R_PAREN SEMICOLON'


#### EXEC ####
def p_exec_statement(t):
    'exec_statement : EXEC NAME vals SEMICOLON'


#### DROP TABLE ####
def p_drop_table_statement(t):
    'drop_table_statement   : DROP TABLE NAME SEMICOLON'


#### UPDATE STATEMENT ####
def p_update_statement(t):
    'update_statement   : UPDATE NAME SET column_assignments WHERE a SEMICOLON'

#### COLUMN aSSIGNMENTS ####
def p_column_assignments(t):
    'column_assignments  : column_assignments COMMA NAME ASSIGN a'


def p_column_assignments_2(t):
    'column_assignments : NAME ASSIGN a'


#### CASE STATEMENT ####
def p_case_statement(t):
    'case_statement : '

#### WHILE STATEMENT ####
def p_while_statement(t):
    'while_statement    : WHILE a BEGIN statements END SEMICOLON'

def p_type(t):
    '''type : INT
            | DECIMAL
            | BIT
            | NCHAR
            | NVARCHAR
            | DATE
            | DATETIME'''

def p_a(t):
    '''a    : INTEGER_VALUE
            | STRING
    '''


def p_error(t):
    print("Error sintáctico en '%s'" % t.value+" "+ t.type)
    # if t is not None:
        # global_arr.append(ExceptionPyType("ERROR SINTACTICO en " + str(t.value) + " SE ESPERABA ALGO MAS", t.lexer.lineno, find_column(input, t)))

import ply.yacc as yacc

def parse(inp):
    global parser
    global lexer
    lexer = lex.lex(reflags=re.IGNORECASE)
    parser = yacc.yacc()
    lexer.lineno = 1

    return parser.parse(inp)


inst = parse("""create data base my_db;
            use my_db;
            select * from my_db;
            insert into my_db (c, d, b) values (1, "hola");
            if(3, "verdadero",'falso');
            create table tabla1(
                campo1 int null primary key,
                campo2 nvarchar null,
                campo3 date reference tabla2(campo3)
            );
            
            create procedure procedimiento1(@variable1 as int) as begin 
                select * from tabla1; 
            end;
            
            create function funcion1 (@var2 as nvarchar) return date as begin
                select * from tabla2;
            end;
            
            exec procedimiento1 'a', 'b';
            
            while 1 begin
                select * from tabla2;
            end;
            
""")
