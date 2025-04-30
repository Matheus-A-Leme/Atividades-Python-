# conceitosavancados.py

# 3. Comandos Avançados

# 3.1 Programação Orientada a Objetos
print("3.1 Programação Orientada a Objetos")

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def apresentar(self):
        return f"Meu nome é {self.nome} e tenho {self.idade} anos."

pessoa1 = Pessoa("Carlos", 30)
print(pessoa1.apresentar())

# Criando outra classe
class Carro:
    def __init__(self, modelo, ano):
        self.modelo = modelo
        self.ano = ano

    def detalhes(self):
        return f"Modelo: {self.modelo}, Ano: {self.ano}"

meu_carro = Carro("Fusca", 1975)
print(meu_carro.detalhes())

# 3.2 Trabalhando com APIs
print("\n3.2 Trabalhando com APIs")

import requests

resposta = requests.get("https://api.github.com")
print("Resposta da API do GitHub:", resposta.json())

# Pegando dados de uma API pública
dados = requests.get("https://jsonplaceholder.typicode.com/todos/1").json()
print("Dados da API pública:", dados)

# Verificando status de resposta
if resposta.status_code == 200:
    print("Requisição bem-sucedida!")
else:
    print("Erro ao acessar a API.")
