import ply.lex as lex
import ply.yacc as yacc

tokens = [
    'EG',
    'AF',
    'EA',
    'AA',
    'VAR',
    'ACT',
    'NUMBER',
    'COMMA',
    'SEMICOLON',
    'NOT',
    'AND',
    'OR',
    'PLUS',
    'MINUS',
    'GE',
    'LPAREN',
    'RPAREN',
    'LBRACK',
    'RBRACK',
    'LBRACE',
    'RBRACE'
]

# tokens defination


def t_EG(t):
    r'Eg'
    return t


def t_AF(t):
    r'Af'
    return t


def t_EA(t):
    r'Ea'
    return t


def t_AA(t):
    r'Aa'
    return t


t_VAR = r'[A-Z][A-Z0-9]*'
t_ACT = r'[a-z][a-z0-9]*'


def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t


t_COMMA = ','
t_SEMICOLON = ';'
t_NOT = '!'
t_AND = '&'
t_OR = '\|'
t_PLUS = '\+'
t_MINUS = '-'
t_GE = '>='
t_LPAREN = '\('
t_RPAREN = '\)'
t_LBRACK = '\['
t_RBRACK = '\]'
t_LBRACE = '\{'
t_RBRACE = '\}'

t_ignore = ' \t'  # ignore tokens


def t_newline(t):  # newline token
    r'\n+'
    t.lexer.lineno += len(t.value)


def t_error(t):  # error handler
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


# init lexer
lexer = lex.lex()

data = ''''''

lexer.input(data)
for token in lexer:
    print(token)
