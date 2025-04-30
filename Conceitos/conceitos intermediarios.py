# conceitosintermediarios.py

# 2. Comandos Intermediários

# 2.1 Funções
print("2.1 Funções")

def saudacao(nome):
    return f"Olá, {nome}!"

print(saudacao("Maria"))

# Função com parâmetro padrão
def apresentar(nome, idade=18):
    return f"Meu nome é {nome} e tenho {idade} anos."

print(apresentar("Carlos"))

# Função que retorna a soma de dois números
def soma(a, b):
    return a + b

print(soma(5, 7))

# 2.2 Manipulação de Arquivos
print("\n2.2 Manipulação de Arquivos")

# Escrevendo em um arquivo
with open("arquivo.txt", "w") as arquivo:
    arquivo.write("Este é um exemplo de escrita em arquivo.\n")
print("Escrevendo no arquivo 'arquivo.txt'...")

# Lendo um arquivo
with open("arquivo.txt", "r") as arquivo:
    conteudo = arquivo.read()
    print("Conteúdo do arquivo:", conteudo)

# Adicionando conteúdo ao arquivo
with open("arquivo.txt", "a") as arquivo:
    arquivo.write("Linha adicional\n")
print("Adicionando uma linha ao arquivo.")

# 2.3 Tratamento de Exceções
print("\n2.3 Tratamento de Exceções")

try:
    resultado = 10 / 0
except ZeroDivisionError:
    print("Erro: Divisão por zero não é permitida.")

try:
    lista = [1, 2, 3]
    print(lista[5])
except IndexError:
    print("Erro: Índice fora do intervalo.")

try:
    numero = int("abc")
except ValueError:
    print("Erro: Conversão inválida de string para inteiro.")
