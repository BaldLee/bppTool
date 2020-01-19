from definition import *

process_num = 2

rule_num = 2

rule0 = Rule(0, 5, [0, 1]) # [X, a, (Y)]
rule0.pretty_print() # X_0 -> 5 -> X_1

rule1 = Rule(1, 10, [2, 0]) # [Y, b, (X, X)]
rule1.pretty_print() # X_1 -> 10 -> X_0X_0

rules = [rule0, rule1]

initial_expr = [1, 0] # X

formula = EG(EX(5, Atom([1, 1], 2))) # EG(E(a, (X + Y >= 2))) 
formula.show() # EG (E<5> (X_0 * 1 + X_1 * 1 >= 2))
Atom([1, 0], 3).show() # X_0 * 1 >= 3

bound_k = 15