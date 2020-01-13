import os
import random


def state_declare(state, process_num):
    return "%s = [Int('%s_%s) for i in range(%d)]\n"%(state, state, "%d' %i", process_num)


def atom_vector_mult(name, vector, value, process_num):
    projs = []
    for i in range(process_num):
        projs.append("%s[%d] * %d" %(name, i, vector[i]))
    return "atom_%s = %s >= %d\n" %(name, ' + '.join(projs), value)


def state_equal(state1, state2, process_num):
    projs = []
    for i in range(process_num):
        projs.append("%s[%d] == %s[%d]" %(state1, i, state2, i))
    return "And(%s)" %(', '.join(projs))


def state_positive(state, process_num):
    projs = []
    for i in range(process_num):
        projs.append("%s[%d] >= 0" %(state, i))
    return "And(%s)" %(', '.join(projs))


# generator for one transition
def generate_one_trans(rule, old_name, new_name, process_num):
    projs = []
    for j in range(process_num):
        if j == rule.left_index:
            projs.append("%s[%d] == %s[%d]-1+%d" %(new_name, j, old_name, j,rule.trans_vector[j]))
        else:
            projs.append("%s[%d] == %s[%d]+%d" %(new_name, j, old_name, j, rule.trans_vector[j]))
    # return "trans_%s_%d = And(%s)" %(old_name, i, ', '.join(projs))
    return "And(%s)" %(', '.join(projs))



def checking(file, state, k, formula, process_num, rules):
    random_upper_bound = k * 10000000000000000
    f = open(file, 'a+')
    op_name = formula.get_op_name()
    if op_name == "atom":
        f.write(atom_vector_mult(state, formula.vector, formula.required, process_num))
    elif op_name == "neg":
        f.close()
        checking(file, state, k, formula.subFormula, process_num, rules)
        f = open(file, 'a+')
        subFormula_type = formula.subFormula.get_op_name()
        f.write("neg_%s = Not(%s_%s)\n"%(state, subFormula_type, state))
    elif op_name == "conj":
        # the left formula
        left_name = "u%d" %(random.randint(0,random_upper_bound))
        f.write(state_declare(left_name, process_num))
        f.write("left_equal_%s = %s\n"%(state, state_equal(left_name, state, process_num)))
        # the right formula
        right_name = "u%d" %(random.randint(0,random_upper_bound))
        f.write(state_declare(right_name, process_num))
        f.write("right_equal_%s = %s\n"%(state, state_equal(right_name, state, process_num)))
        # check two subformula respectively
        f.close()
        checking(file, left_name, k, formula.left, process_num, rules)
        f = open(file, 'a+')
        f.close()
        checking(file, right_name, k, formula.right, process_num, rules)
        f = open(file, 'a+')
        left_formula_type = formula.left.get_op_name()
        right_formula_type = formula.right.get_op_name()
        f.write("conj_%s = And(%s_%s, %s_%s, left_equal_%s, right_equal_%s)\n"%(state, left_formula_type, left_name, right_formula_type, right_name, state, state))
    elif op_name == "ea":
        action = formula.action
        if rules == []:
            f.write("ea_%s = False\n"%state)
        else:
            index = random.randint(0,random_upper_bound)
            var_name = "u%d" %index
            f.write(state_declare(var_name, process_num))

            point_names = []
            for i in range(process_num):
                point_names.append("%s[%d]"%(var_name, i))
            point_names_join = ', '.join(point_names)
            i = 0
            all_possibles = []
            for rule in rules:
                act_cstr = "act_cstr_%s_%d"%(state, i)
                f.write("%s = %d == %d\n"%(act_cstr, action, rule.action))
                left_side_cstr = "left_side_cstr_%s_%d"%(state, i)
                f.write("%s = %s[%d] >= 1\n"%(left_side_cstr, state, rule.left_index))
                trans = "trans_%s_%d"%(state, i)
                f.write("%s = %s\n" %(trans, generate_one_trans(rule, state, var_name, process_num)))
                possi = "possi_%s_%d"%(state, i)
                f.write("%s = And(%s, %s, %s)\n" %(possi, act_cstr, left_side_cstr, trans))
                all_possibles.append("possi_%s_%d"%(state, i))
                i = i + 1
            all_possibles_join = ', '.join(all_possibles)
            f.write("bigDisj4ea_%s = Or(%s)\n" %(state, all_possibles_join))

            subFormula_type = formula.subFormula.get_op_name()
            f.close()
            checking(file, var_name, k, formula.subFormula, process_num, rules)
            f = open(file, 'a+')
            sub_cstr = "%s_%s"%(subFormula_type, var_name)
            exist_cstr = "Exists([%s], And(bigDisj4ea_%s, %s))"%(point_names_join,state, sub_cstr)
            f.write("ea_%s = And(%d >= 1, %s)\n"%(state, k, exist_cstr))
    elif op_name == "eg":
        var_names = []
        for j in range(k+1):
            index = random.randint(0,random_upper_bound)
            var_name = "u%d" %index
            var_names.append(var_name)
            f.write(state_declare(var_name, process_num))
        
        all_trans = []
        for j in range(1, k+1):
            old_var = var_names[j-1]
            new_var = var_names[j]
            all_possibles = []
            i = 0
            for rule in rules:
                left_side_cstr = "left_side_cstr_%s_%d"%(old_var, i)
                f.write("%s = %s[%d] >= 1\n"%(left_side_cstr, state, rule.left_index))
                trans = "trans_%s_%d"%(old_var, i)
                f.write("%s = %s\n" %(trans, generate_one_trans(rule, old_var, new_var, process_num)))
                possi = "possi_%s_%d"%(old_var, i)
                f.write("%s = And(%s, %s)\n" %(possi, left_side_cstr, trans))
                all_possibles.append("possi_%s_%d"%(old_var, i))
                i = i + 1
            all_possibles_join = ', '.join(all_possibles)
            f.write("bigDisj_%s = Or(%s)\n" %(old_var, all_possibles_join))
            all_trans.append("bigDisj_%s"%old_var)
        
        all_trans_join = ', '.join(all_trans)
        f.write("path_%s = And(%s)\n" %(state, all_trans_join))

        f.write("initial_%s = %s\n"%(state, state_equal(var_names[0], state, process_num)))
       
        subFormula_type = formula.subFormula.get_op_name()
        subFormula_cstr = []
        for var_name in var_names:
            subFormula_cstr.append("%s_%s"%(subFormula_type, var_name))
            f.close()
            checking(file, var_name, k, formula.subFormula, process_num, rules)
            f = open(file, 'a+')
        subFormula_cstr_join = ', '.join(subFormula_cstr)
        f.write("sub_bigConj_%s = And([%s])\n" %(state, subFormula_cstr_join))

        all_point_names = []
        for var_name in var_names:
            for i in range(process_num):
                all_point_names.append("%s[%d]"%(var_name, i))
        print(all_point_names)
        points_join = ', '.join(all_point_names)
        
        f.write("eg_%s = Exists([%s], And(path_%s, initial_%s, sub_bigConj_%s))\n"%(state, points_join, state, state, state))


def create(k, formula, process_num, rules):
    # global process_file
    process_file = "constraint.py"
    f = open(process_file, 'w+')

    # write the head codes
    f_head = open("head_codes.txt", 'r')
    head_codes_content = f_head.read()
    f.write(head_codes_content)
    f_head.close()
    f.close()

    # generate constraints according to the formula 
    checking(process_file, "u", k, formula, process_num, rules)

    # add the final constraint
    f = open(process_file, 'a+')
    formula_type = formula.get_op_name()
    f.write("\nt.add(%s_u)\n"%formula_type)

    # write the last codes
    f_last = open("last_codes.txt", 'r')
    last_codes_content = f_last.read()
    f.write(last_codes_content)
    f_last.close()
    f.close()

