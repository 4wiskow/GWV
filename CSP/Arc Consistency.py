def gac(variables, dom, constraints):
    TDA = []
    for c in constraints:
        arc = (c.get_first_variable(), c)
        TDA.append(arc)
        arc = (c.get_second_variable(), c)
        TDA.append(arc)

    while TDA:
        arc = TDA.pop()
        variable = arc[0]
        constraint = arc[1]
        ndx = constraint.get_consistent_domain(variable)

        if ndx != variable.get_domain():
            other_constraints = [c for c in constraints if c.is_variable_in_scope(variable) and c != constraint]
            for c in other_constraints:
                TDA.append((c.get_other_variable(variable), c))
            variable.set_domain(ndx)
        print(variable.get_domain())

    for i in variables:
        print(i.get_domain())


def setup_variables():
    variables = []
    domain = ['add', 'ado', 'age', 'ago', 'aid', 'ail', 'aim', 'air', 'and', 'any', 'ape', 'apt', 'arc', 'are', 'ark', 'arm', 'art', 'ash', 'ask', 'auk', 'awe', 'awl', 'aye', 'bad', 'bag', 'ban', 'bat', 'bee', 'boa', 'ear', 'eel', 'eft', 'far', 'fat', 'fit', 'lee', 'oaf', 'rat', 'tar', 'tie']

    for i in range(6):
        n = Variable(list(domain))
        variables.append(n)

    return variables

def dom(element):
    return element.get_domain()


def setup_constraints(variables):
    constraints = []
    for i in range(3):
        n = Constraint([variables[i], variables[-1]], 0, i)
        constraints.append(n)
        n = Constraint([variables[i], variables[-2]], 1, i)
        constraints.append(n)
        n = Constraint([variables[i], variables[-3]], 2, i)
        constraints.append(n)

    return constraints


class Variable:
    def __init__(self, domain):
        self.domain = list(domain)

    def get_domain(self):
        return self.domain

    def set_domain(self, new_domain):
        self.domain = new_domain

    def remove_from_domain(self, element):
        self.domain = self.domain.remove(element)


class Constraint:
    def __init__(self, variables, positionOne, positionTwo):
        self.scope = variables
        self.positionOne = positionOne
        self.positionTwo = positionTwo

    def get_consistent_domain(self, variableA):
        ndx = []
        other = self.get_other_variable(variableA)
        for word in variableA.get_domain():
            for item in other.get_domain():
                if word[self.positionOne] == item[self.positionTwo]:
                    ndx.append(word)
                    break


        return ndx

    def get_other_variable(self, varA):
        for i in self.scope:
            if varA != i: return i

    def get_first_variable(self):
        return self.scope[0]

    def get_second_variable(self):
        return self.scope[1]

    def is_variable_in_scope(self, var):
        return var in self.scope

    def get_scope(self):
        return self.scope

if __name__ == '__main__':
    variables = setup_variables()
    constraints = setup_constraints(variables)
    gac(variables, dom, constraints)

