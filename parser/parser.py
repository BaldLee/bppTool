import ply.lex as lex
import ply.yacc as yacc
from definition import *
from enum import Enum


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
    def __init__(self, src, act, dst):
        self.src = src
        self.act = act
        self.dst = dst

    def __str__(self):
        return '{ src: '+str(self.src)+', act: '+str(self.act)+', dst: '+str(self.dst)+' }'


class GrammarAtom:
    def __init__(self, vector, required):
        self.vector = vector
        self.required = required


class FormulaKind(Enum):
    ATOM = 0
    NEG = 1
    CONJ = 2
    DISJ = 3
    EA = 4
    AA = 5
    EG = 6
    AF = 7


class SimpleExp:
    def __init__(self, number, var):
        self.number = number
        self.var = var


class GrammarFormula:
    def __init__(self, kind, init):
        self.kind = kind
        self.atom = None
        self.neg = None
        self.conj = None
        self.disj = None
        self.ea = None
        self.aa = None
        self.eg = None
        self.af = None
        if(kind == FormulaKind.ATOM):
            self.atom = init
        if(kind == FormulaKind.NEG):
            self.neg = init
        if(kind == FormulaKind.CONJ):
            self.conj = init
        if(kind == FormulaKind.DISJ):
            self.disj = init
        if(kind == FormulaKind.EA):
            self.ea = init
        if(kind == FormulaKind.AA):
            self.aa = init
        if(kind == FormulaKind.EG):
            self.eg = init
        if(kind == FormulaKind.AF):
            self.af = init

    def get_formula(self):
        if(self.kind == FormulaKind.ATOM):
            return self.atom
        if(self.kind == FormulaKind.NEG):
            return self.neg
        if(self.kind == FormulaKind.CONJ):
            return self.conj
        if(self.kind == FormulaKind.DISJ):
            return self.disj
        if(self.kind == FormulaKind.EA):
            return self.ea
        if(self.kind == FormulaKind.AA):
            return self.aa
        if(self.kind == FormulaKind.EG):
            return self.eg
        if(self.kind == FormulaKind.AF):
            return self.af
        return None


class AtomFormula:
    def __init__(self, atom):
        self.atom = atom


class NegFormula:
    def __init__(self, subformula):
        self.subformula = subformula


class ConjFormula:
    def __init__(self, left, right):
        self.left = left
        self.right = right


class DisjFormula:
    def __init__(self, left, right):
        self.left = left
        self.right = right


class EaFormula:
    def __init__(self, action, subformula):
        self.action = action
        self.subformula = subformula


class AaFormula:
    def __init__(self, action, subformula):
        self.action = action
        self.subformula = subformula


class EgFormula:
    def __init__(self, subformula):
        self.subformula = subformula


class AfFormula:
    def __init__(self, subformula):
        self.subformula = subformula


class Input:
    def __init__(self, variables, actions, rules, start, eglogic, limit):
        self.variables = variables
        self.actions = actions
        self.rules = rules
        self.start = start
        self.eglogic = eglogic
        self.limit = limit

# def p_test(p):
#     'test : formula'
#     p[0] = p[1]


def p_input(p):
    'input : variables SEMICOLON actions SEMICOLON rules SEMICOLON VAR SEMICOLON eglogicformula SEMICOLON NUMBER'
    # print(p[7].get_formula().subformula.get_formula().left.get_formula().atom.vector[0].number)
    # print(p[7].eg.subformula.conj.left.atom.atom.vector[0].var)
    # print(p[7].eg.subformula.conj.left.atom.atom.vector[1].number)
    # print(p[7].eg.subformula.conj.left.atom.atom.vector[1].var)
    print(p[3])
    p[0] = Input(p[1], p[3], p[5], p[7], p[9], p[11])

# def p_input(p):
#     'input : eglogicformula'
#     print(p[1])
#     print(p[1].atom.atom.vector)
#     print(p[1].atom.atom.required)
#     p[0] = "aaa"


def p_variables_var(p):
    'variables : VAR'
    p[0] = []
    p[0].append(p[1])


def p_variables_combine(p):
    'variables : variables COMMA VAR'
    p[0] = p[1]
    p[0].append(p[3])


def p_actions_act(p):
    'actions : ACT'
    p[0] = []
    p[0].append(p[1])


def p_actions_combine(p):
    'actions : actions COMMA ACT'
    p[0] = p[1]
    p[1].append(p[3])


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


def p_exp_var(p):
    'exp : VAR'
    p[0] = SimpleExp(1, p[1])


def p_exp_numbervar(p):
    'exp : NUMBER VAR'
    p[0] = SimpleExp(p[1], p[2])

# def p_pulsexpes_var(p):
#     'plusexpes : VAR'
#     p[0] = []
#     p[0].append(p[1])

# def p_plusexpes_numbervar(p):
#     'plusexpes : NUMBER VAR'
#     p[0] = (p[1], p[2])


def p_plusexpes_simple(p):
    'plusexpes : exp'
    p[0] = []
    p[0].append(p[1])


def p_plusexpes_combine(p):
    'plusexpes : plusexpes PLUS exp'
    p[0] = p[1]
    p[0].append(p[3])


def p_formula_atom(p):
    'formula : atom'
    p[0] = GrammarFormula(FormulaKind.ATOM, AtomFormula(p[1]))


def p_formula_neg(p):
    'formula : NOT formula'
    p[0] = GrammarFormula(FormulaKind.NEG, NegFormula(p[2]))


def p_formula_conj(p):
    'formula : formula AND formula'
    p[0] = GrammarFormula(FormulaKind.CONJ, ConjFormula(p[1], p[3]))


def p_formula_disj(p):
    'formula : formula OR formula'
    p[0] = GrammarFormula(FormulaKind.DISJ, DisjFormula(p[1], p[3]))


def p_formula_ea(p):
    'formula : EA LPAREN ACT COMMA formula RPAREN'
    p[0] = GrammarFormula(FormulaKind.EA, EaFormula(p[3], p[5]))


def p_formula_aa(p):
    'formula : AA LPAREN ACT COMMA formula RPAREN'
    p[0] = GrammarFormula(FormulaKind.AA, AaFormula(p[3], p[5]))


def p_formula_eg(p):
    'formula : EG LPAREN formula RPAREN'
    p[0] = GrammarFormula(FormulaKind.EG, EgFormula(p[3]))


def p_formula_af(p):
    'formula : AF LPAREN formula RPAREN'
    p[0] = GrammarFormula(FormulaKind.AF, AfFormula(p[3]))


def p_formula_paren(p):
    'formula : LPAREN formula RPAREN'
    p[0] = p[2]


def p_eglogicformula(p):
    'eglogicformula : formula'
    p[0] = p[1]


# init parser
parser = yacc.yacc()

data = '''X,Y;
a,b;
[X,a,(Y)]
[Y,b,(X,Y)];
X;
Eg(X + 2Y >= 2 & Ea(a,X >= 1));
7'''


result = parser.parse(data, lexer=lexer)
print(result)

# Eg(X + Y >= 2 & Ea(a,X >= 1));
