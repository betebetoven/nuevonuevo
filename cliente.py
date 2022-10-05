
import requests##pip3 install request
import json
from tkinter.filedialog import askopenfilename
import random
from matriz import matriz



base_url = "http://3.88.228.81:8080/"
def entrada():
    f = open(askopenfilename(), "r")
    return f.read()
def carga_masiva(entrada):
    res = requests.post(f'{base_url}/Lista/{entrada}')
    data = res.text#convertimos la respuesta en dict
    print(data)
def login(usuario, contraseña):
    res = requests.post(f'{base_url}/Login/{usuario},{contraseña}')
    data = res.text#convertimos la respuesta en dict
    print(data)
def editN(nombre):
    res = requests.post(f'{base_url}/editN/{nombre}')
    data = res.text#convertimos la respuesta en dict
    print(data)
def editP(nombre):
    res = requests.post(f'{base_url}/editP/{nombre}')
    data = res.text#convertimos la respuesta en dict
    print(data)
def KS(nombre):#EL PARAMETRO DE ENTRADA LO DEJAMOS NADA MAS PARA CONFIRMACION
    res = requests.post(f'{base_url}/KS/{nombre}')
    data = res.text#convertimos la respuesta en dict
    print(data)

def dispara(mo,mh,x,y):
    if(mo.eliminar(x,y)):
        mh.ingresar(x,y,"golpe")
        print("LE DISTE------------------------")
    else:
        mh.ingresar(x,y,"missed")
        print("FALLASTE------------------------")
    
   


if __name__ == '__main__':
    #carga_masiva(entrada())
    #login("betebetoven","jaja")
    #editN("beto")
    #editP("mama")
   # KS("yes")
    #login("colosho","colosho")
    m = matriz(24)#DE LA COMPU
    m.para_compu()

    if m.llenadomanual(23,23,"pt"):
        print("SI LO PUDO INGRESAR MANUAL_______________________________________________")
    else:
        print("NO LO PUDO INGRESAR MANUAL_______________________________________________")
    m2 = matriz(24)#MIS DISPAROS
    m3 = matriz(24)#MI TABLERO
    m4 = matriz(24)#DISPAROS DE LA COMPU

    
    dispara(m,m2,0,2)
    dispara(m,m2,1,2)
    dispara(m,m2,2,2)
    dispara(m,m2,3,2)
    dispara(m,m2,4,2)
    dispara(m,m2,5,2)
    dispara(m,m2,6,2)
    dispara(m,m2,7,2)
    dispara(m,m2,8,2)
    dispara(m,m2,9,2)
    dispara(m,m2,10,2)
    
    m.grapvzix("compu")
    m2.grapvzix("disp_jug")
    m3.grapvzix("mitablero")
    m4.grapvzix("disp_compu")
    
    for n in m2.ocupados:
        print(str(n))
   
    




    #dispara(m,disparos,4,2)
  
   




  
   
    
    


    
   