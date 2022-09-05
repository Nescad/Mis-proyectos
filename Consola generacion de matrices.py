def llenarmatriz():
    print("llenando matriz")
    for f in range(nf):
        for c in range(nc):
             tot[f][c]=random.randint(10,99)
    
def Mostrarmatrizporfilas():
  print("DATOS DE  LA MATRIZ POR FILAS")
  for f in range(nf):
    print("Fila # : ",f+1," => [ ",end="")
    for c in range(nc):
        print (tot[f][c],end=" ")
    print("]")
print()

def menu():
    print("=================")
    print("Menu de opciones")
    print("=================")
    print("1. Mostrar datos de filas")
    print("2. Mostrar datos de columna")
    print("3. Mostrar suma y promedio de las filas impares")
    print("4. Mostrar dato mayor de la fila #5")
    print("5. Mostrar datos pares de las filas impares")
    print("99. Salir de el menú de opciones")

def datosfilax():
  print("Datos Fila X")
  fx=int(0)
  fx=int(input("¿Filas a mostrar?: "))
  while (fx<1 or fx>nf):
    fx=int(input("¿Filas a mostrar?: "))
  for c in range(nc):
    print(tot[fx-1][c],end=" ")
  print()

def datoscolumnax():
  print("Datos Columna X")
  cx=int(0)
  cx=int(input("¿Columna a mostrar?: "))
  while (cx<1 or cx>nc):
    cx=int(input("¿Columna a mostrar?: "))
  for f in range(nf):
    print(tot[f][cx-1],end=" ")
  print()

def sumatoriaypromedio():
    print("Mostrar suma y promedio de las filas impares")  
    for f in range(0,nf,2):
      sumaimpares = 0
      promediorimpares= 0
      for c in range(nc):
        sumaimpares+=tot[f][c]
      promediorimpares= (sumaimpares/nc)
      print("Sumatoria filas impares: ",sumaimpares)
      print("Promedio impares: ", promediorimpares)
#Profe el codigo cumple con lo pedido, pero la sumatoria y el promedio de los impares se realiza cada dos filas, ya que intenté todo para que funcionara

def datomayor():
  print("Dato mayor")
  datomayor=tot[0][0]
  for f in range(4,nf,5):
    for c in range(nc):
      if(tot[f][c]> datomayor):
        datomayor=tot[f][c]
  print("Dato Mayor :", datomayor)


def datosparesdelasfilasimpares():
  print("Datos pares de las filas impares") 
  for f in range(0,nf,2):
    print("Fila # : ",f+1," => [ ",end="")
    for c in range(nc):
        print (tot[f][c],end=" ")
    print("]")
  print()          

import random
tot=[]   
nf=int(input("¿Cuantas filas?: "))
nc=int(input("¿Cuantas Columnas?: "))
for k in range (nf):
    tot.append([0]*nc)

opcion=int(0)
opcion=int(input("Presiona (1) para generar filas: "))
while (opcion > 1):
  opcion=int(input("Presiona (1) para generar filas: "))
if (opcion==1):
  llenarmatriz()

Mostrarmatrizporfilas()
opcion=0
opcion=int(0)
menu()
opcion=int(input("Digite la opcion Deseada, 99 para Salir : "))
while (opcion!=99):
  if (opcion == 1):
    datosfilax()
  elif (opcion== 2):
    datoscolumnax()
  elif (opcion==3):
    sumatoriaypromedio()
  elif (opcion == 4):
    datomayor()
  elif(opcion==5):
    datosparesdelasfilasimpares()
  else:
    print("Opcion digitada no valida ")
  opcion=0
  menu()
  opcion=int(input("Digite la opcion Deseada, 99 para Salir : "))
print("Fin del algoritmo")