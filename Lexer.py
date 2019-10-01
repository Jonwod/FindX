from Equation import Equation
from Expression import *
import Symbols


class Token:
    """ Stores a string value identified as a single token by the lexer"""
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return "<" + self.value + ">"


def lex(string):
    """ Processes input string and returns an ordered list of Tokens (or None if string
    cannot be interpreted as a valid equation)"""

    tokens = []
    current_token = ""

    def add_token(value):
        if len(value) > 0:
            tokens.append(Token(value))

    for c in string:
        if c == ' ':
            add_token(current_token)
            current_token = ""
        elif c in Symbols.special_symbols:
            add_token(current_token)
            add_token(c)
            current_token = ""
        elif c.isalpha() or c.isdigit() or c == '.':
            current_token += c
        else:
            print("Error in lexer: character" + c + " is invalid")

    add_token(current_token)

    return tokens


# ~~~~~~ TESTING ~~~~~~~~

# tokens = lex("31 + 3*x = 4")
#
# token_string = ''
#
# for token in tokens:
#     token_string += str(token)
#
# print(token_string)

# ~~~~~~~~~~~~~~~~~~~~~~~