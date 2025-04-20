# FizzBuzz Kata - Desenvolvimento Guiado por Testes (TDD)

Este repositório contém a implementação do clássico problema FizzBuzz utilizando a metodologia TDD (Test-Driven Development) com Python e pytest.

## Sobre o Problema

O FizzBuzz é um problema clássico de programação com os seguintes requisitos:

- Imprimir números de 1 a 100, um por linha
- Para múltiplos de 3, imprimir "Fizz" em vez do número
- Para múltiplos de 5, imprimir "Buzz" em vez do número
- Para múltiplos de ambos 3 e 5, imprimir "FizzBuzz" em vez do número

## Como Executar

### Pré-requisitos
- Python 3.x
- pytest (`pip install pytest`)

### Executando os Testes
```bash
pytest test_fizzbuzz.py -v
```

### Executando o Programa
```bash
python fizzbuzz.py
```

## Processo de Desenvolvimento TDD

O código foi desenvolvido seguindo o ciclo TDD: Red (teste falha) → Green (teste passa) → Refactor (refatoração).

### Ciclo 1: Retornar "1" para o número 1

#### Red: Primeiro teste - falha
```python
def test_returns_1_for_1():
    # Este teste vai falhar porque a função fizzbuzz ainda não existe
    assert fizzbuzz(1) == "1"
```
Executando `pytest test_fizzbuzz.py -v` → **FALHA** (função não definida)

#### Green: Implementação mínima para passar
```python
def fizzbuzz(number):
    return "1"
```
Executando `pytest test_fizzbuzz.py -v` → **PASSA**

### Ciclo 2: Retornar "2" para o número 2

#### Red: Segundo teste - falha
```python
def test_returns_2_for_2():
    assert fizzbuzz(2) == "2"
```
Executando `pytest test_fizzbuzz.py -v` → **FALHA** (nossa função sempre retorna "1")

#### Green: Modificação para passar
```python
def fizzbuzz(number):
    return str(number)
```
Executando `pytest test_fizzbuzz.py -v` → **PASSA**

### Ciclo 3: Retornar "Fizz" para múltiplos de 3

#### Red: Terceiro teste - falha
```python
def test_returns_fizz_for_3():
    assert fizzbuzz(3) == "Fizz"
```
Executando `pytest test_fizzbuzz.py -v` → **FALHA** (retorna "3" em vez de "Fizz")

#### Green: Implementação da regra para múltiplos de 3
```python
def fizzbuzz(number):
    if number % 3 == 0:
        return "Fizz"
    return str(number)
```
Executando `pytest test_fizzbuzz.py -v` → **PASSA**

### Ciclo 4: Retornar "Buzz" para múltiplos de 5

#### Red: Quarto teste - falha
```python
def test_returns_buzz_for_5():
    assert fizzbuzz(5) == "Buzz"
```
Executando `pytest test_fizzbuzz.py -v` → **FALHA** (retorna "5" em vez de "Buzz")

#### Green: Implementação da regra para múltiplos de 5
```python
def fizzbuzz(number):
    if number % 3 == 0:
        return "Fizz"
    if number % 5 == 0:
        return "Buzz"
    return str(number)
```
Executando `pytest test_fizzbuzz.py -v` → **PASSA**

### Ciclo 5: Retornar "FizzBuzz" para múltiplos de 3 e 5

#### Red: Quinto teste - falha
```python
def test_returns_fizzbuzz_for_15():
    assert fizzbuzz(15) == "FizzBuzz"
```
Executando `pytest test_fizzbuzz.py -v` → **FALHA** (retorna "Fizz" em vez de "FizzBuzz")

#### Green: Implementação da regra para múltiplos de 3 e 5
```python
def fizzbuzz(number):
    if number % 3 == 0 and number % 5 == 0:
        return "FizzBuzz"
    if number % 3 == 0:
        return "Fizz"
    if number % 5 == 0:
        return "Buzz"
    return str(number)
```
Executando `pytest test_fizzbuzz.py -v` → **PASSA**

### Refactor: Melhorando o código e adicionando mais testes

#### Testes adicionais
```python
def test_returns_fizz_for_multiples_of_3():
    assert fizzbuzz(3) == "Fizz"
    assert fizzbuzz(6) == "Fizz"
    assert fizzbuzz(9) == "Fizz"

def test_returns_buzz_for_multiples_of_5():
    assert fizzbuzz(5) == "Buzz"
    assert fizzbuzz(10) == "Buzz"
    assert fizzbuzz(20) == "Buzz"

def test_returns_fizzbuzz_for_multiples_of_3_and_5():
    assert fizzbuzz(15) == "FizzBuzz"
    assert fizzbuzz(30) == "FizzBuzz"
    assert fizzbuzz(45) == "FizzBuzz"
```

#### Versão final refatorada
```python
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
```

#### Função principal para rodar o programa
```python
def print_fizzbuzz():
    """Imprime FizzBuzz para números de 1 a 100"""
    for i in range(1, 101):
        print(fizzbuzz(i))

if __name__ == "__main__":
    print_fizzbuzz()
```

## Por que TDD?

O Desenvolvimento Guiado por Testes oferece vários benefícios:

1. **Melhor Design**: Escrever testes antes do código nos leva a pensar mais sobre a interface e funcionalidade do código.
2. **Melhor Cobertura de Testes**: Garantimos que cada parte da funcionalidade seja testada.
3. **Refatoração Segura**: Podemos melhorar o código sem medo de quebrar a funcionalidade.
4. **Documentação Viva**: Os testes servem como documentação ativa de como o código deve funcionar.
5. **Desenvolvimento Incremental**: O problema é dividido em partes pequenas e gerenciáveis.

## Estrutura do Projeto

```
.
├── README.md
├── fizzbuzz.py     # Implementação final
└── test_fizzbuzz.py  # Testes unitários
```

## Licença

Este projeto está licenciado sob a licença MIT - veja o arquivo LICENSE para detalhes.
