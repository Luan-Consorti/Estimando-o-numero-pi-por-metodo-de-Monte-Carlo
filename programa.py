
import random
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
import numpy as np

#função que gera os pontos
def gera_pontos(n):
  lista_pontos = []
  for i in range(n):
    lista_pontos.append([random.uniform(-1,1),random.uniform(-1, 1)])
  return lista_pontos

#indicadora
def indicadora(valor):
  if valor <= 1: return 1
  else: return 0

#função que calcula o valo de pi e a estimativa para n
def Estimativa_n(erro,conf,n):
    soma = 0
    #indicadora
    for k in gera_pontos(n):
      soma+= indicadora(np.linalg.norm(k))
    #estimativa para pi 
    ste_pi = (soma/n ) * 4
    #desvio padrao da variancia de uma Bernoulli 
    desvp = np.sqrt(ste_pi/4 * (1-(ste_pi/4)))
    #margem de erro
    erro_aprx = (erro/4)*ste_pi
    #
    t = np.ceil((conf * desvp / erro) ** 2)
    print('\n valor estimado para pi: ',ste_pi)
    print('\n variância: ',desvp**2)
    print("\n Número de amostras: ", t)
    print("\n Erro relativo: ", erro_aprx)
    print('\n Gráfico: \n')

#função para plotar o gráfico
def plot_grfc(n):
    fig, ax = plt.subplots()
    circle = Circle((0,0), 1, facecolor='lightgrey', edgecolor='black', linewidth=1, alpha=0.8)
    ax.add_patch(circle)
    ax.set_aspect('equal')
    ax.set_xlim([-1.2,1.2])
    ax.set_ylim([-1.2,1.2])
    x, y = zip(*gera_pontos(n))
    plt.scatter(x, y, color='black')
    return plt.show()

#main
def Main():
    n = int(input("Insira números de pontos desejados: "))
    Estimativa_n(0.0005,1.96,n)
    plot_grfc(n)

Main()

