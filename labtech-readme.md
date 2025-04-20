# 🧪 Treinamento LabTech - Desafios TDD com Python

<div align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/TDD-007ACC?style=for-the-badge&logo=testing-library&logoColor=white" alt="TDD">
  <img src="https://img.shields.io/badge/pytest-0A9EDC?style=for-the-badge&logo=pytest&logoColor=white" alt="pytest">
  <br>
  <img src="https://img.shields.io/github/stars/danilosilva/treinamento-labtech?style=social" alt="Stars">
  <img src="https://img.shields.io/github/forks/danilosilva/treinamento-labtech?style=social" alt="Forks">
  <img src="https://img.shields.io/github/issues/danilosilva/treinamento-labtech?style=social" alt="Issues">
</div>

<p align="center">
  <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="Python Logo" width="120" height="120">
</p>

## 📋 Sobre o Projeto

Este repositório contém uma série de **Desafios de Programação** baseados na metodologia **TDD (Test-Driven Development)** desenvolvidos como parte do projeto acadêmico do curso de Tecnologia da Informação da **Universidade do Distrito Federal (UDF)**.

Ao longo do primeiro semestre de 2025, serão disponibilizados **6 desafios** que abordam diferentes conceitos e técnicas de programação, todos implementados com a linguagem Python e testados com o framework pytest.

## 🔄 Ciclo TDD

<p align="center">
  <img src="https://upload.wikimedia.org/wikipedia/commons/0/0b/TDD_Global_Lifecycle.png" alt="Ciclo TDD" width="500">
</p>

O desenvolvimento orientado a testes (TDD) segue um ciclo de três fases:

1. **🔴 RED**: Escreva um teste que falha para a funcionalidade que você deseja implementar
2. **🟢 GREEN**: Escreva o código mínimo necessário para fazer o teste passar
3. **🔄 REFACTOR**: Melhore o código mantendo os testes funcionando

## 🛠️ Configuração do Ambiente

### Requisitos

- Python 3.8 ou superior
- pip (gerenciador de pacotes do Python)

### Instalação do pytest

```bash
# Criar um ambiente virtual (recomendado)
python -m venv venv

# Ativar o ambiente virtual
# No Windows:
venv\Scripts\activate
# No Linux/MacOS:
source venv/bin/activate

# Instalar o pytest
pip install pytest

# Verificar a instalação
pytest --version
```

### Como Executar os Testes

```bash
# Executar todos os testes
pytest

# Executar testes de um desafio específico
pytest desafio1/test_desafio1.py

# Executar com visualização detalhada
pytest -v

# Executar com cobertura de código
pip install pytest-cov
pytest --cov=.
```

## 📚 Desafios

Serão disponibilizados 6 desafios ao longo do primeiro semestre de 2025:

## 💡 Como Utilizar os Desafios

Cada desafio segue a metodologia TDD e contém:

1. Um arquivo README com instruções detalhadas
2. Arquivos de teste que definem os requisitos do problema

Para cada desafio, recomendamos seguir estas etapas:

1. Leia o README do desafio para entender os requisitos
2. Execute os testes para ver que eles falham (RED)
3. Implemente a solução mais simples para fazer os testes passarem (GREEN)
4. Refatore seu código mantendo os testes passando (REFACTOR)

## 👨‍💻 Exemplos Práticos

### Exemplo de um ciclo TDD: FizzBuzz

#### 🔴 RED - Escrevendo um teste que falha:

```python
# test_fizzbuzz.py
def test_fizzbuzz_returns_1_for_1():
    assert fizzbuzz(1) == "1"
```

Executando: `pytest test_fizzbuzz.py -v`
Resultado: FALHA (função não existe)

#### 🟢 GREEN - Implementação mínima:

```python
# fizzbuzz.py
def fizzbuzz(num):
    return "1"
```

Executando: `pytest test_fizzbuzz.py -v`
Resultado: PASSA

#### 🔄 REFACTOR - Melhorando o código:

```python
# fizzbuzz.py
def fizzbuzz(num):
    return str(num)
```

Executando: `pytest test_fizzbuzz.py -v`
Resultado: PASSA

## 👤 Desenvolvedor

**Danilo Teodoro dos Santos Silva**
- Aluno da Universidade do Distrito Federal (UDF)
- Treinamento do Projeto LabTech

## 📄 Licença

Este projeto está licenciado sob a [Licença MIT](LICENSE) - veja o arquivo LICENSE para detalhes.

## 🤝 Contribuições

Contribuições são bem-vindas! Se você deseja adicionar novos desafios relacionados ao TDD ou melhorar os existentes:

1. Faça um Fork do repositório
2. Crie uma Branch para sua feature (`git checkout -b feature/NovoDesafio`)
3. Faça commit das suas mudanças (`git commit -m 'Adiciona novo desafio'`)
4. Push para a Branch (`git push origin feature/NovoDesafio`)
5. Abra um Pull Request

---

<div align="center">
  <p>
    <b>🚀 Desenvolvido com paixão pela programação e ensino de qualidade 🚀</b>
  </p>
  <p>
    <i>Universidade do Distrito Federal - UDF, 2025</i>
  </p>
</div>
