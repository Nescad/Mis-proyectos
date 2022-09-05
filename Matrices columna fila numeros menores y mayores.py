import random
mat=[]
mayor=[]
menor=[]
mayor=int(0)
menor=int(0)
nf=int()
nc=int()
nf=int(input("Cuantas filas? :"))
nc=int(input("Cuantas columnas? :"))
for k in range (nf):
    mat.append([0]*nc)


def llenarvector():
    print("llenando matriz")
    for f in range(nf):
        for c in range(nc):
            mat[f][c] = random.randint(10,99)
    print("matriz generada")
    print(mat)

def numeromenor():
    print("de menor a mayor")
    for m in range(menor):
        if(mat<0):
            print("Los números son menores: ", numeromenor)


def numeromayor():
     print("de menor a mayor")
     for n in range(mayor):
        if(mat>=0):
            print("Los números son menores: ", numeromayor)
    

def mostrarmatricesporfilas():
    print("Mostrando matrices por filas")
    mayor=int(0)
    for f in range(nf):
        print("Columna #", f+1, end=" = ")
        for c in range(nc):
            print (mat[f][c])
            print()


def mostrandomatricesporcolumnas():
    print("Mostrando matrices por columnas")
    for c in range(nc):
        print("Fila #", c+1, end=" = ")
        for f in range(nf):
            print(mat[f][c])
        print()

llenarvector()
mostrandomatricesporcolumnas()
mostrarmatricesporfilas()
numeromenor()
numeromayor()

