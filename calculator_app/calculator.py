from calculator.simple import SimpleCalculator

class Calculator:
    ''' This is class for doing mathematical operations'''

    def add(a, b):
        """
        Additon operation

        Keyword arguments:
                a -- the first operand
                b -- the second operand

        Returns:
                a+b
        """
        return float(a) + float(b)

    def evaluate(a):
        """
        Additon operation

        Keyword arguments:
                a -- the first operand
                b -- the second operand

        Returns:
                a+b
        """
        c = SimpleCalculator()
        c.run(a)
        print(c.log)
        return c.lcd
