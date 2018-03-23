import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
from timeit import timeit
from random import randint
import numpy as np
import scipy.interpolate as interpolate


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
    plt.title('gnomeSort', fontsize=18)
    fig.savefig('gnomeSort.png')


def gnomeSort(lista):
    pivo = 0
    tam = len(lista)
    while pivo < tam - 1:
        if lista[pivo] > lista[pivo+1]:
            lista[pivo+1], lista[pivo] = lista[pivo], lista[pivo+1]
            if pivo > 0:
                pivo -= 2
        pivo += 1


aleatorio = []
decrescente = []
x = [1000, 3000, 6000, 9000, 12000, 15000, 18000, 21000, 24000]
for i in x:
    aleatorio.append(timeit("gnomeSort({})".format(geraLista(i)), setup="from __main__ import gnomeSort", number=1))
    decrescente.append(timeit("gnomeSort({})".format(geraListaDecrescente(i)), setup="from __main__ import gnomeSort", number=1))
desenhaGrafico(x, aleatorio, decrescente)
