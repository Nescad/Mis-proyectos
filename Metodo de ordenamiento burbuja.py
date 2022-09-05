def llenarvector():
  for k in range(n):
    Vectorinicial[k]=randint(-99999,99999)

def Burbuja1():
  aux=int(0) 
  for j in range(n-1):
    for k  in range(j+1,n): 
      if vector[k] < vector[j]:
        aux =  vector[j]
        vector[j]  = vector[k]
        vector[k]  = aux
               
def Burbuja2():
  print("Metodo de intercambio o Burbuja 2: ")
  Ordenado=bool(True)
  for k in range(n-2):
    if (vector[k+1] < vector[k]):
      Ordenado=False
      break
  if  (Ordenado):
    print("Vector ordenado")
  else:
    Burbuja1()

from random import randint
n=int(0)
n=int(input("¿Cuantos datos desea ejecutar?: "))
Vectorinicial=[0]*n
llenarvector()
print("-------------------------------")

import time 
inicio= time.time()

print("Vector inicial: ")
print(Vectorinicial)
vector=Vectorinicial.copy()
print("-------------------------------")

print ("Metodo de Intercambio o Burbuja 1: ")
(Burbuja1())
print(vector)
print("-------------------------------")

vector=Vectorinicial.copy()
(Burbuja2())
print(vector)
print("-------------------------------")

print("Tiempo de Duracion" )
final=time. time()
tiempo= round(final-inicio) 
print("El tiempo de ejecucion es de: ",tiempo,"segundos")
print("-------------------------------")

