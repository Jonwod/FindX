from Lexer import lex
from Expression import *
from Equation import Equation
import Symbols
from OrderOfOperations import order_of_operations


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


def make_operation(s):
    """ Makes and returns a  BinaryOperation expression of appropriate type for the input string symbol
    Will have operands of None"""
    if s == Symbols.power:
        return Power(None, None)
    elif s == Symbols.multiply:
        return Multiplication(None, None)
    elif s == Symbols.divide:
        return Division(None, None)
    elif s == Symbols.plus:
        return Addition(None, None)
    elif s == Symbols.minus:
        return Subtraction(None, None)
    else:
        print("Error in make_operation: Symbol" + s + " not accounted for.")


def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False


def parse_expression(tokens):
    """ Parses a string of tokens into an expression """
    # The plan:
    # Cycle through operations in reverse order of priority and from each identified operation,
    for n_priority_symbols in reversed(order_of_operations):
        for i in range(0, len(tokens)):
            if tokens[i].value in n_priority_symbols:
                if tokens[i].value in Symbols.operators:
                    operation = make_operation(tokens[i].value)
                    if i > 0 and len(tokens) > (i + 1):
                        operation.op1 = parse_expression(tokens[:i])
                        operation.op2 = parse_expression(tokens[i + 1:])
                        return operation
                    else:
                        print("Syntax error in parse_expression: operator " + tokens[i].value + " does not have an "
                              "expression on each side")
                elif tokens[i].value == Symbols.open_bracket:
                    # TODO: Parse brackets
                    pass
                elif tokens[i].value == Symbols.close_bracket:
                    # TODO: Parse brackets
                    pass

    # If got to here then no tokens in tokens are operators.
    # tokens should therefore have length of 1, as you can't have adjacent constants/variables
    if len(tokens) == 1:
        if is_number(tokens[0].value):
            return Constant(float(tokens[0].value))
        else:
            return Variable(tokens[0].value)
    else:
        print("Error in parse_expression: " + str(len(tokens)) + " tokens with no operators")


def parse_equation(string):
    """ Parses a string into an Expression"""
    tokens = lex(string)
    lhs, rhs = split_equation(tokens)
    lhs = parse_expression(lhs)
    rhs = parse_expression(rhs)

    return Equation(lhs, rhs)


# ~~~~~~ TESTING ~~~~~~~~

string = "31 + 3 * x = 4 / x + 1"

equation = parse_equation(string)

print(equation)

# ~~~~~~~~~~~~~~~~~~~~~~~
