"""
Test suite for the Calculator class.
"""

import pytest
from calculator.calculator import Calculator, InvalidInputException

@pytest.fixture
def calc():
    """Fixture to create a Calculator instance."""
    return Calculator()


class TestAddition:
    """Tests for the add method."""

    def test_add_positive_numbers(self, calc):
        """Test adding two positive numbers."""
        # Arrange
        a = 5
        b = 3
        expected = 8

        # Act
        result = calc.add(a, b)

        # Assert
        assert result == expected

    def test_add_negative_numbers(self, calc):
        """Test adding two negative numbers."""
        # Arrange
        a = -5
        b = -3
        expected = -8

        # Act
        result = calc.add(a, b)

        # Assert
        assert result == expected

    def test_add_positive_and_negative(self, calc):
        """Test adding positive and negative numbers."""
        # Arrange
        a = 5
        b = -3
        expected = 2

        # Act
        result = calc.add(a, b)

        # Assert
        assert result == expected

    def test_add_negative_and_positive(self, calc):
        """Test adding negative and positive numbers."""
        # Arrange
        a = -5
        b = 3
        expected = -2

        # Act
        result = calc.add(a, b)

        # Assert
        assert result == expected

    def test_add_positive_with_zero(self, calc):
        """Test adding positive number with zero."""
        # Arrange
        a = 5
        b = 0
        expected = 5

        # Act
        result = calc.add(a, b)

        # Assert
        assert result == expected

    def test_add_zero_with_positive(self, calc):
        """Test adding zero with positive number."""
        # Arrange
        a = 0
        b = 5
        expected = 5

        # Act
        result = calc.add(a, b)

        # Assert
        assert result == expected

    def test_add_floats(self, calc):
        """Test adding floating point numbers."""
        # Arrange
        a = 2.5
        b = 3.7
        expected = 6.2

        # Act
        result = calc.add(a, b)

        # Assert
        assert result == pytest.approx(expected)


class TestSubtraction:
    """Tests for the subtract method."""

    def test_subtract_positive_numbers(self, calc):
        """Test subtracting positive numbers."""
        
        # Arrange
        a = 5
        b = 3
        expected = 2
        
        # Act
        result = calc.subtract(a, b)
        
        # Assert
        assert result == expected


class TestMultiplication:
    """Tests for the multiply method."""

    def test_multiply_positive_numbers(self, calc):
        """Test multiplying positive numbers."""
        # Arrange
        a = 5
        b = 3
        expected = 15
        
        # Act
        result = calc.multiply(a, b)
        
        # Assert
        assert result == expected


class TestDivision:
    """Tests for the divide method."""

    def test_divide_positive_numbers(self, calc):
        """Test dividing positive numbers."""
        # Arrange
        a = 10
        b = 2
        expected = 5
        
        # Act
        result = calc.divide(a, b)
        
        # Assert
        assert result == expected

    def test_divide_by_zero(self, calc):
        """ Test dviding by zero"""
        # Arrange
        a = 67
        b = 0

        # Act and Assert
        with pytest.raises(ValueError):
            calc.divide(a,b)


class TestInvalidInput:
    """Tests for invalid input handling."""
    
    def test_add_too_large_value(self, calc):
        """Test adding a value that exceeds the maximum limit."""
        # Arrange
        a = 1000000
        b = 1000000
        
        # Act & Assert
        with pytest.raises(InvalidInputException):
            calc.add(a, b)
            
    def test_add_too_small_value(self, calc):
        """Test adding a value that is below the minimum limit."""
        # Arrange
        a = -1000000
        b = -1000000
        
        # Act & Assert
        with pytest.raises(InvalidInputException):
            calc.add(a, b)

    def test_add_invalid_input(self, calc):
        """Test adding invalid input."""
        # Arrange
        a = "5"
        b = 3
        
        # Act & Assert
        with pytest.raises(InvalidInputException):
            calc.add(a, b)
