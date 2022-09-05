import random
Pagos=[] 
nf=int(0)
nc=int(0)   
nf=int(input("Digite el número de filas: "))
nc=int(input("Digite el número de columnas: "))
for k in range (nf):
    Pagos.append([0]*nc)

def Llenarmatrizalazar():
  print("Llenando la matriz")
  for f in range (nf):
    for c in range (nc):
        Pagos[f][c] = random.randint(10,99)

def Mostrarmatrizporfilas():
  print("Datos de la matriz por filas")
  for f in range(nf):
    print("Fila # : ",f+1," => [ ",end="")
    for c in range(nc):
        print (Pagos[f][c],end=" ")
    print("]")
  print()

def menu():
    print("=================")
    print("Menu de opciones")
    print("=================")
    print("1. Mostrar datos pares de las filas impares. ")
    print("2. Mostrar la diagonal de los datos. ")
    print("3.Mostrar los datos de las dos últimas columnas.")
    print("4. Salir de las opciones. ")


def datosparesdelasfilasimpares():
  print("Datos pares de las filas impares") 
  for f in range(0,nf,2):
    print("Fila # : ",f+1," => [ ",end="")
    for c in range(nc):
        print (Pagos[f][c],end=" ")
    print("]")
  print()  

def Diagonalmatriz():
  print("Datos de la diagonal")
  Diagonal=[]
  for f in range(len((Pagos))):
    Diagonal.append(Pagos[f][f])
  print(Diagonal)
    
def Matrizdosultimascolumnas():
  print("Datos de las dos últimas columnas: ")
  cf=int(0)
  cm=int(0)
  for f in range(nf):
    print(end="[")
    print(Pagos[f][cm-2],end=" ")
    print (Pagos[f][cf-1],end=" ")
    print("]")
print()
    
opcion=int(0)
opcion=int(input("Presiona (1) para generar filas aleatorias: "))
while (opcion < 1):
  opcion=int(input("Presiona (1) para generar filas: "))
if (opcion==1):
    Llenarmatrizalazar()

Mostrarmatrizporfilas()
opcion=0
opcion=int(0)
menu()
opcion=int(input("Digite la opción deseada, si desea salir presionar (4): "))
while (opcion!=4):
  if (opcion == 1):
    datosparesdelasfilasimpares()
  elif (opcion==2):
    if(nf==nc):
      Diagonalmatriz()
    else:
      print("Opción no valida")
  elif(opcion==3):
    Matrizdosultimascolumnas()
    
  opcion=0
  menu()
  opcion=int(input("Digite la opción deseada, si desea salir presionar (4): "))
print("Fin del algoritmo")


  
