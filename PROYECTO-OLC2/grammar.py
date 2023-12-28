import re

from src.error.xsql_error import xsql_error

global_arr = []
errores_sintacticos = []
matriz_resultante = []

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
    'concatena': 'CONCATENA',
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
             'DOT'  ### maked by diego xd
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
t_DOT = r'\.'    ### maked by diego xd

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
    t.type = reservadas.get(t.value.lower(), 'NAME')
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
from src.models.VariableType import VariableType
from src.models.ValueType import ValueType
from src.models.Value import Value
from src.models.DeclareStatement import DeclareStatement
from src.models.UnaryOperation import UnaryOperation
from src.models.OperationType import OperationType
from src.models.BinaryOperation import BinaryOperation
from src.models.SetStatement import SetStatement
from src.models.Assignment import Assignment
from src.models.ElseStatement import ElseStatement
from src.models.WhenStatement import WhenStatement
from src.models.IfStatement import IfStatement
from src.models.WhileStatement import WhileStatement
from src.models.FunctionStatement import FunctionStatement
from src.models.ProcedureStatement import ProcedureStatement
from src.models.ParameterStatement import ParameterStatement
from src.models.ReturnStatement import ReturnStatement
from src.models.ExecStatement import ExecStatement
from src.models.CallFunctionStatement import CallFunctionStatement
from src.models.CasStatement import CasStatement
from src.models.OrdenEjecucion import OrdenEjecucion
from src.models.CreateDBStatement import CreateDBStatement
from src.models.UseStatement import UseStatement
from src.models.CreateTableStatement import CreateTableStatement
from src.models.TableProperty import TableProperty
from src.models.AlterTableStatement import AlterTableStatement
from src.models.DropTableStatement import DropTableStatement
from src.models.TruncateTableStatement import TruncateTableStatement
from src.models.InsertStatement import InsertStatement
from src.models.SelectStatement import SelectStatement
from src.models.TableColumn import TableColumn
from src.models.DeleteStatement import DeleteStatement
from src.models.UpdateStatement import UpdateStatement
from src.models.EOF import EOF

sys.setrecursionlimit(10000000)


def p_init(t):
    'init   : statements'
    t[0] = t[1]


def p_statements(t):
    'statements : statements statement'
    # t[1].append(t[2])
    # t[0] = t[1]
    ordEje:OrdenEjecucion = t[1]
    ordEje.right = t[2]
    ordenEjecucion = OrdenEjecucion(0, 0, ordEje, None)
    t[0] = ordenEjecucion


def p_statements_2(t):
    'statements : statement'
    # t[0] = []
    eof = EOF(0, 0)
    t[0] = OrdenEjecucion(0, 0, t[1], eof)


def p_statement(t):
    '''statement    : create_database_statement SEMICOLON
                    | use_statement SEMICOLON
                    | declare_statement SEMICOLON
                    | set_statement SEMICOLON
                    | create_table_statement SEMICOLON
                    | select_statement SEMICOLON
                    | insert_statement SEMICOLON
                    | create_function_statement SEMICOLON
                    | create_procedure_statement SEMICOLON
                    | call_function_statement SEMICOLON
                    | alter_table_statement SEMICOLON
                    | if_statement SEMICOLON
                    | exec_statement SEMICOLON
                    | drop_table_statement SEMICOLON
                    | update_statement SEMICOLON
                    | while_statement SEMICOLON
                    | truncate_statement SEMICOLON
                    | return_statement SEMICOLON
                    | delete_statement SEMICOLON'''
    t[0] = t[1]


##### CREATE DATABASE #####

def p_create_database_statement(t):
    'create_database_statement    : CREATE DATA BASE NAME'
    t[0] = CreateDBStatement(t.lineno(1), find_column(input, t.slice[1]), t[4])


#### USE ####

def p_use_statement(t):
    'use_statement   : USE NAME'
    t[0] = UseStatement(t.lineno(1), find_column(input, t.slice[1]), t[2])


#### DECLARE ####

def p_declare_statement(t):
    'declare_statement   : DECLARE ID AS type'
    t[0] = DeclareStatement(t.lineno(1), find_column(input, t.slice[1]), t[2], t[4])

def p_declare_statement_2(t):
    'declare_statement   : DECLARE ID  type'
    t[0] = DeclareStatement(t.lineno(1), find_column(input, t.slice[1]), t[2], t[3])

#### SET ####

def p_set_statement(t):
    'set_statement   : SET assignments'
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
    'create_table_statement : CREATE TABLE NAME L_PAREN properties R_PAREN'
    t[0] = CreateTableStatement(t.lineno(1), find_column(input, t.slice[1]), t[3], t[5])


def p_properties(t):
    'properties : properties COMMA property'
    t[0] = t[1]
    t[0].append(t[3])


def p_properties_2(t):
    'properties : property'
    t[0] = []
    t[0].append(t[1])


def p_property(t):
    'property   : NAME type null_prod PRIMARY KEY'
    t[0] = TableProperty(t.lineno(1), find_column(input, t.slice[1]), t[1], t[2], t[3], True, "-", "-")


def p_property_2(t):
    'property   : NAME type null_prod'
    t[0] = TableProperty(t.lineno(1), find_column(input, t.slice[1]), t[1], t[2], t[3], False, "-", "-")


def p_property_3(t):
    'property   : NAME type null_prod REFERENCE NAME L_PAREN NAME R_PAREN'
    t[0] = TableProperty(t.lineno(1), find_column(input, t.slice[1]), t[1], t[2], t[3], False, t[5], t[7])


def p_null_prod(t):
    'null_prod  : NOT NULL'
    t[0] = False


def p_null_prod_2(t):
    'null_prod  : NULL'
    t[0] = True


def p_null_prod_3(t):
    'null_prod  : '
    t[0] = True


#### SELECT ####

def p_select_statement(t):
    'select_statement   : SELECT columns FROM NAME'
    t[0] = SelectStatement(t.lineno(1), find_column(input, t.slice[1]), t[2], t[4], None)


def p_select_statement_2(t):
    'select_statement   : SELECT columns FROM NAME WHERE a'
    t[0] = SelectStatement(t.lineno(1), find_column(input, t.slice[1]), t[2], t[4], t[6])


# def p_select_statement_3(t):
#     'select_statement : SELECT columns FROM table_names_select WHERE a'
#
# def p_select_statement_4(t):
#     'select_statement : SELECT columns FROM table_names_select'
#
# def p_lista_names_select(t):
#     'table_names_select : NAME table_names_select_p'
#
# def p_lista_names_select_2(t):
#     ''' table_names_select_p : COMMA NAME table_names_select_p
#                             |'''


#### INSERT ####

def p_insert_statement(t):
    'insert_statement   : INSERT INTO NAME L_PAREN column_names R_PAREN VALUES L_PAREN vals R_PAREN'
    t[0] = InsertStatement(t.lineno(1), find_column(input, t.slice[1]), t[3], t[5], t[9])

def p_column_names(t):
    'column_names   : column_names COMMA NAME'
    t[0] = t[1]
    t[0].append(t[3])

def p_column_names_2(t):
    'column_names   : NAME'
    t[0] = []
    t[0].append(t[1])

#### COLUMNS AND VALS PRODS ####

def p_columns(t):
    'columns    : columns COMMA column'
    t[0] = t[1]
    t[0].append(t[3])


def p_columns_2(t):
    'columns    : column'
    t[0] = []
    t[0].append(t[1])

def p_column(t):
    """column   : TIMES"""  #### | a NAME pueden haber columnas a las que se le asignan un valor, que sería 'a' maked by diego xd"""
    t[0] = TableColumn(t.lineno(1), t.slice[1], None, t[1], None)


def p_column_2(t):
    "column : NAME"
    value = Value(t.lineno(1), t.slice[1], t[1], ValueType().COLUMN)
    t[0] = TableColumn(t.lineno(1), t.slice[1], None, t[1], value)

def p_column_3(t):
    "column : NAME DOT NAME"
    value = Value(t.lineno(1), t.slice[3], t[3], ValueType().COLUMN)
    t[0] = TableColumn(t.lineno(1), t.slice[1], t[1], t[3], value)


def p_column_4(t):
    """column   : case_statement NAME
                | a NAME
                | if_statement NAME"""
    t[0] = TableColumn(t.lineno(1), t.slice[2], None, t[2], t[1])

def p_vals(t):
    'vals   : vals COMMA a'
    t[0] = t[1]
    t[0].append(t[3])


def p_vals_2(t):
    'vals   : a'
    t[0] = []
    t[0].append(t[1])


#### CREATE FUNCTION AND PROCEDURE ####

def p_create_function_statement(t):
    'create_function_statement  : CREATE FUNCTION NAME L_PAREN parameters R_PAREN RETURN type AS BEGIN statements END'
    t[0] = FunctionStatement(t.lineno(1), find_column(input, t.slice[1]), t[3], t[5], t[11], t[8])

def p_create_function_statement_2(t):
    'create_function_statement  : CREATE FUNCTION NAME L_PAREN R_PAREN RETURN type AS BEGIN statements END'
    t[0] = FunctionStatement(t.lineno(1), find_column(input, t.slice[1]), t[3], [], t[10], t[7])

def p_create_procedure_statement(t):
    'create_procedure_statement : CREATE PROCEDURE NAME L_PAREN parameters R_PAREN AS BEGIN statements END'
    t[0] = ProcedureStatement(t.lineno(1), find_column(input, t.slice[1]), t[3], t[5], t[9])

def p_create_procedure_statement_2(t):
    'create_procedure_statement : CREATE PROCEDURE NAME L_PAREN R_PAREN AS BEGIN statements END'
    t[0] = ProcedureStatement(t.lineno(1), find_column(input, t.slice[1]), t[3], [], t[8])



def p_parameters(t):
    'parameters : parameters COMMA ID AS type'
    t[0] = t[1]
    t[0].append(ParameterStatement(t.lineno(1), find_column(input, t.slice[2]), t[3], t[5]))


def p_parameters_2(t):
    'parameters : parameters COMMA ID type'
    t[0] = t[1]
    t[0].append(ParameterStatement(t.lineno(1), find_column(input, t.slice[2]), t[3], t[4]))

def p_parameters_3(t):
    'parameters : ID type'
    t[0] = []
    t[0].append(ParameterStatement(t.lineno(1), find_column(input, t.slice[1]), t[1], t[2]))

def p_parameters_4(t):
    'parameters : ID AS type'
    t[0] = []
    t[0].append(ParameterStatement(t.lineno(1), find_column(input, t.slice[1]), t[1], t[3]))




#### ALTER TABLE, FUNCTION AND PROCEDURE ####
def p_alter_table_statement(t):
    'alter_table_statement  : ALTER TABLE NAME ADD COLUMN NAME type'
    t[0] = AlterTableStatement(t.lineno(1), find_column(input, t.slice[1]), t[3], t[6], t[7], 'add')


def p_alter_table_statement_2(t):
    'alter_table_statement  : ALTER TABLE NAME DROP COLUMN NAME'
    t[0] = AlterTableStatement(t.lineno(1), find_column(input, t.slice[1]), t[3], t[6], None, 'drop')


#### IF STATEMENT ####
def p_if_statement(t):
    'if_statement   : IF a THEN statements END IF'
    t[0] = IfStatement(t.lineno(1), find_column(input, t.slice[1]), t[2], t[4], None)


def p_if_statement_2(t):
    'if_statement   : IF a THEN statements ELSE statements END IF'
    t[0] = IfStatement(t.lineno(1), find_column(input, t.slice[1]), t[2], t[4], t[6])



def p_if_statement_3(t):
    'if_statement   : IF L_PAREN a COMMA a COMMA a R_PAREN'
    t[0] = IfStatement(t.lineno(1), find_column(input, t.slice[1]), t[3], t[5], t[7])

#### EXEC ####
def p_exec_statement(t):
    'exec_statement : EXEC NAME vals'
    t[0] = ExecStatement(t.lineno(1), find_column(input, t.slice[1]), t[2], t[3])



def p_exec_statement_2(t):
    'exec_statement : EXEC NAME args'
    t[0] = ExecStatement(t.lineno(1), find_column(input, t.slice[1]), t[2], t[3])



def p_exec_statement_3(t):
    'exec_statement : EXEC NAME'
    t[0] = ExecStatement(t.lineno(1), find_column(input, t.slice[1]), t[2], [])

def p_args(t):
    'args   : args COMMA ID ASSIGN a'
    t[0] = t[1]
    t[0].append(Assignment(t.lineno(1), find_column(input, t.slice[2]), t[3], t[5]))

def p_args_2(t):
    'args   : ID ASSIGN a'
    t[0] = []
    t[0].append(Assignment(t.lineno(1), find_column(input, t.slice[1]), t[1], t[3]))


#### DROP TABLE ####
def p_drop_table_statement(t):
    'drop_table_statement   : DROP TABLE NAME'
    t[0] = DropTableStatement(t.lineno(1), find_column(input, t.slice[1]), t[3])


#### UPDATE STATEMENT ####
def p_update_statement(t):
    'update_statement   : UPDATE NAME SET column_assignments WHERE a'
    t[0] = UpdateStatement(t.lineno(1), find_column(input, t.slice[1]), t[2], t[4], t[6])


#### COLUMN aSSIGNMENTS ####
def p_column_assignments(t):
    'column_assignments  : column_assignments COMMA NAME ASSIGN a'
    t[0] = t[1]
    assignment = Assignment(t.lineno(1), find_column(input, t.slice[2]), t[3], t[5])
    t[0].append(assignment)


def p_column_assignments_2(t):
    'column_assignments : NAME ASSIGN a'
    assignment = Assignment(t.lineno(1), find_column(input, t.slice[1]), t[1], t[3])
    t[0] = []
    t[0].append(assignment)


#### WHILE STATEMENT ####
def p_while_statement(t):
    'while_statement    : WHILE a BEGIN statements END'
    t[0] = WhileStatement(t.lineno(1), find_column(input, t.slice[1]), t[2], t[4])


### TRUNCATE TABLE STATEMENT ###
def p_truncate_statement(t):
    'truncate_statement : TRUNCATE TABLE NAME'
    t[0] = TruncateTableStatement(t.lineno(1), find_column(input, t.slice[1]), t[3])


### DELETE STATEMENT ###
def p_delete_statement(t):
    'delete_statement : DELETE FROM NAME WHERE a'
    t[0] = DeleteStatement(t.lineno(1), find_column(input, t.slice[1]), t[3], t[5])


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
    """h    : L_PAREN a R_PAREN"""
    t[0] = t[2]

def p_h_7(t):
    """h    : exec_statement
            | call_function_statement"""
    t[0] = t[1]

def p_call_function_statement(t):
    """call_function_statement   : function_name_prod L_PAREN vals R_PAREN"""
    t[0] = CallFunctionStatement(t.lineno(1), find_column(input, t.slice[2]), t[1], t[3])


def p_call_function_statement_2(t):
    "call_function_statement : function_name_prod L_PAREN R_PAREN"
    t[0] = CallFunctionStatement(t.lineno(1), find_column(input, t.slice[2]), t[1], [])

def p_call_function_statement_3(t):
    "call_function_statement    : CAS L_PAREN a AS type R_PAREN"
    t[0] = CasStatement(t.lineno(1), find_column(input, t.slice[1]), t[3], t[5])

def p_function_name_prod(t):
    """function_name_prod   : HOY
                            | CONCATENA
                            | SUBSTRAER
                            | CONTAR
                            | SUMA
    """
    t[0] = t[1]

def p_return_statement(t):
    """return_statement : RETURN a"""
    t[0] = ReturnStatement(t.lineno(1), find_column(input, t.slice[1]), t[2])


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

#####
def limpiar_lista_errores():
    for error_sintactico in errores_sintacticos :
        errores_sintacticos.remove(error_sintactico)

def obtener_matriz_resultante():
    return matriz_resultante