import matplotlib as mpl
mpl.use('Agg')
from timeit import timeit
from random import randint
import matplotlib.pyplot as plt

def listaAleatoria(tam):
  lista = [] 
  for i in range(tam):
    n = randint(1,1*tam)
    lista.append(n)
  return lista

def listaReversa(tam):
  lista = []
  n = tam
  for i in range(tam):
    lista.append(n)
    n=n-1
  return lista

def bubbleSort(lista):
  for i in range(0,len(lista)):
    for j in range(i+1,len(lista)):
      if lista[i] > lista[j]:
        aux = lista[i]
        lista[i] = lista[j]
        lista[j] = aux
  retorno = lista
  return retorno
  
time1 = []
time2 = []
length = []
for tam in range(3000,24001,3000):
    lista1 = listaAleatoria(tam)
    lista2 = listaReversa(tam)
    tempo1 = timeit("bubbleSort({})".format(lista1),setup="from __main__ import \
                    bubbleSort",number = 1)
    tempo2 = timeit("bubbleSort({})".format(lista2),setup="from __main__ import \
                    bubbleSort",number = 1)
    time1.append(tempo1)
    time2.append(tempo2)
    length.append(tam)
    

def desenhaGrafico(x,y,k,xl = "Entradas", yl = "Saídas"):
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111)
    ax.plot(x,y, label = "Caso medio")
    ax.plot(x,k, label = "Pior caso")
    ax.legend(bbox_to_anchor=(1, 1),bbox_transform=plt.gcf().transFigure)
    plt.ylabel(yl)
    plt.xlabel(xl)
    fig.savefig('BubbleSort.png')
