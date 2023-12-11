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
    'select': 'TRUNCATE',
    'from': 'FROM',
    'where': 'WHERE',
    'update': 'UPDATE',
    'insert': 'INSERT',
    'into': 'INTO',
    'values': 'VALUES',
    'if': 'IF',
    'case': 'CASE',
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
    'set': 'SET'
}
tokens = [
    'ID',
    'INTEGER',
    'DECIMAL',
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
    'NOT',
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
t_NOT = r'!'
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
    r'\"(\\\'|\\"|\\\\|\\n|\\t|[^\'\\\"])*?\"'
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
def t_DECIMAL(t):
    r'\d+\.\d+'
    try:
        t.value = float(t.value)
    except ValueError:
        # global_arr.append(ExceptionPyType(str(t.value) + " DEMASIADO GRANDE", t.lexer.lineno, -1))
        t.value = 0
    return t


# Expresion Regular para Entero
def t_INTEGER(t):
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
import back.ply.lex as lex

lexer = lex.lex(reflags=re.IGNORECASE)

import sys

sys.setrecursionlimit(10000000)

def p_init(t):
    'init   : init statement'

def p_init_2(t):
    'init   : '

def p_statement(t):
    '''statement    : createDatabaseStatement
                    | useStatement
                    | declareStatement
                    | setStatement
                    | createTableStatement
                    | selectStatement
                    | insertStatement
                    | createFunctionStatement
                    | createProcedureStatement
                    | alterTableStatement
                    | alterFunctionStatement
                    | alterProcedureStatement
                    | ifStatement
                    | execStatement
                    | dropTableStatement
                    | caseStatement
                    | updateStatement'''

def p_create_database_statement(t):
    'createDatabaseStatement    :   CREATE DATA BASE NAME SEMICOLON'

def p_use_statement(t):
    'useStatement   : USE NAME SEMICOLON'

def p_declare_statement(t):
    'declareStatement   : DECLARE ID type SEMICOLON'

def p_set_statement(t):
    'setStatement   : SET assignments SEMICOLON'

def p_assignments(t):
    'assignments    : assignments COMMA ID ASSIGN a'

def p_assignments_2(t):
    'assignments    : ID ASSIGN a'

def p_create_table_statement(t):
    'createTableStatement   : CREATE TABLE NAME L_PAREN properties R_PAREN SEMICOLON'

def p_properties(t):
    'properties : properties COMMA property'

def p_properties_2(t):
    'properties : property'

def p_property(t):
    'property   : NAME type PRIMARY KEY'
    
def p_property_2(t):
    'property   : NAME type'

def p_property_3(t):
    'property   : NAME type REFERENCES NAME L_PAREN NAME R_PAREN'

def p_select_statement(t):
    'selectStatement    : SELECT columns FROM NAME SEMICOLON'

def p_select_statement_2(t):
    'selectStatement    : SELECT columns FROM NAME WHERE a SEMICOLON'

def p_select_statement_3(t):
    'selectStatement    : SELECT TIMES FROM NAME SEMICOLON'

def p_select_statement_4(t):
    'selectStatement    : SELECT TIMES FROM NAME WHERE a SEMICOLON'

def p_type(t):
    '''type : INT
            | DECIMAL
            | BYTE
            | NCHAR
            | NVARCHAR
            | DATE
            | DATETIME'''


#def p_error(t):
    # print("Error sintáctico en '%s'" % t.value+" "+ t.type)
    # if t is not None:
        # global_arr.append(ExceptionPyType("ERROR SINTACTICO en " + str(t.value) + " SE ESPERABA ALGO MAS", t.lexer.lineno, find_column(input, t)))

import back.ply.yacc as yacc

def parse(inp):
    global parser
    global lexer
    lexer = lex.lex(reflags=re.IGNORECASE)
    parser = yacc.yacc()
    lexer.lineno = 1

    return parser.parse(inp)


