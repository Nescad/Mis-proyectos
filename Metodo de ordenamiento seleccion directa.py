def llenarvector():
  for k in range(n):
    Vectorinicial[k]=randint(-99999,99999)

def Selecciondirecta():
    for i in range(len(vector)):
        menor=vector[i]
        for j in range(i+1, len(vector)):
            if vector[j]< menor :
                menor = vector[j]
                aux=vector[i]
                vector[i]=menor
                vector[j]=aux

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

print ("Metodo de ordenamiento por seleccion directa: ")
(Selecciondirecta())
print(vector)
print("-------------------------------")

print("Tiempo de Duracion: " )
final=time. time()
tiempo= round(final-inicio) 
print("El tiempo de ejecucion es de: ",tiempo,"segundos")
print("-------------------------------")

