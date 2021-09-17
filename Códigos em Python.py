------------------------------------------------------------------------------------------------------------------ PYTHON ------------------------------------------------------------------------------------------------------------------

- COMANDO PARA IMPRIMIR NA TELA: print("Ola Mundo!!")
____________________________________________________________________________________________________________________________________________________________________________________

- COMO PUXAR O TIPO DA VARIAVEL: 

	existe = true 
	type(existe)
	print(type(existe))

____________________________________________________________________________________________________________________________________________________________________________________

- LIMPAR TELA: import os 
	       clear = lambda: os.system("cls")
	       clear()

____________________________________________________________________________________________________________________________________________________________________________________

- VARIAVEIS: 

pais = "Italia" 
quantidade = 4

OBS:Não há declaração de variáveis estáticas em Python, como em linguagens como C, Java ou C#. 

Por exemplo:

int idade;

Em Python, a variável só passa a existir quando atribuímos um valor, como no exemplo abaixo:

idade = 12

____________________________________________________________________________________________________________________________________________________________________________________

 
- IMPRIMIR NA TELA UTILIZANDO AS VARIAVEIS: 

pais = "Italia" 
quantidade = 4
print(pais, "ganhou", quantidade,"titulos mundiais") 


____________________________________________________________________________________________________________________________________________________________________________________

- IMPRIMIR NA TELA UTILIZANDO AS VARIAVEIS, O SEP(SEPARADOR) E O END:	
									subst = "Python"
									verbo = "é"
									adjetivo = "fantástico"
									print(subst, verbo, adjetivo, sep="_", end="!\n") 

--------------------------------------------- RESULTADO : --------------------------------------------- 	
									
										Python_é_fantástico!

------------------------------------------------------------------------------------------------------- 	
____________________________________________________________________________________________________________________________________________________________________________________


- SNAKE_CASE: Variáveis em Snake_Case são:


idade_esposa = 20
perfil_vip = 'Flávio Almeida'
recibos_em_atraso = 30

Em outras linguagens também se usa o padrão CamelCase. O mesmo exemplo com CamelCase (que não é o padrão do Python):

idadeEsposa = 20
perfilVip = 'Flávio Almeida'
recibosEmAtraso = 30

____________________________________________________________________________________________________________________________________________________________________________________


- IF E ELSE:  Exemplo de IF e ELSE:

	minha_idade = 26
	idade_namorado = 25
	if(minha_idade == idade_namorado):
    	    print('temos idades iguais')
	else:
    	    print('temos idades diferentes')

OBS: Importante também é sempre usar a indentação correta. Ou seja, depois da linha com o if, devemos usar 4 espaços ou pressionar a tecla tab para começar o novo bloco de código.
____________________________________________________________________________________________________________________________________________________________________________________

- INPUT / ENTRADA DE DADOS DO USUÁRIO:

input("Digite o seu número: ")


____________________________________________________________________________________________________________________________________________________________________________________

-  ATRIBUIR AO INPUT UMA VARIAVEL:

chute = input("Digite o seu número: ")

____________________________________________________________________________________________________________________________________________________________________________________

- CONVERTENDO INPUT QUE É UMA STRING PARA UM INT:

cvt_chute = input("Digite o seu número: ")

print("Você digitou: ", cvt_chute)


------ CONVERSÃO: ------------

chute = int(cvt_chute)

------ CONVERSÃO DIRETA: / + SIMPLES E + RÁPIDA------------

chute = int(input("digite seu numero? "))
____________________________________________________________________________________________________________________________________________________________________________________
 
- ELIF / MISTURA DE ELSE COM IF KK/ PARA USAR O ELSE COM CONDIÇÃO:

usuario = input("Informe o usuário do sistema!")

if(usuario == "Flávio"):
    print("Seja bem-vindo Flávio!")
elif(usuario == "Douglas"):
    print("Seja bem-vindo Douglas!")
elif(usuario == "Nico"):
    print("Seja bem-vindo Nico")
else:
    print("Usuário não identificado!")

____________________________________________________________________________________________________________________________________________________________________________________

- FOR:


for rodada in range(1, total_de_tentativas + 1):

____________________________________________________________________________________________________________________________________________________________________________________

- BOOLEAN:

acertou = (chute == numero_secreto) 
type(acertou)

____________________________________________________________________________________________________________________________________________________________________________________

- FUNÇÃO FORMAT:
 
total_de_tentativas = 3 
rodada = 1
print("Tentativa {} de {} ".format(rodada, total_de_tentativas))
print("Tentativa {1} de {0}".format(1, 3))
print("R$ {}".format(1.59))
print("R$ {:f}".format(1.59))
print("R$ {:.2f}".format(1.5))
print("R$ {:.2f}".format(1234.50))
print("R$ {:7.2f}".format(1234.50))
print("R$ {:7.2f}".format(1.5))
print("R$ {:07d}".format(4))
print("Data {:02d}/{:02d}".format(9, 4))
print("Data {:02d}/{:02d}".format(19, 11))
print("*****************")


- FUNÇÃO F-STRINGS:

nome = 'Matheus'
print(f'Meu nome é {nome}')
print(f'Meu nome é {nome.lower()}')









--------------------------------------------- RESULTADO : --------------------------------------------- 	

					Tentativa 1 de 3
					Tentativa 3 de 1 
					R$ 1.59
					R$ 1.590000
					R$ 1.50
					R$ 1234.50
					R$ 1234.50			
					R$    1.50
					R$ 0000004
					Data 09/04
					Data 19/11
					
					*****************
					
					Meu nome é Matheus
					Meu nome é matheus
					
	
------------------------------------------------------------------------------------------------------- 

____________________________________________________________________________________________________________________________________________________________________________________

- BREAK: 

if(acertou): 
print("Você acertou!")
break


EXP: BREAK É PARA SER UTILIZADO PARA FECHAR UM LAÇO
____________________________________________________________________________________________________________________________________________________________________________________

- CONTINUE: 

if(chute < 1 or  chute > 100):
        print("Você deve digitar um número entre 1 e 100")
        continue

EXP: CONTINUE É USADO PARA QUE O PROGRAMA NÃO PARE E SIM CONTINUAR RODANDO PASSANDO PARA PROXIMA INTERAÇÃO

____________________________________________________________________________________________________________________________________________________________________________________

- TEXTO EXPLICATIVO DO BREAK E CONTINUE:

Para controlar melhor os laços, existem os comandos break e continue, que são utilizados dentro de um laço (for ou while). Ambos fazem parte do controle de fluxo (control flow).

A diferença é que o break, quando for executado, sai do bloco do laço abruptamente, enquanto continue apenas pula para próxima iteração. 

____________________________________________________________________________________________________________________________________________________________________________________

- RANDOM / FUNÇÃO PARA IMPORTAR UM NUMERO ALEATÓRIO

import random

numero_secreto = random.randrange(1, 101)

____________________________________________________________________________________________________________________________________________________________________________________

- ABS / FUNÇÃO PARA DEIXAR O VALOR ABSOLUTO, PARA NÃO DEIXAR OS VALORES NEGATIVO 

abs(-10)
abs(10)
--------------------------------------------- RESULTADO : ---------------------------------------------
						 
						 10		
						 10

------------------------------------------------------------------------------------------------------- 

____________________________________________________________________________________________________________________________________________________________________________________

- IMPORTANDO OUTRO MÓDULO EM PYTHON: 

import forca 
import adivinhacao
import nomeclasse

____________________________________________________________________________________________________________________________________________________________________________________

- CRIANDO FUNÇÃO PARA CHAMAR O OUTRO MÓDULO: 

def jogar():
def nome_função():

____________________________________________________________________________________________________________________________________________________________________________________

- FUNÇÃO COM PARAMETROS:

def soma(a, b):
s = soma(3, 4) 
     return a + b


____________________________________________________________________________________________________________________________________________________________________________________

- CHAMANDO FUNÇÃO:

forca.jogar()
adivinhacao.jogar()
nome_classe.nome_função()




--------------------------------------------- EXEMPLO: ---------------------------------------------

				print("(1) Forca (2) Adivinhação")
				jogo = int(input("Qual jogo? "))
				if (jogo == 1):
    					print("Jogando forca")
    					forca.jogar()
				elif (jogo == 2):
    					print("Jogando adivinhação")
    					adivinhacao.jogar()


------------------------------------------------------------------------------------------------------- 

____________________________________________________________________________________________________________________________________________________________________________________

- COMO SABER SE É O PROGRAMA É O PRINCIPAL OU NÃO... SE ELE ESTA SENDO EXECUTADO DIRETAMENTE OU SÓ SENDO IMPORTADO:

if(__name__ == "__main__"):
    jogar()

if(__name__ == "__main__"):
    nome_função()

____________________________________________________________________________________________________________________________________________________________________________________

 - LISTA EM PYTHON CHAMANDO ALGUMAS FUNÇÕES

// *lista* //: 

 precos = [1525,1120,1464,1200,1330,1356,1312,1531,1232, 1234,1250,1114,1553,1147,1303,1296,1309,1404,1479,1376,1152,1440,1038,1018,1291,1388,1577,1115,1488,1494,1254,1230,1122,1396,1208,1356,1549,1116,1443,1075,1536,1542,1036,1015,1020,1217,1484,1032,1390,1026 ] //


// *retorna o menor número* //: 

print( min(precos))


// *retorna o maior número* //:

print( max(precos))


// *retorna a quantidade de itens da lista* //:

print( len(precos))


// *retorna a quantidade de um determinado elemento em uma lista* //:

print(precos.count(0))

//*retorna o índice da primeira ocorrência de um determinado elemento em uma lista*//

frutas = ['Banana', 'Morango', 'Maçã', 'Uva', 'Maçã', 'Uva']

print(frutas.index('Uva'))

R: O código acima nos retorna 3, pois é o índice da primeira ocorrência do elemento 'Uva' na lista frutas (lembre-se nas listas começamos a contar do índice 0).

____________________________________________________________________________________________________________________________________________________________________________________

-TUPLA EM PYTHON:

Para criar uma tupla, é bem simples. É do mesmo jeito que criamos uma lista, mas ao invés de usar colchetes, usamos parênteses.
Com uma tupla não é possível nem adicionar, nem remover elementos.
O tipo tuple é considerado uma sequência de valores.

// *Tupla* //: 

precos = (1525,1120,1464,1200,1330,1356,1312,1531,1232, 1234,1250,1114,1553,1147,1303,1296,1309,1404,1479,1376,1152,1440,1038,1018,1291,1388,1577,1115,1488,1494,1254,1230,1122)

____________________________________________________________________________________________________________________________________________________________________________________

-LIST COMPREHENSIONS
 
frutas = ["maçã", "banana", "laranja", "melancia"]

lista = []
for fruta in frutas:
    lista.append(fruta.upper())


SOLUÇÃO MAIS SIMPLES:

frutas = ["maçã", "banana", "laranja", "melancia"]

lista = [fruta.upper() for fruta in frutas]
____________________________________________________________________________________________________________________________________________________________________________________

-OPEN / WRITE / CLOSE:

arquivo = open("palavras.txt", "w") #abrir um arquivo
W = É para escrever no arquivo, se já existir esse arquivo vai apagar oq tiver no arquivo.
A =  É para adicionar novos elementos no arquivo 
R =  É para leitura do arquivo

>>> arquivo.write("banana") #ESCREVENDO NO ARQUIVO
6
>>> arquivo.write("melancia") #ESCREVENDO NO ARQUIVO
8

>>> arquivo.close() #FECHANDO ARQUIVO

arquivo.write("morango\n") #ESCREVENDO E COLOCANDO QUEBRA DE LINHA


-FUNÇÃO WITH OPEN PARA O PYTHON FECHAR SOZINHO O ARQUIVO CASO HOUVER ERROS:

with open("palavras.txt") as arquivo:
    for linha in arquivo:
        print(linha)

____________________________________________________________________________________________________________________________________________________________________________________

1 - De início devemos abrir o arquivo, e como já sabemos é uma boa prática fechá-lo ao final:

    arquivo = open("palavras.txt", "r")

    arquivo.close()

2 - Depois temos que criar uma lista e percorrer o arquivo. Cada linha do arquivo deve ser guardada nessa lista:


    arquivo = open("palavras.txt", "r")
    palavras = []

    for linha in arquivo:
        palavras.append(linha)

    arquivo.close()

3 - Precisamos remover o \n ao final da linha, fazendo um strip nela:


    arquivo = open("palavras.txt", "r")
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()

4 - Agora que já temos todas as palavras na lista devemos acessá-las aleatoriamente. Para isso, vamos importar a biblioteca random?

import random

5 - Com a biblioteca já disponível temos que acessar uma das palavras incluídas na nossa lista. Para isso será necessário gerar um número com a posição aleatória. O número gerado deveria ser apenas de índices válidos na lista: 0 até o tamanho da lista:

    numero = random.randrange(0, len(palavras))

6 - Com o número gerado basta agora pegarmos a palavra secreta correspondente a essa posição:

    numero = random.randrange(0, len(palavras))

    palavra_secreta = palavras[numero].upper()


____________________________________________________________________________________________________________________________________________________________________________________
 
-FUNÇÕES EM PYTHON INICIALIZANDO E CHAMANDO

# declara a função:

def imprime_mensagem():
    print("Olá")

# chama a função: 

imprime_mensagem()
____________________________________________________________________________________________________________________________________________________________________________________

- EXPLICAÇÃO DO PQ UTILIZAR FUNÇÕES EM PYTHON

Sabemos que quebrar uma grande função complexa em pequenas funções é uma boa prática por causa de diversos fatores, mas podemos citar como os principais deles:

1 Dar manutenção ao código fica muito mais fácil, visto que agora podemos examinar vários pequenos blocos, que são muito mais fáceis de compreender do que um grande bloco de código.

2 Ao quebrar uma grande função, também estamos deixando ela com menos responsabilidades,com a meta de atingir o ideal de que cada função tenha apenas uma única responsabilidade.

3 O código também fica muito mais fácil de testar, pois se temos diversas funções pequenas,conseguimos testar uma a uma em busca de erros no código.

4 E por último, a legibilidade do código aumenta muito, pois dando nomes semânticos a cada uma das funções menores, conseguimos deixar bem claro o que aquela parte do código deve fazer e facilita o entendimento do todo como um geral.