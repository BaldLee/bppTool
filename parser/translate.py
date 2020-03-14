from parser.parser import *
from definition import *
# print("### translate ###")

# init dicionaries
varDict = {}
actDict = {}

acc = 0
for item in result.variables:
    varDict[item] = acc
    acc += 1

acc = 5
for item in result.actions:
    actDict[item] = acc
    acc += 5


# tool function


def translate_formula(f):
    formula = f.get_formula()
    if(f.kind == FormulaKind.ATOM):
        atom = formula.atom
        vec = [0 for x in range(0, process_num)]
        for item in atom.vector:
            vec[varDict[item.var]] = item.number
        req = atom.required
        return Atom(vec, req)
    if(f.kind == FormulaKind.NEG):
        return Neg(translate_formula(formula.subFormula))
    if(f.kind == FormulaKind.CONJ):
        return Conj(translate_formula(formula.left), translate_formula(formula.right))
    if(f.kind == FormulaKind.DISJ):
        return Disj(translate_formula(formula.left), translate_formula(formula.right))
    if(f.kind == FormulaKind.EA):
        return EX(actDict[formula.action], translate_formula(formula.subformula))
    if(f.kind == FormulaKind.AA):
        return AX(actDict[formula.action], translate_formula(formula.subformula))
    if(f.kind == FormulaKind.EG):
        return EG(translate_formula(formula.subformula))
    if(f.kind == FormulaKind.AF):
        return AF(translate_formula(formula.subformula))


# set process_num
process_num = len(varDict)

# set rule_num
rule_num = len(result.rules)

# init rules
rules = []
for item in result.rules:
    src = varDict[item.src]
    act = actDict[item.act]
    dst = [0 for x in range(0, process_num)]
    for x in item.dst:
        dst[varDict[x]] = 1
    rules.append(Rule(src, act, dst))

# set initial_expr
initial_expr = [0 for x in range(0, process_num)]
initial_expr[varDict[result.start]] = 1

# set formula
formula = translate_formula(result.eglogic)

# set bound_k
bound_k = result.limit


# print stuff
# print("> process_num: " + str(process_num))
# print("> rule_num: " + str(rule_num))
# print("> rules: ")
# for rule in rules:
#     rule.pretty_print()
# print("> initial_expr: " + str(initial_expr))
# print("> formula: ")
# formula.show()
# print("> bound_k: " + str(bound_k))
