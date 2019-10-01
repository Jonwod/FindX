
class Expression:
    pass


class Constant(Expression):
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return Constant(self.value + other.value)

    def __sub__(self, other):
        return Constant(self.value - other.value)

    def __str__(self):
        return str(self.value)


class Variable(Expression):
    def __init__(self, name):
        self.name = str(name)

    def __str__(self):
        return self.name


class BinaryOperation(Expression):
    def __init__(self, op1, op2):
        self.op1, self.op2 = op1, op2


class Power(BinaryOperation):
    def __str__(self):
        return str(self.op1) + " ^ " + str(self.op2)


class Multiplication(BinaryOperation):
    def __str__(self):
        return str(self.op1) + " * " + str(self.op2)


class Division(BinaryOperation):
    def __str__(self):
        return str(self.op1) + " / " + str(self.op2)


class Addition(BinaryOperation):
    def evaluate(self):
        return self.op1 + self.op2

    def __str__(self):
        return str(self.op1) + " + " + str(self.op2)


class Subtraction(BinaryOperation):
    def __str__(self):
        return str(self.op1) + " - " + str(self.op2)


class BracketExpression(Expression):
    def __init__(self, contained_expression):
        self.contained_expression = contained_expression

    def __str__(self):
        return "(" + str(self.contained_expression) + ")"


# class CompoundExpression(Expression):
#     def __init__(self, operations):
#         self.operations = operations
#
#     def __str__(self):
#         string = ""
#         for op in self.operations:
#             string += str(op)
#         return string


# ~~~~~~ TESTING ~~~~~~~~

# three = Constant(3)
# two = Constant(2)
#
# x = Variable()
#
#
# three_plus_two_plus_x = Plus(Plus(three, two), x)
#
# print(three_plus_two_plus_x)

# ~~~~~~~~~~~~~~~~~~~~~~~~