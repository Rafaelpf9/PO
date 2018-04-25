import matplotlib as mpl
mpl.use('Agg')
from timeit import timeit
from random import randint
import matplotlib.pyplot as plt

def geraLista(tam):
  lista = [] 
  for i in range(tam):
    n = randint(1,1*tam)
    if n not in lista:lista.append(n)
  return lista

def Bubble(lista):
  for i in range(0,len(lista)):
    for j in range(i+1,len(lista)):
      if lista[i] > lista[j]:
        aux = lista[i]
        lista[i] = lista[j]
        lista[j] = aux
  retorno = lista
  return retorno
  
time = []
length = []
for tam in range(3000,24001,3000):
    lista = geraLista(tam)
    tempo = timeit("Bubble({})".format(lista),setup="from __main__ import \
                    Bubble",number = 1)
    time.append(tempo)
    length.append(tam)
    
def desenhaGrafico(x,y,xl = "Entradas", yl = "Saídas"):
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111)
    ax.plot(x,y, label = "Melhor Tempo")
    ax.legend(bbox_to_anchor=(1, 1),bbox_transform=plt.gcf().transFigure)
    plt.ylabel(yl)
    plt.xlabel(xl)
    plt.title('Tamanho x Tempo',fontsize=20)
    fig.savefig('graph.png')
    
desenhaGrafico(length,time,"Tamanho","Tempo(s)")
