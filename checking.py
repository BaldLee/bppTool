import os
from smt_generator import create, generate_one_trans
from structure import formula, process_num, rules, bound_k

def check():
    print(generate_one_trans(rules[0], 'S', 'T', process_num))
    create(bound_k, formula, process_num, rules)
    os.system("python3 constraint.py")
    

if __name__ == '__main__':
    check()