def llenarvector():
  for k in range(n):
    Vectorinicial[k]=randint(-99999,99999)

def Insercciondirecta():
  aux=int(0)
  k=int(0)
  for I in range(1,n):
    aux = vector[I]
    k = I - 1
    while (k>= 0) and (aux < vector[k]):
      vector[k + 1] = vector[k]
      k = k - 1   
    vector[k + 1] = aux

from random import randint
n=int(0)
n=int(input("¿Cuantos datos desea ejecutar?: "))
Vectorinicial=[0]*n
llenarvector()

import time 
inicio= time.time()

print("Vector inicial: ")
print(Vectorinicial)
vector=Vectorinicial.copy()
print("-------------------------------")

print ("Metodo de ordenamiento por inserccion directa: ")
(Insercciondirecta())
print(vector)
print("-------------------------------")

print("Tiempo de Duracion: " )
final=time. time()
tiempo= round(final-inicio) 
print("El tiempo de ejecucion es de: ",tiempo,"segundos")
print("-------------------------------")
