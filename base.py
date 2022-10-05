




from tkinter import *
import tkinter
from tkinter import messagebox
from tkinter.ttk import Combobox
import requests##pip3 install request
import json
from tkinter.filedialog import askopenfilename
import random
import os
from matriz import matriz


from PIL import ImageTk,Image

tablero_jugador_global = None
tablero_computadora_global = None
tablero_disparos_computadora_global = None
tablero_disparos_jugador_global = None
direccion = "one"
base_url = "http://3.88.228.81:8080/"
def entrada():
    global direccion
    direccion = askopenfilename()
    f = open(direccion, "r")
    return f.read()
def carga_masiva(entrada):
    res = requests.post(f'{base_url}/Lista/{entrada}')
    data = res.text#convertimos la respuesta en dict
    
    f = open(f'arbolb.dot', "w")
    f.write(data)
    f.close()
    os.system(f'dot -Tpng arbolb.dot -o arbolb.png')


    ver5()
    print(data)
def login(usuario, contraseña):
    res = requests.post(f'{base_url}/Login/{usuario},{contraseña}')
    data = res.text#convertimos la respuesta en dict
    messagebox.showinfo("LOGIN",data)
    print(data)
def editN(nombre):
    res = requests.post(f'{base_url}/editN/{nombre}')
    data = res.text#convertimos la respuesta en dict
    messagebox.showinfo("CAMBIO DE NOMBRE",data)
    print(data)
def editP(nombre):
    res = requests.post(f'{base_url}/editP/{nombre}')
    data = res.text#convertimos la respuesta en dict
    messagebox.showinfo("CAMBIO DE CONTRASEÑA",data)
    print(data)
def KS(nombre):#EL PARAMETRO DE ENTRADA LO DEJAMOS NADA MAS PARA CONFIRMACION
    res = requests.post(f'{base_url}/KS/{nombre}')
    data = res.text#convertimos la respuesta en dict
    messagebox.showinfo("ELIMINACION",data)
    print(data)

root = Tk()
root.title('Fase 2')
def ver():#VER SU TABLERO Y MIS DISPAROS
    global compu
    global disp_jug
    global uwu
    top = Toplevel()
    f = Label(top,text="TABLERO COMPUTADORA").pack(side = LEFT, fill = Y)
    compu = ImageTk.PhotoImage(Image.open('compu.png').resize((400,400)))
    my_label = Label(top, image=compu).pack(side = LEFT, fill = Y)
    f = Label(top,text="TABLERO disparos").pack(side = LEFT, fill = Y)
    disp_jug = ImageTk.PhotoImage(Image.open('disp_jug.png').resize((400,400)))
    my_label2 = Label(top, image=disp_jug).pack(side = LEFT, fill = Y)
def ver2():#VER MI TABLERO Y MIS DISPAROS
    global compu
    global disp_jug
    global uwu
    top = Toplevel()
    f = Label(top,text="TABLERO JUGADOR").pack(side = LEFT, fill = Y)
    compu = ImageTk.PhotoImage(Image.open('mitablero.png').resize((400,400)))
    my_label = Label(top, image=compu).pack(side = LEFT, fill = Y)
    f = Label(top,text="TABLERO disparos").pack(side = LEFT, fill = Y)
    disp_jug = ImageTk.PhotoImage(Image.open('disp_jug.png').resize((400,400)))
    my_label2 = Label(top, image=disp_jug).pack(side = LEFT, fill = Y)
def ver3():#VER SU TABLERO Y SUS DISPAROS
    global compu
    global disp_jug
    global uwu
    top = Toplevel()
    f = Label(top,text="TABLERO COMPUTADORA").pack(side = LEFT, fill = Y)
    compu = ImageTk.PhotoImage(Image.open('compu.png').resize((400,400)))
    my_label = Label(top, image=compu).pack(side = LEFT, fill = Y)
    f = Label(top,text="TABLERO disparos").pack(side = LEFT, fill = Y)
    disp_jug = ImageTk.PhotoImage(Image.open('disp_compu.png').resize((400,400)))
    my_label2 = Label(top, image=disp_jug).pack(side = LEFT, fill = Y)
def ver4():#VER MI TABLERO Y SUS DISPAROS
    global compu
    global disp_jug
    global uwu
    top = Toplevel()
    f = Label(top,text="TABLERO JUGADOR").pack(side = LEFT, fill = Y)
    compu = ImageTk.PhotoImage(Image.open('mitablero.png').resize((400,400)))
    my_label = Label(top, image=compu).pack(side = LEFT, fill = Y)
    f = Label(top,text="TABLERO disparos").pack(side = LEFT, fill = Y)
    disp_jug = ImageTk.PhotoImage(Image.open('disp_compu.png').resize((400,400)))
    my_label2 = Label(top, image=disp_jug).pack(side = LEFT, fill = Y)
def ver5():#VER MI TABLERO Y SUS DISPAROS
    global compu
    top = Toplevel()
    f = Label(top,text="ARBOL B").pack()
    compu = ImageTk.PhotoImage(Image.open('arbolb.png').resize((1200,700)))
    my_label = Label(top, image=compu).pack()
#ACA VA VER MI ABLERO Y SUS DISPAROS, ES LO MISMOS SOLO CAMBIA EL NOMBRE DE LA FOTO
def logo():
    global username
    global password
    global us
    global pas
    global inge
    top = Toplevel()
    f = Label(top,text="username").pack()
    username = StringVar(top)
    password = StringVar(top)
    us = Entry(top,textvariable=username).pack()
    d = Label(top,text="password").pack()
    pas = Entry(top,textvariable=password).pack()
    def ingr():
        login(username.get(),password.get())
        print(f'usuario:{username.get()} y contraseña: {password.get()}')
        jugar()
    inge = Button(top,text="INGRESAR",command=ingr).pack()

def jugar():
    global dimension
    global dx
    global dy
    global ddx
    global ddy
    global barco
    global d
    global pas
    global inge
    global ingee
    global ingeee
    global cbb
    global selected_month
    global edit
    global vt
    top = Toplevel()
    dimension = StringVar(top)
    ddx = StringVar(top)
    ddy = StringVar(top)#convertir los strings a ints
    barco = StringVar(top)
    selected_month = StringVar(top)
    dime = Label(top,text="DIMENSION DE TABLERO:").pack()
    d = Entry(top,textvariable=dimension).pack()
    dl = Label(top,text="x:").pack()
    dx = Entry(top,textvariable=ddx).pack()
    dll = Label(top,text="y:").pack( )
    dy = Entry(top,textvariable=ddy).pack()
    dlll = Label(top,text="barco:").pack( )
    cbb = Combobox(top,textvariable=selected_month)
    cbb['values']= ['pt','sub','dt','b']
    cbb['state']='readonly'
    cbb.pack()
    def ingr():
        print(f'dimension:{dimension.get()} ')
        global tablero_computadora_global
        global tablero_disparos_computadora_global
        global tablero_jugador_global
        global tablero_disparos_jugador_global
        tablero_computadora_global = matriz(int(dimension.get()))
        tablero_computadora_global.para_compu()
        tablero_disparos_computadora_global = matriz(int(dimension.get()))
        tablero_jugador_global = matriz(int(dimension.get()))
        tablero_disparos_jugador_global = matriz(int(dimension.get()))

    def ingr2():
        global tablero_computadora_global
        global tablero_disparos_computadora_global
        global tablero_jugador_global
        global tablero_disparos_jugador_global
        if tablero_jugador_global.llenadomanual(int(ddx.get()),int(ddy.get()),selected_month.get()):
            messagebox.showinfo("INGRESO","INGRESAD CORRECTAMENTE")
            print("SI LO PUDO INGRESAR MANUAL_______________________________________________")
        else:
            messagebox.showerror("ERROR","CASILLA OCUPADA O NO HAY ESPACIOS CERCA")
            print("NO LO PUDO INGRESAR MANUAL_______________________________________________")
        print(f' coordenadas: {ddx.get()},{ddy.get()}  barco:{selected_month.get()}')
    def ingr3():
        print(f'VAMO A JUGA')
    inge = Button(top,text="CREAR TABLERO",command=ingr).pack()
    ingee = Button(top,text="AGREGAR BARCO",command=ingr2).pack()
    ingeee = Button(top,text="JUGAR",command=jugar_si).pack()
    edit = Button(top,text="editar informacion",command=editar_informacion).pack()
    vt = Button(top,text="VER TIENDA",command=ver6).pack()

def dispara(mo,mh,x,y):
    if(mo.eliminar(x,y)):
        mh.ingresar(x,y,"golpe")
        messagebox.showinfo("DISPARO","LE DISTE")
        print("LE DISTE------------------------")
    else:
        mh.ingresar(x,y,"missed")
        messagebox.showerror("DISPARO","FALLASTE")
        print("FALLASTE------------------------")
    


def jugar_si():
    global tablero_computadora_global
    global tablero_disparos_computadora_global
    global tablero_jugador_global
    global tablero_disparos_jugador_global
    global dx
    global dy
    global ddx
    global ddy
    global pas
    global inge
    global ingee
    global ingeee
    global cbb
    global ing
    global fire
    global ataque_de_racimo
    tablero_computadora_global.grapvzix("compu")
    tablero_disparos_jugador_global.grapvzix("disp_jug")
    tablero_jugador_global.grapvzix("mitablero")
    tablero_disparos_computadora_global.grapvzix("disp_compu")
    top = Toplevel()
    ddx = StringVar(top)
    ddy = StringVar(top)#convertir los strings a ints
    dime = Label(top,text="DISPARA:").pack()
    dl = Label(top,text="x:").pack()
    dx = Entry(top,textvariable=ddx).pack()
    dll = Label(top,text="y:").pack( )
    dy = Entry(top,textvariable=ddy).pack()
    def ingr():
        #dispara usuario
        dispara(tablero_computadora_global,tablero_disparos_jugador_global,int(ddx.get()),int(ddy.get()))
        #dispara a computadora
        dispara(tablero_jugador_global,tablero_disparos_computadora_global,random.randint(0,9),random.randint(0,9))
        tablero_computadora_global.grapvzix("compu")
        tablero_disparos_jugador_global.grapvzix("disp_jug")
        tablero_jugador_global.grapvzix("mitablero")
        tablero_disparos_computadora_global.grapvzix("disp_compu")
        print(f' DISPARO: {ddx.get()},{ddy.get()}')
    def ingr3():
        dispara(tablero_computadora_global,tablero_disparos_jugador_global,0,2)
        dispara(tablero_computadora_global,tablero_disparos_jugador_global,1,2)
        dispara(tablero_computadora_global,tablero_disparos_jugador_global,2,2)
        dispara(tablero_computadora_global,tablero_disparos_jugador_global,3,2)
        dispara(tablero_computadora_global,tablero_disparos_jugador_global,4,2)
        dispara(tablero_computadora_global,tablero_disparos_jugador_global,5,2)
        dispara(tablero_computadora_global,tablero_disparos_jugador_global,6,2)
        dispara(tablero_computadora_global,tablero_disparos_jugador_global,7,2)
        dispara(tablero_computadora_global,tablero_disparos_jugador_global,8,2)
        dispara(tablero_computadora_global,tablero_disparos_jugador_global,9,2)
        tablero_computadora_global.grapvzix("compu")
        tablero_disparos_jugador_global.grapvzix("disp_jug")
        tablero_jugador_global.grapvzix("mitablero")
        tablero_disparos_computadora_global.grapvzix("disp_compu")
        print(f'ataque de racismo')
    fire = Button(top,text="DISPARA",command=ingr).pack()
    ataque_de_racimo = Button(top,text="ATAQUE DE RACIMO",command=ingr3).pack()
    ingee = Button(top,text="ver __SU__ tablero y MIS disparos",command=ver).pack()
    ingeee = Button(top,text="ver __MI__ tablero y MIS disparos",command=ver2).pack()
    inge = Button(top,text="ver __SU__ tablero y SUS disparos",command=ver3).pack()
    ing = Button(top,text="ver __MI__ tablero y SUS disparos",command=ver4).pack()

def editar_informacion():
    global dimension
    global dx
    global ddx
    global d
    global inge
    global ingee
    global ingeee
    top = Toplevel()
    dimension = StringVar(top)
    ddx = StringVar(top)
    ddy = StringVar(top)#convertir los strings a ints
    barco = StringVar(top)
    selected_month = StringVar(top)
    dime = Label(top,text="cambiar nombre:").pack()
    d = Entry(top,textvariable=dimension).pack()
    dl = Label(top,text="cambiar contraseña:").pack()
    dx = Entry(top,textvariable=ddx).pack()
    def ingr():
        editN(dimension.get())
        print(f'cambio de nomre:{dimension.get()} ')
    def ingr2():
        editP(ddx.get())
        print(f' cambio de contraseña: {ddx.get()}')
    def ingr3():
        KS("si")
        print(f'elimino cuenta, regresar a login')
    inge = Button(top,text="editar nombre",command=ingr).pack()
    ingee = Button(top,text="editar contraseña",command=ingr2).pack()
    ingeee = Button(top,text="eliminar cuenta",command=ingr3).pack()
    
def cm():
    carga_masiva(entrada())



def ver6():#VER MI TABLERO Y SUS DISPAROS
    top = Toplevel()
    f = Label(top,text="TIENDA").pack()
    global direccion
    f = open(direccion, "r")
    stienda =  json.loads(f.read())["articulos"]
    for c in stienda :
        print(c["id"])
        f = Label(top,text=c["id"]).pack()
        print(c["categoria"])
        f = Label(top,text=c["categoria"]).pack()
        print(c["precio"])
        f = Label(top,text=c["precio"]).pack()
        print(c["nombre"])
        f = Label(top,text=c["nombre"]).pack()
        mnb = Button(top,text="COMPRAR").pack()
    sb = Scrollbar(top)
    sb.config(command = top.yview )
    sb.pack(side = LEFT, fill = RIGHT)


   
logi = Button(root,text="login",command=logo).pack()
cmm = Button(root,text="CARGA MASIVA",command=cm).pack()

#btn = Button(root,text="ver su tablero y mis disparos",command=ver).pack()






mainloop()