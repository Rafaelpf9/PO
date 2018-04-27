import matplotlib as mpl
mpl.use('Agg')
from timeit import timeit
from random import randint,choice
import matplotlib.pyplot as plt
import numpy as np
import scipy.interpolate as interpolate

def geraLista(tam):
    lista = []
    for i in range(tam):
        n = randint(1,1*tam)
        if n not in lista: 
          lista.append(n)
    return lista
    

def desenhaGrafico(x,y,y2,y3):
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111)
    ax.plot(x,y, label = "linear")
    ax.plot(x,y2, label = "binária")
    ax.plot(x,y3, label = "diferença")

    ax.legend(bbox_to_anchor=(1, 1),bbox_transform=plt.gcf().transFigure)
    plt.ylabel("tempo")
    plt.xlabel("N")
    plt.title('Gráfico ',fontsize=20)
    fig.savefig('grafico.png')
def pesquisalinear( seq, x):
    for i in range(len(seq)):
        if seq[i] == x:
            return 1
    return 0
def binaria(vet, num):
	esquerda, direita, tentativa = 0, len(vet), 1
	while 1:
		meio = (esquerda + direita) // 2
		aux_num = vet[meio]
		if num == aux_num:
			return tentativa
		elif num > aux_num:
			esquerda = meio
		else:
			direita = meio
		tentativa += 1
		
x=[6000,9000,12000,15000,24001]
t1=[]
t2=[]
t3=[]
t=0
t4=0
for i in x:
    lista = geraLista(i)
    lista.sort()
    for q in range(0,10):
      a =choice(lista)
      t += timeit("pesquisalinear({},{})".format(lista,a),setup="from __main__ import pesquisalinear",number=1)
      t4 += timeit("binaria({},{})".format(lista,a),setup="from __main__ import binaria",number=1)
    t= t/10
    t4=t4/10
    t1.append(t)
    t2.append(t4)
    t3.append((t-t4))

desenhaGrafico(x,t1,t2,t3)
