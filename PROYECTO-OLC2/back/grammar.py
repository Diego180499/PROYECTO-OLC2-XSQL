import re

from error.xsql_error import xsql_error

# here start grammar
# --------------------------------------------------------------
# 04-06-2023: Created by Daniel Morales
# proyecto 1 - compiladores 2 usac 2023
# --------------------------------------------------------------
# Definimos las palabras reservadas de nuestro lenguaje
global_arr = []
errores_sintacticos = []


def get_errores():
    return errores_sintacticos


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
    'reference': 'REFERENCE',
    'add': 'ADD',
    'int': 'INT',
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
    'cas': 'CAS',
    'set': 'SET',
    'while': 'WHILE',
    'delete': 'DELETE'
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
             'DIVIDE',
             'POINT'  ### maked by diego xd
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
t_POINT = r'\.'    ### maked by diego xd

# Expresiones Regulares de las cadenas con "" o ''
def t_STRING(t):
    r'(\"(\\\'|\\"|\\\\|\\n|\\t|[^\'\\\"])*?\")|(\'(\\\'|\\"|\\\\|\\n|\\t|[^\'\\\"])*?\')'
    t.value = t.value[1:-1]  # remuevo las comillas

    # print(str(t.value))
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
    # print('find an integer:', t.value)
    return t


# Expresion Regular para IDS
def t_ID(t):
    r'@[a-zA-Z][a-zA-Z_0-9]*'
    t.type = reservadas.get(t.value, 'ID')
    return t


# ignorar espacios
t_ignore = " \t"


# Expresion regular para los nombre de las tablas, bases de datos, columnas
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
from models.VariableType import VariableType
from models.ValueType import ValueType
from models.Value import Value
from models.DeclareStatement import DeclareStatement
from models.UnaryOperation import UnaryOperation
from models.OperationType import OperationType
from models.BinaryOperation import BinaryOperation
from models.SetStatement import SetStatement
from models.Assignment import Assignment
from models.ElseStatement import ElseStatement
from models.WhenStatement import WhenStatement
from models.IfStatement import IfStatement
from models.WhileStatement import WhileStatement


sys.setrecursionlimit(10000000)


def p_init(t):
    'init   : statements'
    t[0] = t[1]


def p_statements(t):
    'statements : statements statement'
    t[1].append(t[2])
    t[0] = t[1]


def p_statements_2(t):
    'statements : '
    t[0] = []


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
                    | update_statement
                    | while_statement
                    | truncate_statement
                    | delete_statement'''
    t[0] = t[1]


##### CREATE DATABASE #####

def p_create_database_statement(t):
    'create_database_statement    : CREATE DATA BASE NAME SEMICOLON'


#### USE ####

def p_use_statement(t):
    'use_statement   : USE NAME SEMICOLON'


#### DECLARE ####

def p_declare_statement(t):
    'declare_statement   : DECLARE ID AS type SEMICOLON'
    t[0] = DeclareStatement(t.lineno(1), find_column(input, t.slice[1]), t[2], t[4])

def p_declare_statement_2(t):
    'declare_statement   : DECLARE ID  type SEMICOLON'
    t[0] = DeclareStatement(t.lineno(1), find_column(input, t.slice[1]), t[2], t[3])

#### SET ####

def p_set_statement(t):
    'set_statement   : SET assignments SEMICOLON'
    t[0] = SetStatement(t.lineno(1), find_column(input, t.slice[1]), t[2])


def p_assignments(t):
    'assignments    : assignments COMMA ID ASSIGN a'
    t[1].append(Assignment(t.lineno(1), find_column(input, t.slice[2]), t[3], t[5]))
    t[0] = t[1]


def p_assignments_2(t):
    'assignments    : ID ASSIGN a'
    t[0] = []
    t[0].append(Assignment(t.lineno(1), find_column(input, t.slice[2]), t[1], t[3]))


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

#### INSERT ####

def p_insert_statement(t):
    'insert_statement   : INSERT INTO NAME L_PAREN columns R_PAREN VALUES L_PAREN vals R_PAREN SEMICOLON'


#### COLUMNS AND VALS PRODS ####

def p_columns(t):
    'columns    : columns COMMA column'


def p_columns_2(t):
    'columns    : columns COMMA column POINT column'

def p_columns_3(t):
    'columns    : column POINT column'

def p_columns_4(t):
    'columns    : column'

def p_column(t):
    """column   : TIMES
                | NAME
                | case_statement
                | call_function_prod
                | a NAME"""  #### pueden haber columnas a las que se le asignan un valor, que sería 'a' maked by diego xd"""
    t[0] = t[1]


def p_vals(t):
    'vals   : vals COMMA a'


def p_vals_2(t):
    'vals   : a'


#### CREATE FUNCTION AND PROCEDURE ####

def p_create_function_statement(t):
    'create_function_statement  : CREATE FUNCTION NAME L_PAREN parameters R_PAREN RETURN type AS BEGIN statements END SEMICOLON'


def p_create_procedure_statement(t):
    'create_procedure_statement : CREATE PROCEDURE NAME L_PAREN parameters R_PAREN AS BEGIN statements RETURN a END SEMICOLON'


def p_parameters(t):
    'parameters : parameters COMMA ID AS type'

def p_parameters_2(t):
    'parameters : parameters COMMA ID type'

def p_parameters_3(t):
    'parameters : ID AS type'

def p_parameters_4(t):
    'parameters : ID  type'



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
    'if_statement   : IF a THEN statements END IF SEMICOLON'
    t[0] = IfStatement(t.lineno(1), find_column(input, t.slice[1]), t[2], t[4], None)


def p_if_statement_2(t):
    'if_statement   : IF a THEN statements ELSE statements END IF SEMICOLON'
    t[0] = IfStatement(t.lineno(1), find_column(input, t.slice[1]), t[2], t[4], t[6])



def p_if_statement_3(t):
    'if_statement   : IF L_PAREN a COMMA a COMMA a R_PAREN SEMICOLON'
    t[0] = IfStatement(t.lineno(1), find_column(input, t.slice[1]), t[3], [t[5]], [t[7]])

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


#### WHILE STATEMENT ####
def p_while_statement(t):
    'while_statement    : WHILE a BEGIN statements END SEMICOLON'
    t[0] = WhileStatement(t.lineno(1), find_column(input, t.slice[1]), t[2], t[4])


### TRUNCATE TABLE STATEMENT ###
def p_truncate_statement(t):
    'truncate_statement : TRUNCATE TABLE NAME SEMICOLON'


### DELETE STATEMENT ###
def p_delete_statement(t):
    'delete_statement : DELETE FROM NAME WHERE a SEMICOLON'


### CASE STATEMENT ###
def p_case_statement(t):
    'case_statement : CASE when_statements END NAME'
    t[0] = t[2]

def p_when_statement(t):
    'when_statements : WHEN a THEN a when_statements'
    t[0] = WhenStatement(t.lineno(1), find_column(input, t.slice[1]), t[2], t[4], t[5])

def p_when_statement_2(t):
    'when_statements : ELSE THEN a'
    t[0] = ElseStatement(t.lineno(1), find_column(input, t.slice[1]), t[3])

def p_type(t):
    '''type : INT
            | DECIMAL
            | DATE
            | DATETIME'''

    t[0] = VariableType(t[1], 32)


def p_type_2(t):
    """type : NCHAR L_PAREN a R_PAREN
            | NVARCHAR L_PAREN a R_PAREN"""
    t[0] = VariableType(t[1], t[3])

def p_a(t):
    '''a    : a OR b'''
    t[0] = BinaryOperation(t.lineno(1), find_column(input, t.slice[2]), t[1], t[3], t[2])


def p_a_2(t):
    'a  : b'
    t[0] = t[1]


def p_b(t):
    'b  : b AND c'
    t[0] = BinaryOperation(t.lineno(1), find_column(input, t.slice[2]), t[1], t[3], t[2])


def p_b_2(t):
    'b  : c'
    t[0] = t[1]


def p_c(t):
    'c  : NOT_SIGN d'
    t[0] = UnaryOperation(t.lineno(1), find_column(input, t.slice[1]), t[2], OperationType.NOT)


def p_c_2(t):
    'c  : d'
    t[0] = t[1]


def p_d(t):
    """d    : d EQUALS e
            | d NOT_EQ e
            | d LESS_THAN e
            | d GREATER_THAN e
            | d LESS_EQ e
            | d GREATER_EQ e
    """
    t[0] = BinaryOperation(t.lineno(1), find_column(input, t.slice[2]), t[1], t[3], t[2])


def p_d_2(t):
    'd  : e'
    t[0] = t[1]


def p_e(t):
    """e    : e PLUS f
            | e MINUS f"""
    t[0] = BinaryOperation(t.lineno(1), find_column(input, t.slice[2]), t[1], t[3], t[2])


def p_e_2(t):
    'e  : f'
    t[0] = t[1]


def p_f(t):
    """f    : f TIMES g
            | f DIVIDE g"""
    t[0] = BinaryOperation(t.lineno(1), find_column(input, t.slice[2]), t[1], t[3], t[2])


def p_f_2(t):
    'f  : g'
    t[0] = t[1]


def p_g(t):
    'g  : MINUS h'
    t[0] = UnaryOperation(t.lineno(1), find_column(input, t.slice[1]), t[2], OperationType.MINUS)


def p_g_2(t):
    'g  : h'
    t[0] = t[1]


def p_h(t):
    """h    : INTEGER_VALUE"""
    t[0] = Value(t.lineno(1), find_column(input, t.slice[1]), t[1], ValueType.INTEGER_VALUE)


def p_h_2(t):
    """h    : DECIMAL_VALUE"""
    t[0] = Value(t.lineno(1), find_column(input, t.slice[1]), t[1], ValueType.DECIMAL_VALUE)


def p_h_3(t):
    """h    : STRING"""
    t[0] = Value(t.lineno(1), find_column(input, t.slice[1]), t[1], ValueType.STRING)


def p_h_4(t):
    """h    : ID"""
    t[0] = Value(t.lineno(1), find_column(input, t.slice[1]), t[1], ValueType.ID)


def p_h_5(t):
    """h    : NAME"""
    t[0] = Value(t.lineno(1), find_column(input, t.slice[1]), t[1], ValueType.COLUMN)

def p_h_6(t):
    """h    : if_statement"""
    t[0] = t[1]

def p_call_function_prod(t):
    """call_function_prod   : HOY L_PAREN R_PAREN
                            | CONCATENAR L_PAREN a COMMA a R_PAREN
                            | SUBSTRAER L_PAREN a R_PAREN
                            | CONTAR L_PAREN a R_PAREN
                            | SUMA L_PAREN a R_PAREN
                            | CAS L_PAREN a AS type R_PAREN
    """


def p_error(t):
    error = xsql_error("Error sintactico", t.value, t.type, t.lineno - 1)
    errores_sintacticos.append(error)
    # print("Error sintáctico en '%s'" % t.value+" "+ t.type)
    # print(f'en linea {t.lineno-1}')
    # if t is not None:
    # global_arr.append(ExceptionPyType("ERROR SINTACTICO en " + str(t.value) + " SE ESPERABA ALGO MAS", t.lexer.lineno, find_column(input, t)))


import ply.yacc as yacc


def parse(inp):
    global parser
    global lexer
    lexer = lex.lex(reflags=re.IGNORECASE)
    parser = yacc.yacc()
    lexer.lineno = 1
    result = parser.parse(inp)
    # print(errores_sintacticos)

    return result
