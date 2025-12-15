class Calculator:
    """ A simple calculator class. """

    def check_input(self, x):
        """ Check if the input is an integer.

        Parameters:
        x: The input value to be checked.

        Raises:
        TypeError: If x is not an integer.
        """
        if not isinstance(x, int):
            raise TypeError("Parameter 'x' must be an integer.")

    
    def add(self, x, y):
        """ Adds two numbers together.

        Parameters:
        x (int): The first number.
        y (int): The second number.

        Returns:
        int: The sum of x and y.

        Raises:
        TypeError: If either x or y is not an integer.
        """
        self.check_input(x)
        self.check_input(y)

        return x + y