def test_retunrs_1_for_1():
    assert fizzbuzz(1) == "1"

def fizzbuzz(number):
    return "1"

def test_returns_2_for_2():
    assert fizzbuzz(2) == "2"

def fizzbuzz(number):
    return str(number)

def test_returns_3_for_3():
    assert fizzbuzz(3) == "Fizz"
    
def fizzbuzz(number):
    if number % 3 == 0:
        return "Fizz"
    return str(number)

def test_returns_buzz_for_5():
    assert fizzbuzz(5) == "Buzz"
    
def fizzbuzz(number):
    if number % 3 == 0:
        return "Fizz"
    if number % 5 == 0:
        return "Buzz"
    return str(number)

def fizzbuzz (number):
    if number % 3 == 0 and number % 5 == 0:
        return "FizzBuzz"
    if number % 3 == 0:
        return "Fizz"
    if number % 5 == 0:
        return "Buzz"
    return str(number)

def test_returns_fizz_for_multiple_of_3():
    assert fizzbuzz(3) == "Fizz"
    assert fizzbuzz(6) == "Fizz"
    assert fizzbuzz(9) == "Fizz"

def test_returns_buzz_for_multiple_of_5():
    assert fizzbuzz(5) == "Buzz"
    assert fizzbuzz(10) == "Buzz"
    assert fizzbuzz(20) == "Buzz"

def test_returns_fizzbuzz_for_multiple_of_3_and_5():
    assert fizzbuzz(15) == "FizzBuzz"
    assert fizzbuzz(30) == "FizzBuzz"
    assert fizzbuzz(45) == "FizzBuzz"

def fizzbuzz(number):
    """
    Retorna:
    - 'FizzBuzz' para múltiplos de 3 e 5
    - 'Fizz' para múltiplos de 3
    - 'Buzz' para múltiplos de 5
    - O próprio número como string nos outros casos
    """
    result = ""
    if number % 3 == 0:
        result += "Fizz"
    if number % 5 == 0:
        result += "Buzz"
    
    return result if result else str(number)

# Função para imprimir FizzBuzz de 1 a 100
def print_fizzbuzz():
    """Imprime FizzBuzz para números de 1 a 100"""
    for i in range(1, 101):
        print(fizzbuzz(i))

if __name__ == "__main__":
    print_fizzbuzz()
