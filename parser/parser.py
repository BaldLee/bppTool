import ply.lex as lex
import ply.yacc as yacc
from definition import *

#
#
#           Lex Analysis
#
#

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


#
#
#         Grammar Analysis
#
#

class GrammarRule:
    def __init__(self, s, a, d):
        self.src = s
        self.act = a
        self.dst = d

    def __str__(self):
        return '{ src: '+str(self.src)+', act: '+str(self.act)+', dst: '+str(self.dst)+' }'


class GrammarAtom:
    def __init__(self, v, r):
        self.vec = v
        self.required = r

# def p_input(p):
#     'input : variables SEMICOLON rules SEMICOLON VAR SEMICOLON eglogicformula SEMICOLON NUMBER'
#     print(0)


def p_test(p):
    'test : atom'
    p[0] = p[1]


def p_variables_var(p):
    'variables : VAR'
    p[0] = []
    p[0].append(p[1])


def p_variables_combine(p):
    'variables : variables COMMA VAR'
    p[0] = p[1]
    p[0].append(p[3])


def p_rules_rule(p):
    'rules : rule'
    p[0] = []
    p[0].append(p[1])


def p_rules_combine(p):
    'rules : rules rule'
    p[0] = p[1]
    p[0].append(p[2])


def p_rule(p):
    'rule : LBRACK VAR COMMA ACT COMMA LPAREN variables RPAREN RBRACK'
    p[0] = GrammarRule(p[2], p[4], p[7])


def p_atom(p):
    'atom : plusexpes GE NUMBER'
    p[0] = GrammarAtom(p[1], p[3])


def p_pulsexpes_var(p):
    'plusexpes : VAR'
    p[0] = [p[1]]


def p_plusexpes_combine(p):
    'plusexpes : plusexpes PLUS VAR'
    p[0] = p[1]
    p[0].append(p[3])


# init parser
parser = yacc.yacc()

data = '''

'''

result = parser.parse(data, lexer=lexer)
print(result)
print(result.vec)
print(result.required)