import random
class Nodo:
    def __init__(self , info= None, siguiente= None):
        self.info=info
        self.siguiente=siguiente


    def verNodo(self):
        return self.info
class Lista:
    def __init__(self):
        self.primero = None
        self.longitud =0

    def insertarPrimer(self, dato):
        p =Nodo(dato)
        p.siguiente =self.primero
        self.primero = p
        self.longitud +=1

    def insertarUltimo(self,dato):
        nuevo =Nodo(dato)
        if self.primero == None:
            self.primero == nuevo
            self . longitud =  1
        else:
            p = self.primero
            while p.siguiente != None:
                p = p.siguiente
            p.siguiente = nuevo
            self.longitud +=1

    def listar(self):
        print ("[",end="")
        p = self.primero
        while p != None:
            print (p.verNodo(),end=" ")
            if p.siguiente != None:
                print (",",end="")
            p = p.siguiente
        print ("]")

    def ordenar(self):
        p=self.primero
        if p==None:
            print ("Lista vacia")

        else:
            q=p
            while q.siguiente!=None:
                r=q.siguiente
                while r!=None:
                    if r.info<q.info:
                        aux=r.info
                        r.info=q.info
                        q.info=aux
                    r=r.siguiente
                q=q.siguiente

    def eliminar(self, val):
        q = self.primero
        r = self.primero
        while r.info != val and r.siguiente != None:
            q = r
            r = r.siguiente
        if r.info == val:
            q.siguiente = r.siguiente
            self.longitud -= 1
        if r == self.primero:
            self.primero = r.siguiente
            self.longitud -= 1


    def Eliminar_inicio(self):
        if self.primero!=None:
            self.primero=self.primero.siguiente
            self.longitud-=1

    def eliminar_al_final(self):
        anterior = self.primero
        actual = self.primero
        while actual.siguiente is not None:
            anterior = actual
            actual = actual.siguiente
        anterior.siguiente = None
        self.longitud -= 1



    def Cambiar_valor(self, pos, valor):
        q = self.primero
        k = 0
        if pos > 0:
            while k != pos and q.siguiente != None:
                q = q.siguiente
                k += 1
            if k == pos:
                q.info = valor
        else:
            q.info = valor



    def buscar(self,dat):
        p = self.primero
        if p != None:
            while p != None:
                if p.info == dat:
                    print ("Se encontro")
                    return True
                p= p.siguiente
        print ("No se encontro")
        return False

    def borrarPos(self, pos):
        q = self.primero
        r = self.primero
        k = 0
        if pos > 0:
            while k != pos and r.siguiente is not None:
                q = r
                r = r.siguiente
                k += 1
            if k == pos:
                q.siguiente = r.siguiente
                self.longitud -= 1
        else:
            self.primero = r.siguiente
            self.longitud -= 1

    def numero_mayor(self):
        mayor = 0
        p = self.primero
        while p is not None:
            if p.info > mayor:
                mayor = p.info
            p = p.siguiente
        print (mayor)
        return mayor

    def numero_menor(self):
        menor = 0
        p = self.primero
        while p is not None:
            if menor == 0:
                menor = p.info
            elif menor > p.info:
                menor = p.info
            p = p.siguiente
        print (menor)
        return menor

    def cantidad_primos(self):
        primo=[]
        p = self.primero
        while p is not None:
            cont = 0
            for i in range(1, p.info+1):
                if p.info % i == 0:
                    cont += 1
                if cont == 2 and p.info != 1:
                    primo.append(p.info)
            p = p.siguiente
        print (cont)
    def rotarLista(self):
        actual= self.primero
        anterior = self.primero
        dato = self.primero.info
        while actual.siguiente != None:
            actual = actual.siguiente
            anterior.info = actual.info
            anterior = actual
            if actual.siguiente == None:
                actual.info = dato

    def unoSIotroNo(self):
      par = True
      print("[",end="")
      p = self.primero
      while p != None:
          if par:
            print(p.verNodo(),end="")
            if p.siguiente != None:
                print(",",end="")
          par = not par
          p = p.siguiente
      print("]")


    def mostrarLosUltimosXnodos(self, val):
      i = 0
      print("[",end="")
      p = self.primero
      while p != None:
          if i>= self.longitud - val:
            print(p.verNodo(),end="")
            if p.siguiente != None:
                print(",",end="")
          p = p.siguiente
          i+=1
      print("]")

    def mostrarDatoMasCentral(self):
        posCentro = self.longitud//2
        i = 0
        print("[",end="")
        p = self.primero
        while p != None:
            if i==posCentro:
                print(p.verNodo(),end="")
            p = p.siguiente
            i+=1
        print("]")


lista=Lista()
lista1=Lista()
for i in range(11):
    lista.insertarPrimer(random.randint(0,50))
lista.listar()
salir=False
while salir!=True:
    opcion=int(input("Seleccione lo que desea realizar... \n1. Adicionar \n2. Consultar \n3. Eliminar  \n4. Operar \n5. Crear nueva lista \n6. Mostrar los numeros de la lista intercalada \n7. Mostrar los ultimos nodos de la lista en X \n8. Mostrar los nodos de la lista central \n9. Salir de la consola \n\n Ingrese la opcion: "))

    if opcion==1:
        opcion1=int(input("Seleccione lo que desea realizar... \n1. Insertar al inicio \n2. Insertar al final \n3. Ordenar \n4.Salir  \n\n Ingrese la opcion: "))
        if opcion1==1:
            print ("Esta adicionando al inicio")
            x=int(input("Digite el valor a ingresar al inicio: "))
            lista.insertarPrimer(x)
            lista.listar()
        elif opcion1==2:
            y=int(input("Digite el valor a ingresar al final: "))
            lista.insertarUltimo(y)
            lista.listar()
        elif opcion1==3:
            lista.ordenar()
            lista.listar()
        elif opcion1==4:
            salir=True
    elif opcion==2:
        opcion2=int(input("Seleccione lo que desea realizar... \n1. Cambiar Valor  \n2. Buscar \n3. Rotar lista \n4. Salir  \n\n Ingrese la opcion: "))
        if opcion2==1:
            a=int(input("Ingrese la posicion a cambiar: "))
            c=int(input("Ingrese el valor a cambiar: "))
            lista.Cambiar_valor(a,c)
            lista.listar()
        elif opcion2==2:
            v=int(input("Ingrese el valor a buscar: "))
            lista.buscar(v)
        elif opcion2==3:
            lista.rotarLista()
            lista.listar()
        elif opcion2==4:
            salir=True
    elif opcion==3:
        opcion3=int(input("Seleccione lo que desea realizar... \n1. Eliminar al inicio \n2. Eliminar al final \n3. Eliminar valor \n4. Eliminar Posicion \n5. Salir  \n\n Ingrese la opcion: "))
        if opcion3==1:
            lista.Eliminar_inicio()
            lista.listar()
        elif opcion3==2:
            lista.eliminar_al_final()
            lista.listar()
        elif opcion3==3:
            val=int(input("Ingrese el valor a borrar: "))
            lista.eliminar(val)
            lista.listar()
        elif opcion3==4:
            pos=int(input("Ingrese la posicion a borrar: "))
            lista.borrarPos(pos)
            lista.listar()
        elif opcion3==5:
            salir=True
    elif opcion==4:
        opcion4=int(input("Seleccione lo que desea realizar... \n1. Catidad de primos  \n2. Numero Mayor  \n3. Numero Menor  \n4. Salir   \n\n Ingrese la opcion: "))
        if opcion4==1:
            lista.cantidad_primos()
        elif opcion4==2:
            lista.numero_mayor()
        elif opcion4==3:
            lista.numero_menor()
        elif opcion4==4:
            salir=True
    elif opcion==5:
        tama=int(input("Ingrese tamaño de la lista: "))
        for i in range(tama):
            lista1.insertarPrimer(random.randint(0,50))
        lista=lista1
        lista1.listar()
    elif opcion==6:
        opcion6= int(input("Seleccione lo que desea realizar... \n Presiona (1) para mostrar los numeros intercalados \n Presiona (2) para salir \n\n Ingrese la opcion:  "))
        if opcion6==1:
            lista.unoSIotroNo()
        elif opcion6==2:
            salir==True
    elif opcion==7:
        opcion7=int(input("Seleccione lo que desea realizar... \n Presiona (1) para mostrar los ultimos (X) nodos de la lista \n Presiona (2) para salir \n\n Ingrese la opcion:  "))
        if opcion7==1:
            val=int(input("Ingrese los (X) ultimos nodos a formar de la lista: "))
            lista.mostrarLosUltimosXnodos(val)    
        elif opcion7==2:
            salir=True
    elif opcion==8:
        opcion8=int(input("Seleccione lo que desea realizar... \n Presiona (1) para mostrar el nodo de la lista central \n Presiona (2) para salir \n\n Ingrese la opcion:  "))
        if opcion8==1:
            lista.mostrarDatoMasCentral()
        elif opcion7==2:
            salir=True
    elif opcion==9:
        salir=True




