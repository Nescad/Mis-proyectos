def llenarVector():
  print("LLENANDO VECTOR")
  #p=int(input("Cuantos Datos ? :"))
  for k in range(p):
    nros.append(randint(-99,99))
  print("VECTOR GENERADO")
  print(nros)

def pasarImpares():
  print("PASANDO DATOS IMPARES")
  contImpar=int(0)
  sumaImpar=int(0)
  nroMayor=int(-9999999)
  print(p)
  for k in range(p):
    if (nros[k]%2==1):
      vecImpar.append(nros[k])
      sumaImpar = sumaImpar + nros[k]
      contImpar = contImpar + 1
      if (nros[k]>nroMayor):
        nroMayor=nros[k]
  # fin del ciclo
  print("VECTOR DE NUMEROS IMPARES")
  print(vecImpar)
  print("Numero Impar Mayor : ",nroMayor )
  print("Promedio de los nros Impares :",(sumaImpar/contImpar))


def pasarPares():
  print("PASANDO DATOS PARES")
  contPar=int(0)
  sumaPar=int(0)
  nroMenor=int(9999999)
  for k in range(p):
    if (nros[k]%2==0):
      vecPar.append(nros[k])
      sumaPar = sumaPar + nros[k]
      contPar = contPar + 1
      if (nros[k]<nroMenor):
        nroMenor=nros[k]
  # fin del ciclo
  print("VECTOR DE NUMEROS PARES")
  print(vecPar)
  print("Numero Par Menor : ",nroMenor )
  print("Promedio de los nros Pares :",(sumaPar/contPar))

# Algoritmo principal
#
from random import randint
p=int(0)
p=int(input("Cuantos Datos ? :"))
nros=[]
vecImpar=[]
vecPar=[]

#
# Invocamos los metodos
#
llenarVector()
pasarImpares()
pasarPares()