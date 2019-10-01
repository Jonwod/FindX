import Symbols

# A list of lists of equal priority symbols, ordered from high to low priority
order_of_operations = [[Symbols.open_bracket, Symbols.close_bracket],
                       [Symbols.power],
                       [Symbols.multiply, Symbols.divide],
                       [Symbols.plus, Symbols.minus]
                       ]
