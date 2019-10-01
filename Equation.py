from Expression import Expression


class Equation:
    def __init__(self, lhs, rhs):
        self.lhs, self.rhs = lhs, rhs

    def __str__(self):
        return str(self.lhs) + " = " + str(self.rhs)



# ~~~~~~ TESTING ~~~~~~~~
# from Expression import *
#
# three = Constant(3)
# two = Constant(2)
#
# x = Variable('x')
#
#
# three_plus_two_plus_x = Addition(Addition(three, two), x)
#
# equation = Equation(three_plus_two_plus_x, Constant(13))
#
# print(equation)
# ~~~~~~~~~~~~~~~~~~~~~~~~