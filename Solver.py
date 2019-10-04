import copy
import Equation

def solve(equation, variable_name):
    """ Finds the value of the variable with name variable_name in the input
    equation, if it can be solved """

    eq = copy.deepcopy(equation)

    