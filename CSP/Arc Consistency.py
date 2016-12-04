def gac(variables, constraints):
    """Implementation of the generalized arc consistency algorithm by Poole/Mackworth."""
    TDA = []
    for v in variables:
        for c in constraints:
            if c.is_variable_in_scope(v):
                arc = (v, c)
                TDA.append(arc)

    while TDA:
        arc = TDA.pop()
        variable = arc[0]
        constraint = arc[1]
        ndx = constraint.get_consistent_domain(variable)

        if ndx != variable.get_domain():
            other_constraints = [c for c in constraints if c.is_variable_in_scope(variable) and c != constraint]
            for c in other_constraints:
                if (c.get_other_variable(variable), c) not in TDA:
                    TDA.append((c.get_other_variable(variable), c))
            variable.set_domain(ndx)

    for i in variables:
        print(i.get_domain())

    return variables


def setup_variables():
    """
    Creates Variables with their domains.
    :return: list of variables
    """
    variables = []
    domain = {'add', 'ado', 'age', 'ago', 'aid', 'ail', 'aim', 'air', 'and', 'any', 'ape', 'apt', 'arc', 'are', 'ark',
              'arm', 'art', 'ash', 'ask', 'auk', 'awe', 'awl', 'aye', 'bad', 'bag', 'ban', 'bat', 'bee', 'boa', 'ear',
              'eel', 'eft', 'far', 'fat', 'fit', 'lee', 'oaf', 'rat', 'tar', 'tie'}

    for i in range(6):
        n = Variable(domain)
        variables.append(n)

    return variables


def setup_constraints(vars):
    """
    Instantiates the constraints
    :param vars: The variables to create the constraints for
    :return: list of constraints
    """
    cons = []
    for i in range(3):
        n = Constraint([vars[i], vars[-1]], 0, i)
        cons.append(n)
        n = Constraint([vars[i], vars[-2]], 1, i)
        cons.append(n)
        n = Constraint([vars[i], vars[-3]], 2, i)
        cons.append(n)

    return cons


class Variable:
    """
    A Variable for a CSP holding its domain.
    """
    def __init__(self, domain):
        self.domain = set(domain)

    def get_domain(self):
        return set(self.domain)

    def set_domain(self, new_domain):
        self.domain = new_domain


class Constraint:
    """
    Constraint for CSPs
    """
    def __init__(self, variables, positionOne, positionTwo):
        """

        :param variables: The two variables in the scope of this constraint
        :param positionOne: The position of the character of the A-type Variable which has to be compared
        :param positionTwo: The position of the character of the D-type Variable which has to be compared
        """
        self.scope = variables
        self.positions = [positionOne, positionTwo]  # e.g. 1, 0 for Variables A1 and D2

    def get_consistent_domain(self, current):
        """

        :param current: Get the set of values for which there is a value in the domain of the other variable
        in this constraints' scope such that this constraint is satisfied
        :return: set of values consistent with this constraint
        """
        ndx = set()
        other = self.get_other_variable(current)
        current_pos = self.positions[self.scope.index(current)]  # Position of the relevant character for the variable given by client
        other_pos = self.positions[self.scope.index(other)]  # Position of the relevant character of the other variable
        for word in current.get_domain():
            for item in other.get_domain():
                if word[current_pos] == item[other_pos] and word != item:  # Compare the relevant characters
                    ndx.add(word)
                    break

        return ndx

    def get_other_variable(self, var):
        """
        Get the other variable in the scope of this constraint.
        :param var: Variable
        :return: Variable
        """
        for i in self.scope:
            if var != i: return i

    def get_first_variable(self):
        return self.scope[0]

    def get_second_variable(self):
        return self.scope[1]

    def is_variable_in_scope(self, var):
        return var in self.scope

    def get_scope(self):
        return self.scope

if __name__ == '__main__':
    vs = setup_variables()
    cs = setup_constraints(vs)
    gac(vs, cs)

