import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
from timeit import timeit
from random import randint

def geraLista(tam):
    lista = []
    for i in range(tam):
        n = randint(1,1*tam)
        if n not in lista: lista.append(n)
    return lista

def geraListaDecrescente(tam):
  lista = []
  x = tam
  for i in range(tam):
    lista.append(x)
    x -= 1
  return lista

def desenhaGrafico(x,y,z,xl = "Nº de Elementos", yl = "Tempo(s)"):
    fig = plt.figure(figsize=(10, 10))
    ax = fig.add_subplot(111)
    ax.plot(x,y, label = "Caso Médio")
    plt.plot(x, z, label="Pior Caso")
    ax.legend(bbox_to_anchor=(1, 1),bbox_transform=plt.gcf().transFigure)
    plt.ylabel(yl)
    plt.xlabel(xl)
    fig.savefig('countingsort.png')
    
def countingsort(lista,maxval):
    n = len(lista)
    m = maxval + 1
    count = [0] * m
    for a in lista:
        count[a] += 1
        i = 0
    for a in range(m):
        for c in range(count[a]):
            lista[i] = a
            i += 1
    return lista
        
casoMedio= []
piorCaso = []
x = [1000,3000,6000,9000,12000,15000,18000,21000,24000]
for i in x:
    x1= geraLista(i)
    tempoMedio = timeit("countingsort({},{})".format(x1,max(x1)),setup="from __main__ import countingsort",number=1)
    for j in range(i):
        n = tempoMedio
        if n not in casoMedio: casoMedio.append(n)
    x2 = geraListaDecrescente(i)    
    tempoPior = timeit("countingsort({},{})".format(x2,max(x2)),setup="from __main__ import countingsort",number=1)
    for k in range(i):
        m = tempoPior
        if m not in piorCaso: piorCaso.append(m)
desenhaGrafico(x,casoMedio,piorCaso)
