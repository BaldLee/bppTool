import os
from smt_generator import create
from structure import formula, process_num, rules, bound_k

def check():
    create(bound_k, formula, process_num, rules)
    os.system("python3 constraint.py")


if __name__ == '__main__':
    check()