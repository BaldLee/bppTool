from definition import *

process_num = 2

rule_num = 2
rule0 = Rule(1, 10, [0, 1])
rule1 = Rule(1, 5, [2, 0])
rules = [rule0, rule1]

initial_expr = [1, 0]
formula = EG(Ea(5, Atom([0, 1, 1], 2)))

bound_k = 15