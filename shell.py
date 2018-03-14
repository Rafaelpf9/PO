import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
from timeit import timeit
from random import randint


def desenha_grafico(x, y, z, xl = "N", yl = "TEMPO"):
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111)
    ax.plot(x, y, label = "Lista Aleatória")
    ax.plot(x, z, label = "Lista Reversa")
    ax.legend()
    plt.ylabel(yl)
    plt.xlabel(xl)
    plt.title('Shell Sort')
    fig.savefig('grafico-shell-sort.png')


def gera_lista_aleatoria(tam):
    lista = []
    for i in range(tam):
        n = randint(1, 1*tam)
        if n not in lista: lista.append(n)
    return lista
 
 
def gera_lista_reversa(tam):
    lista = []
    for i in range(tam):
      lista.append(tam-i)
    return lista


def radix_sort(random_list):
    len_random_list = len(random_list)
    modulus = 10
    div = 1
    while True:
        # empty array, [[] for i in range(10)]
        new_list = [[], [], [], [], [], [], [], [], [], []]
        for value in random_list:
            least_digit = value % modulus
            least_digit //= div
            new_list[least_digit].append(value)
        modulus = modulus * 10
        div = div * 10

        if len(new_list[0]) == len_random_list:
            return new_list[0]

        random_list = []
        rd_list_append = random_list.append
        for x in new_list:
            for y in x:
                rd_list_append(y)


n = [1000, 3000, 6000, 9000, 12000, 15000, 18000, 21000, 24000]
#n = [10, 20, 30, 40, 50]

tempo1 = []
tempo2 = []

for i in n:
    lista = gera_lista_aleatoria(i)
    tempo1.append(timeit("radix_sort({})".format(lista), setup="from __main__ import radix_sort", number=1))
    lista = gera_lista_reversa(i)
    tempo2.append(timeit("radix_sort({})".format(lista), setup="from __main__ import radix_sort", number=1))
  
desenha_grafico(n, tempo1, tempo2)
