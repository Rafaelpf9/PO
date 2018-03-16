import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
from timeit import timeit
from random import randint
import numpy as np
import scipy.interpolate as interpolate
import math
 
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

def desenhaGrafico(x,y,w,xl = "Nº de Elementos", yl = "Tempo(s)"):
    fig = plt.figure(figsize=(10, 10))
    ax = fig.add_subplot(111)
    xnew = np.linspace(min(x), max(x), 10 * (max(x) - min(x)))
    a, b, c = interpolate.splrep(x, y, s=0, k=2)
    suave = interpolate.BSpline(a, b, c, extrapolate=False)
    d, e, f = interpolate.splrep(x, w, s=0, k=2)
    suave2 = interpolate.BSpline(d, e, f, extrapolate=False)
    plt.plot(xnew, suave2(xnew), label="Decrescente")
    plt.plot(xnew, suave(xnew), label="Aleatória")
    ax.legend(bbox_to_anchor=(1, 1),bbox_transform=plt.gcf().transFigure)
    plt.ylabel(yl)
    plt.xlabel(xl)
    plt.title('heapsort', fontsize=18)
    fig.savefig('heapsort.png')
 
def heapsort(lists):
    def heapify(lists):
        start=(len(lists)-2)//2
        while start>=0:
            siftDown(lists,start,len(lists)-1)
            start-=1

    def siftDown(lists, start, end):
        root = start
        while root*2+1<=end:
            child = root * 2 + 1
            if child + 1 <= end and lists[child] < lists[child + 1]:
                child += 1
            if child <= end and lists[root] < lists[child]:
                lists[root], lists[child] = lists[child], lists[root]
                root = child
            else:
                return

    heapify(lists)
    end = len(lists) - 1
    while end > 0:
        lists[end], lists[0] = lists[0], lists[end]
        siftDown(lists, 0, end - 1)
        end -= 1

 
 
aleatorio = []
decrescente = []
x = [1000, 3000, 6000, 9000, 12000, 15000, 18000, 21000, 24000]
for i in x:
    aleatorio.append(timeit("heapsort({})".format(geraLista(i)), setup="from __main__ import heapsort", number=1))
    decrescente.append(timeit("heapsort({})".format(geraListaDecrescente(i)), setup="from __main__ import heapsort", number=1))
desenhaGrafico(x, aleatorio, decrescente)
