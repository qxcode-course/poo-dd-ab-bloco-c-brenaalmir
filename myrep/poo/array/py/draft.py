import random

class Foo:
    def __init__(self, x: int):
        self.x = x

    def __str__(self):
        return f'Foo({self.x})'

lista_vazia: list[int] = []
lista_preenchida: list[int] = [1, 2, 3, 4, 5]
lista_preencida_objetos: list[Foo] = [Foo(1), Foo(2), Foo(3), Foo(4), Foo(5)]


#- Obter o tamanho do array

tamanho_int = len(lista_preenchida)
tamanho_obj  = len(lista_preencida_objetos)

#- Adicionar e remover elementos ao final

lista_preenchida.append(6)
final = lista_preenchida.pop()

#- Adicionar e remover elementos no início

lista_preenchida.insert(0, 99)
inicio = lista_preenchida.pop(0)

#- Adicionar e remover elementos em uma posição específica

lista_preenchida.insert(2, 123)
removido = lista_preenchida.pop(2)

#- Fazer impressão formatada utilizando o método join

lista: list[str] = []
for i in lista_preenchida:
    lista.append(str(i))
texto = ",".join(lista)

#- Criar um array com elementos em sequência de zero a n

n = 10
sequencia: list[int] = []
for i in range(n+1):
    sequencia.append(i)

#- Criar um array com valores aleatórios

aleatorio: list[int] = []
for i in range(10):
    aleatorio.append(random.randint(0, 50))

#- Acessar elementos por índice

if len(lista_preenchida) > 2:
    elemento = lista_preenchida[2]
else:
    elemento = None

#- Percorrer os elementos utilizando for-range

for i in lista_preenchida:
    x = i

#- Percorrer os elementos utilizando for indexado

for i in range(len(lista_preenchida)):
    x = lista_preenchida[i]

#- Procurar um elemento X usando laço

x = 3
achou = False
for i in lista_preenchida:
    if i == x:
        achou = True
        break

#- Procurar um elemento X usando função nativa

achou_n = (x in lista_preenchida)

#- Criar um novo array com elementos filtrados, por exemplo, pares

pares: list[int] = []
for i in lista_preenchida:
    if i % 2 == 0:
        pares.append(i)

#- Criar um novo array com elementos transformados, por exemplo, ao quadrado

quadrados: list[int] = []
for i in lista_preenchida:
    quadrados.append(i*i)

#- Buscar e remover um elemento X

valor = 3
if valor in lista_preenchida:
    lista_preenchida.remove(valor)

#- Remover todos os elementos com valor X da lista

valor = 2
nova_lista: list[int] = []
for i in lista_preenchida:
    if i != valor:
        nova_lista.append(i)

lista_preenchida = nova_lista

#- Verificar quais funções existem nativamente na linguagem

busca = hasattr(lista_preenchida, 'index')
remover = hasattr(lista_preenchida, 'remove')
ordenar = hasattr(lista_preenchida, 'sort')
embaralhar = hasattr(random, 'shuffle')