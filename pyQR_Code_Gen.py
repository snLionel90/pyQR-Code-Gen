from tkinter import *
from tkinter import messagebox
import pyqrcode
import os
import webbrowser

win = Tk()
win.title ("Py QR Code generator sn.Lionel90")
#win.configure(background ="navajo white")
win.iconbitmap("./icons/qr_icon.png")
win.resizable=FALSE

__author__="sn.Lionel90 / Lionel Sanchez"
print(__author__)

url_capture= StringVar()

#Funciones / Functions

def generarQR(): #genera de forma aleatoria el codigo qr
    if len (url_capture.get()) !=0: #obtiene la url,
        global myqr #variable global de qr
        myqr = pyqrcode.create(url_capture.get()) #obtiene el qr desde la url
        qrImagen = myqr.xbm(scale=6) #muestra el codigo qr generado en una imagen, la guarda en memoria
        global imagen 
        imagen = BitmapImage(data=qrImagen) #extrae de la memoria la imagen y kla muestra en pantalla

    else:
        messagebox.showinfo("Error", "Por favor, escriba una URL o un nombre valida")
        #muestra un mensaje de error
    try:
        mostrarCodigoQR() #llamada ala funcion de mostar el QL
    except:
        pass #que circule

def mostrarCodigoQR():
    global imagen #utilizamos la variable de la funcion anterior
    QR_Label.config(image= imagen)
    subLbl.config(text="show QR For: " +url_capture.get()) 

def salir():
    exit(0)

def limpiar ():
    etEntrada.delete(0,len(url_capture.get()))

#fucncion de enlace externo abre un navegador web
def openWroser():
    global webbrowser
    webbrowser.open("https://github.com/snLionel90/", new=2, autoraise=True)

#componentes de la pantalla
lb1 = Label(win, text="Escribe la URL", font=("Arial", 15))
lb1.grid(row = 0, column=0, sticky = N +S +E +W) #posicion a la esquina superior izda

#edit text para insertar la URL
etEntrada = Entry(win, textvariable = url_capture, font = ("Calibri", 15))
etEntrada.grid(row = 0, column = 1,  sticky = N +S +E +W) #posicion central

#boton de generar QR
QR_btn = Button(win, text="generar Codigo QR", font= ("Arial", 15),bg="palegreen", fg="black", width=15, command = generarQR)
QR_btn.grid(row=0, column=2, sticky = N +S +E +W) #poscion esquina superior derecha

#mostrando el botn de escape o salida de programa
quit_btn = Button(win, text=" Salir", font=("Arial", 15),bg="gray50", fg="yellow", width=10, command = salir)
quit_btn.grid (row = 1, column=0) #segunda fila a la izquierda 

#espacio reservado para el copyright
copyright=Label(win, text="Sn.Lionel90 (c) 2020", font=("Arial", 13))
copyright.grid(row=2, column=0) #segunda fila al centro

#boton limpia
btn_limpia=Button(win, text=" Limpiar URL", font=("Arial", 15),bg="gray80", fg="yellow", width=10, command = limpiar)
btn_limpia.grid(row=1, column=1)

# lanzador evento visitar web
btn_web= Button(win, text=" visitar Web", font=("Arial", 15),bg="gray30", fg="navajo white", width=10, command=openWroser)
btn_web.grid(row=1, column=2) #segunda fila a la derecha

#imagen cdeQR
QR_Label=Label(win, text=" ")
QR_Label.grid(row=2, column=1, sticky = N +S +E +W) #posicion centarl

#conteo total de filas y columnas
totalRows = 3
totalColumns = 3

for row in range(totalRows +1):
    win.grid_rowconfigure(row, weight=1)

for col in range(totalColumns +1):
    win.grid_columnconfigure(col,weight = 1)


win.mainloop()



