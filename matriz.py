
from tkinter.messagebox import NO
from nodo import nodo
import random 
import pyperclip
import os
class par:
    x = 0
    y=0
    def __init__(self,x,y ):
        self.x = x
        self.y = y
    def __str__ (self):
        return '[x:' + str(self.x) + ',y:' + str(self.y)+']'

class matriz:
    raiz = nodo("root", -1,-1)
    dx = 0
    dy = 0
    ocupados = []
    general = "digraph G\n"+"{label=\"expresion regular\"\n"+"        node[shape = circle]\n"+"        node[style = filled]\n"+"        node[fillcolor = \"#EEEEE\"]\n"+"        node[color = \"#EEEEE\"]\n"+"        node[color = \"#31CEF0\"]\n"+"        edge [style=invis]\n"
    espacios = {
        "pt":4,
        "sub":3,
        "dt":2,
        "b":1
    }


   
    def __init__(self,t ):
        self.dx = t
        self.dy = t
        self.raiz = nodo("root", -1,-1)
        self.ocupados = []
        self.creatodo()
        

    def recursivx(self,rooot, cont, meta):
        if cont == meta:
            print(str(rooot))
            return
        else:
            rooot.derecha = nodo("ejex",cont,-1)
            rooot.derecha.izquierda = rooot
            cont = cont+1
            print(str(rooot))
            self.recursivx(rooot.derecha,cont,meta)
    
    def recursivy(self,rooot, cont, meta):
        if cont == meta:
            print(str(rooot))
            return
        else:
            rooot.abajo = nodo("ejey",-1,cont)
            rooot.abajo.arriba = rooot
            cont = cont +1
            print(str(rooot))
            self.recursivy(rooot.abajo,cont,meta )
    def creatodo(self):
        self.recursivx(self.raiz,0,self.dx)
        self.recursivy(self.raiz,0,self.dy)

    
    def ingresar(self,x,y,barco):
        for n in self.ocupados:
            if(n.x == x and n.y == y):
                return False
        if(x>=self.dx or y >= self.dy or x<0 or y < 0):
            return False
        nuevo_nodo = nodo(barco,x,y)
        print("ingresando: "+str(nuevo_nodo))
        ahora = self.raiz
        while(ahora.c.x != x):
            
            ahora = ahora.derecha
        
        while(ahora != None):
            
            if(ahora.abajo == None and ahora.c.y < y):  
                ahora.abajo = nuevo_nodo
                ahora.abajo.arriba = ahora
                
            elif(ahora.abajo!= None and ahora.abajo.c.y >y and ahora.c.y < y):
                aux = ahora.abajo
                ahora.abajo = nuevo_nodo
                ahora.abajo.arriba = ahora
                ahora.abajo.abajo = aux
                ahora.abajo.abajo.arriba = ahora.abajo
            ahora = ahora.abajo
        ahora = self.raiz
        #ahora toca de lado de y para ingresar en x 
        while(ahora.c.y != y):
            
            ahora = ahora.abajo
        
        while(ahora != None):
            if(ahora.derecha == None and ahora.c.x < x):
                ahora.derecha = nuevo_nodo
                ahora.derecha.izquierda = ahora
                self.ocupados.append(par(x,y))
                return True
            elif(ahora.derecha!= None and ahora.derecha.c.x >x and ahora.c.x < x):
                aux = ahora.derecha
                ahora.derecha = nuevo_nodo
                ahora.derecha.izquierda = ahora
                ahora.derecha.derecha = aux
                ahora.derecha.derecha.izquierda = ahora.derecha
                self.ocupados.append(par(x,y))
                return True
            ahora = ahora.derecha
    def eliminar(self,x,y):
        if(x>self.dx or y> self.dy):
            return False                #SOLO SE UTILIZAN DOS CASOS EN LA ELIMINACION YA QUE DE FIJO 
        bandera = False    #SIEMPRE VA A TENER NODO A LA IZQUIERDA Y ARRIBA, POR LO QEU PUEDE FACTORIZARSE
        for n in self.ocupados:#A UN CASO GENERAL
            if(n.x == x and n.y == y):
                bandera = True
        if bandera == True:
            ahora = self.raiz
            while(ahora.c.x != x):
                ahora = ahora.derecha
            while(ahora.c.y != y):
                ahora = ahora.abajo
            ahora.arriba.abajo = ahora.abajo
            if(ahora.abajo != None):
                ahora.abajo.arriba = ahora.arriba
            ahora.izquierda.derecha = ahora.derecha
            if(ahora.derecha != None):
                ahora.derecha.izquierda = ahora.izquierda
            ahora= None
            for n in self.ocupados:
                if(n.x == x and n.y == y):
                    self.ocupados.remove(n)
        return bandera


    def var(self,x,y,B):
        p = range(y,y+self.espacios[B])
        for ny in p:
            if(not(self.ingresar(x,ny,B))):
                p2 = range(y,ny)
                for eny in p2:
                    self.eliminar(x,eny)#ESTA CONFUNCIENDO EL FALSE DE SALIDA PQ TAMBIEN BORRA EL NODO QUE YA SE ENCONTRABA AHI
                return False
        return True
    def vab(self,x,y,B):
        p = range(y+1-self.espacios[B],y+1)
        for ny in p:
            if(not(self.ingresar(x,ny,B))):
                p2 = range(y+1-self.espacios[B],ny)
                for eny in p2:
                    self.eliminar(x,eny)
                return False
        return True
    def vder(self,x,y,B):
        p = range(x,x+self.espacios[B])
        for ny in p:
            if(not(self.ingresar(ny,y,B))):
                p2 = range(x,ny)
                for eny in p2:
                    self.eliminar(eny,y)
                return False
        return True
    def viz(self,x,y,B):
        p = range(x+1-self.espacios[B],x+1)
        for ny in p:
            if(not(self.ingresar(ny,y,B))):
                p2 = range(x+1-self.espacios[B],ny)
                for eny in p2:
                    self.eliminar(eny,y)
                return False
        return True




    def llenadoautom(self,x,y,b):
        for n in self.ocupados:
            if(n.x == x and n.y == y):
                self.llenadoautom(random.randint(0,self.dx-1),random.randint(0,self.dy-1),b)
                return
        if self.var(x,y,b):
            print("lo hizo arriba")
        elif self.vab(x,y,b):
            print("lo hizo abajo")
        elif self.vder(x,y,b):
            print("lo hizo derecha")
        elif self.viz(x,y,b):
            print("lo hizo izquierda")
        else:
            self.llenadoautom(random.randint(0,self.dx-1),random.randint(0,self.dy-1),b)
    def llenadomanual(self,x,y,b):    
        for n in self.ocupados:
            if(n.x == x and n.y == y):
                print("ESTA CASILLA YA ESTA OCUPADA")
                return False
        if self.var(x,y,b):
            print("lo hizo arriba")
            return True
        elif self.vab(x,y,b):
            print("lo hizo abajo")
            return True
        elif self.vder(x,y,b):
            print("lo hizo derecha")
            return True
        elif self.viz(x,y,b):
            print("lo hizo izquierda")
            return True
        else:
            print("IMPOSIBLE COLOCAR EN ESTA CASILLA")
            return False


        
    def conexionesa(self):
        n = self.raiz
        while n!= None:
            p=n
            while p.abajo != None:
                self.general+="\n"+str(id(p))+"->"+str(id(p.abajo))+ "[dir = both];"
                p=p.abajo
            n=n.derecha
    def conexionesd(self):
        n = self.raiz
        while n!= None:
            p=n
            while p.derecha != None:
                if( (p.barco!= "ejex" and p.derecha.barco != "ejex") or (p.barco!= "root" and p.derecha.barco != "ejex")):
                    self.general+="\n"+str(id(p))+"->"+str(id(p.derecha))+ "[constraint=false,dir = both];"
                else:
                    self.general+="\n"+str(id(p))+"->"+str(id(p.derecha))+ "[dir = both];"

                p=p.derecha
            n=n.abajo
    def rank(self):
        
        n = self.raiz
        while n!=None:
            p=n
            self.general+="\n {rank=same; "
            while p!=None:
                self.general+=str(id(p))+";"
                p=p.derecha
            n=n.abajo
            self.general+="}"
        
            

    def impder(self, n):
        while(n != None):
            color = "white"
            if n.barco == "pt":
                color = "gray"
            elif n.barco == "sub":
                color = "red"
            elif n.barco == "dt":
                color = "blue"
            elif n.barco == "b":
                color = "pink"
            elif n.barco == "golpe":
                color = "green"
            elif n.barco == "missed":
                color = "red"
            
            
            self.general+="\n"+str(id(n))+ "[label=\"" + str(n)+"\","+"fillcolor = \""+color+"\"]"
            print(str(n),end = ' ')
            n = n.derecha

    def imprime(self, n):
        while(n!=None):
            
            print("FILA: ",end = ' ')
            self.impder(n)
            print("\n")
            n = n.abajo
    def muestra(self):
        self.imprime(self.raiz)

    def impderc(self, n):
        while(n != None):
            print('['+ str(n.c)+']',end = ' ')
            n = n.derecha
    def imprimec(self, n):
        while(n!=None):
            print("FILA: ",end = ' ')
            self.impderc(n)
            print("\n")
            n = n.abajo
    def muestrac(self):
        print("----------------------------------------------")
        self.imprimec(self.raiz)
        print("----------------------------------------------")
    def grapvzix(self,a):
        self.general = general = "digraph G\n"+"{label=\"expresion regular\"\n"+"        node[shape = square]\n"+"        node[style = filled]\n"+"        node[fillcolor = \"#EEEEE\"]\n"+"        node[color = \"#EEEEE\"]\n"+"        node[color = \"#31CEF0\"]\n"
        self.imprime(self.raiz)
        self.conexionesa()
        self.conexionesd()
        self.rank()
        self.general+="\n}"
        pyperclip.copy(self.general)
        f = open(f'{a}.dot', "w")
        f.write(self.general)
        f.close()
        os.system(f'dot -Tpng {a}.dot -o {a}.png')
        #print(self.general)
    def basico_automatico(self):
        self.llenadoautom(random.randint(0,9),random.randint(0,9),"pt")
        self.llenadoautom(random.randint(0,9),random.randint(0,9),"sub")
        self.llenadoautom(random.randint(0,9),random.randint(0,9),"sub")
        self.llenadoautom(random.randint(0,9),random.randint(0,9),"dt")
        self.llenadoautom(random.randint(0,9),random.randint(0,9),"dt")
        self.llenadoautom(random.randint(0,9),random.randint(0,9),"dt")
        self.llenadoautom(random.randint(0,9),random.randint(0,9),"b")
        self.llenadoautom(random.randint(0,9),random.randint(0,9),"b")
        self.llenadoautom(random.randint(0,9),random.randint(0,9),"b")
        self.llenadoautom(random.randint(0,9),random.randint(0,9),"b")


    def para_compu(self):
        n = self.dx
        if n == 10:
            self.basico_automatico()
        elif n>10 and n<=20:
            for n in range(2):
                self.basico_automatico()
        elif n > 20:
            meta = ((n-1)/10)+1
            print(int(meta))
            for n in range(int(meta)):
                self.basico_automatico()
    
        

    ##def ingresarvertical():


    #def ingresarhorzontal():

 
        


   
 

            