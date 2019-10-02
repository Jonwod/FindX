
class Expression:
    def debug_string(self):
        return str(self)   


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

    @property
    def symbol(self):
        """ Make sure to override """
        return '?'

    def debug_string(self):
        return '<' + self.op1.debug_string() + ' ' + self.symbol + ' ' + self.op2.debug_string() +'>'

    def __str__(self):
        return str(self.op1) +' ' + self.symbol + ' ' + str(self.op2)


class Power(BinaryOperation):
    @property
    def symbol(self):
        return '^'


class Multiplication(BinaryOperation):
    @property
    def symbol(self):
        return '*'


class Division(BinaryOperation):
    @property
    def symbol(self):
        return '/'


class Addition(BinaryOperation):
    @property
    def symbol(self):
        return '+'


class Subtraction(BinaryOperation):
    @property
    def symbol(self):
        return '-'


class BracketExpression(Expression):
    def __init__(self, contained_expression):
        self.contained_expression = contained_expression

    def __str__(self):
        return "(" + str(self.contained_expression) + ")"

    def debug_string(self):
        return "(" + self.contained_expression.debug_string() + ")"


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