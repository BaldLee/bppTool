class Rule:
    def __init__(self, left_index, action, trans_vector):
        self.left_index = left_index
        self.action = action
        self.trans_vector = trans_vector
    def pretty_print(self):
        part0 = "X_%d -> %s -> " %(self.left_index, self.action)
        part1 = ""
        for i in range(len(self.trans_vector)):
            part1 += ("X_%d" %i) * self.trans_vector[i]
        print(part0 + part1)
    def show4solving(self):
        return "Rule(%s, '%s', %s)" %(self.left_index, self.action, self.trans_vector)


class Atom:
    def __init__(self, vector, required):
        self.vector = vector
        self.required = required
    def get_op_name(self):
        return "atom"
    # def get_print_result(self):
    #     return "X_%d >= %d" %(self.index, self.required)
    def show(self):
        print(self.get_print_result())

class Neg:
    def __init__(self, subFormula):
        self.subFormula = subFormula
    def get_op_name(self):
        return "neg"
    def get_print_result(self):
        return "neg (%s)" %(self.subFormula.get_print_result())
    def show(self):
        print(self.get_print_result())

class Conj:
    def __init__(self, left, right):
        self.left = left
        self.right = right
    def get_op_name(self):
        return "conj"
    def get_print_result(self):
        return "conj (%s, %s)" %(self.left.get_print_result(), self.right.get_print_result())
    def show(self):
        print(self.get_print_result())

class Disj:
    def __init__(self, left, right):
        self.left = left
        self.right = right
    def get_print_result(self):
        return "disj (%s, %s)" %(self.left.get_print_result(), self.right.get_print_result())
    def show(self):
        print(self.get_print_result())

class Ea:
    def __init__(self, action, subFormula):
        self.action = action
        self.subFormula = subFormula
    def get_op_name(self):
        return "ea"
    def get_print_result(self):
        return "E<%s> (%s)" %(self.action, self.subFormula.get_print_result())
    def show(self):
        print(self.get_print_result())

class Aa:
    def __init__(self, action, subFormula):
        self.action = action
        self.subFormula = subFormula
    def get_print_result(self):
        return "A<%s> (%s)" %(self.action, self.subFormula.get_print_result())
    def show(self):
        print(self.get_print_result())

class EG:
    def __init__(self, subFormula):
        self.subFormula = subFormula
    def get_op_name(self):
        return "eg"
    def get_print_result(self):
        return "EG (%s)" %(self.subFormula.get_print_result())
    def show(self):
        print(self.get_print_result())

class AF:
    def __init__(self, subFormula):
        self.subFormula = subFormula
    def get_op_name(self):
        return "af"
    def get_print_result(self):
        return "AF (%s)" %(self.subFormula.get_print_result())
    def show(self):
        print(self.get_print_result())

