from Lexer import lex
from Expression import *
from Equation import Equation
import Symbols


def split_equation(tokens):
    """ Returns a tuple consisting of a list of tokens for the
    left and right hand sides of the input equation, respectively."""
    lhs = []
    rhs = []
    found_equals = False
    for token in tokens:
        if token.value == '=':
            found_equals = True
        else:
            (rhs if found_equals else lhs).append(token)

    if not found_equals:
        print("Error in split_equation: Equals token not found!")

    return lhs, rhs


def parse_expression(tokens):
    """ Parses a string of tokens into an expression """
    # The plan:
    # Cycle through operations in order of priority and from each identified operation,
    # parse the expression on each side (recursively)


def parse_equation(string):

    """ Parses a string into an Expression"""
    tokens = lex(string)
    lhs, rhs = split_equation(tokens)
    lhs = parse_expression(lhs)
    rhs = parse_expression(rhs)

    return Equation(lhs, rhs)




# ~~~~~~ TESTING ~~~~~~~~

string = "31 + 3*x = 4"

equation = parse_equation(string)

print(equation)

# ~~~~~~~~~~~~~~~~~~~~~~~