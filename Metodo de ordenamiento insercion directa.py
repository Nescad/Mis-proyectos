def llenarvector():
  for k in range(n):
    vectorInicial[k]=randint(-99999,99999)

def seleccionDirecta():
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
n=int(input("Cuantos Datos ?"))
vectorInicial=[0]*n
llenarvector() # con 500, 5000, 10000 y 20000
print("VECTOR INICIAL")
print(vectorInicial)
vector=vectorInicial.copy()
print ("Metodo de Intercambio o Burbuja 1")
#TI=time()
burbuja1()
#tf=time()
#td= tf - ti
print("Vector Ordenado con el metodo Burbuja")
print(vector)
print("Tiempo de Duracion: " )