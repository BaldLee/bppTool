from parser.translate import *

print("> process_num: " + str(process_num))
print("> rule_num: " + str(rule_num))
print("> rules: ")
for rule in rules:
    rule.pretty_print()
print("> initial_expr: " + str(initial_expr))
print("> formula: ")
formula.show()
print("> bound_k: " + str(bound_k))