def llenarvector():
  for k in range(n):
    Vectorinicial[k]=randint(-99999,99999)

def Insercionbinaria():
    for i in range(1, len(vector)):
        aux = vector[i]
        izq = 0
        der = i - 1
        while izq <= der:
            m = int((izq + der) / 2)
            if aux < vector[m]:
                der = m - 1
            else:
                izq = m + 1

        j = i - 1
        while j >= izq:
            vector[j + 1] = vector[j]
            j = j - 1
        vector[izq] = aux

from random import randint
n=int(0)
n=int(input("¿Cuantos datos desea ejecutar?:"))
Vectorinicial=[0]*n
llenarvector() 

import time 
inicio= time.time()

print("Vector inicial: ")
print(Vectorinicial)
vector=Vectorinicial.copy()
print("-------------------------------")

print ("Metodo de ordenamiento por insercion binaria: ")
(Insercionbinaria())
print(vector)
print("-------------------------------")

print("Tiempo de Duracion: " )
final=time. time()
tiempo= round(final-inicio) 
print("El tiempo de ejecucion es de: ",tiempo,"segundos")
print("-------------------------------")

