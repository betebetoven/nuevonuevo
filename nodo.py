from coordenadas import coordenadas


class nodo:
    arriba= None
    abajo = None
    derecha = None
    izquierda = None
    c = None
    barco = ""
    def __init__(self, barc,x,y):
        self.barco = barc
        self.c = coordenadas(x,y)
    def __str__ (self):
        return '{c:[' + str(self.c) + '],b:' + self.barco+'}'