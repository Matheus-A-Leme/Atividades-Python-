# conceitosbasicos.py

# 1. Comandos Básicos

# 1.1 Variáveis e Tipos de Dados
print("1.1 Variáveis e Tipos de Dados")
nome = "João"  # String
idade = 25  # Inteiro
altura = 1.75  # Float
ativo = True  # Booleano

# Exibir informações formatadas
print(f"Nome: {nome}, Idade: {idade}, Altura: {altura}, Nativo: {ativo}")

# Outro exemplo de concatenação de string
mensagem = "Olá, " + nome + "! Bem-vindo."
print(mensagem)

# Conversão de tipos
idade_str = str(idade)
print("Idade como string:", idade_str)

# 1.2 Estruturas Condicionais
print("\n1.2 Estruturas Condicionais")
numero = 10
if numero > 0:
    print("O número é positivo")
elif numero < 0:
    print("O número é negativo")
else:
    print("O número é zero")

# Verificação de par ou ímpar
if numero % 2 == 0:
    print("O número é par")
else:
    print("O número é ímpar")

# 1.3 Laços de Repetição
print("\n1.3 Laços de Repetição")
# Laço for
for i in range(1, 6):
    print(f"Contagem: {i}")

# Laço while
contador = 5
while contador > 0:
    print(f"Regressiva: {contador}")
    contador -= 1

# Percorrendo listas
frutas = ["maçã", "banana", "uva"]
for fruta in frutas:
    print(f"Fruta: {fruta}")
