from Expression import *

print("Hello, this is FindX")


def lex(string):
    pass


while True:
    option = input("Enter an equation, in terms of X, or type 'quit' to quit")
    if option == "quit":
        break
    else:
        lex(option)