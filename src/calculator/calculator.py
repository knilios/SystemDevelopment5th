"""
A simple calculator module with basic arithmetic operations.
"""


class InvalidInputException(Exception):
    """Exception raised when input values are outside the valid range."""
    pass


class Calculator:
    """Calculator class providing basic arithmetic operations."""

    @staticmethod
    def validate_input(value):
        """Validate input value.

        Args:
            value: The value to validate

        Raises:
            InvalidInputException: If the value is outside the valid range
        """
        if not isinstance(value, (int, float)):
            raise InvalidInputException(f"Input {value} is not a valid number")
        if not (-1000 <= value <= 1000):
            raise InvalidInputException(f"Input {value} is out of valid range (-1000 to 1000)")

    def add(self, a, b):
        """Add two numbers.

        Args:
            a: First number
            b: Second number

        Returns:
            Sum of a and b

        Raises:
            InvalidInputException: If any input is outside valid range
        """
        self.validate_input(a)
        self.validate_input(b)
        return a + b

    def subtract(self, a, b):
        """Subtract b from a.

        Args:
            a: First number
            b: Second number

        Returns:
            Difference of a and b

        Raises:
            InvalidInputException: If any input is outside valid range
        """
        self.validate_input(a)
        self.validate_input(b)
        return a - b

    def multiply(self, a, b):
        """Multiply two numbers.

        Args:
            a: First number
            b: Second number

        Returns:
            Product of a and b

        Raises:
            InvalidInputException: If any input is outside valid range
        """
        self.validate_input(a)
        self.validate_input(b)
        return a * b

    def divide(self, a, b):
        """Divide a by b.

        Args:
            a: Numerator
            b: Denominator

        Returns:
            Quotient of a and b

        Raises:
            InvalidInputException: If any input is outside valid range
            ValueError: If b is zero
        """
        self.validate_input(a)
        self.validate_input(b)
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b





