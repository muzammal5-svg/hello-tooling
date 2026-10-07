# tests/test_main.py

from src.main import add_numbers

def test_add_numbers_success():
    # Arrange (Data set karna)
    num1 = 5
    num2 = 10
    
    # Act (Function ko call karna)
    result = add_numbers(num1, num2)
    
    # Assert (Check karna ke result theek hai ya nahi)
    assert result == 15

def test_add_numbers_negative():
    # Aik aur test case negative numbers ke liye
    result = add_numbers(-2, -3)
    assert result == -5