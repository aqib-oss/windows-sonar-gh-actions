from sonaronwindows.calculator import Calculator


def test_sum():
    # Arrange
    calculator: Calculator = Calculator()

    # Act
    result: int = calculator.sum(4, 3)

    # Assert
    assert result == 7
