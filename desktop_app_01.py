# se importa la librería tkinter con todas sus funciones
from tkinter import *
from tkinter import messagebox

#------------------------
# funciones de la app
#------------------------

def calcular():
    messagebox.showinfo("Minicalculadora 1.0", "Hizo click en el boton Calcular")
    s = int(a.get())+int(b.get())
    r = int(a.get())-int(b.get())
    m = int(a.get())*int(b.get())
    d = int(a.get())/int(b.get())
    mod = int(a.get())%int(b.get())
    de  = int(a.get())//int(b.get())
    p  = int(a.get())**int(b.get())
    
    t_resultados.insert(INSERT, f"{a.get()} + {b.get()} = {s}\n")
    t_resultados.insert(INSERT, f"{a.get()} - {b.get()} = {r}\n")
    t_resultados.insert(INSERT, f"{a.get()} * {b.get()} = {m}\n")
    t_resultados.insert(INSERT, f"{a.get()} / {b.get()} = {d}\n")
    t_resultados.insert(INSERT, f"{a.get()} % {b.get()} = {mod}\n")
    t_resultados.insert(INSERT, f"{a.get()} // {b.get()} = {de}\n")
    t_resultados.insert(INSERT, f"{a.get()} ** {b.get()} = {p}\n")


def borrar():
    messagebox.showinfo("Minicalculadora 1.0", "Los datos serán borrados...")
    a.set("")
    b.set("")
    t_resultados.delete("1.0", "end")

def salir():
    messagebox.showinfo("Minicalculadora 1.0", "La app se cerrará")
    ventana_principal.destroy()

#------------------------
# ventana principal
#------------------------

# se declara una variable llamada ventana_principal, que adquiere las caracteristicas de un objeto Tk()
ventana_principal = Tk()

# titulo de la ventana
ventana_principal.title("Minicalculadora 1.0")

# tamaño de la ventana
ventana_principal.geometry("500x500")

# deshabilitar boton de maximizar
ventana_principal.resizable(0,0)

# color de fondo de la ventana
ventana_principal.config(bg="gray")

#--------------------------
# variables de control
#--------------------------
a = StringVar()
b = StringVar()

#--------------------------
# frame entrada datos
#--------------------------

frame_entrada = Frame(ventana_principal)
frame_entrada.config(bg="white", width=480, height=180)
frame_entrada.place(x=10,y=10)

# logo de la app
logo = PhotoImage(file="img/logo_uis.png")
lb_logo = Label(frame_entrada, image=logo, bg="white")
lb_logo.place(x=11,y=40)

# etiqueta para el titulo
lb_titulo = Label(frame_entrada, text="Minicalculadora 1.0")
lb_titulo.config(bg="white", fg="green", font=("Helvetica", 20))
lb_titulo.place(x=240,y=10)

# etiqueta para el primer número
lb_a = Label(frame_entrada, text="a : ")
lb_a.config(bg="white", fg="green", font=("Helvetica", 20))
lb_a.place(x=250, y=60)

# caja de texto (Entry) para el primer número
entry_a = Entry(frame_entrada, textvariable=a)
entry_a.config(bg="white", fg="green", font=("Courier", 20))
entry_a.focus_set()
entry_a.place(x=290, y=60, width=100, height=30)

# etiqueta para el segundo número
lb_b = Label(frame_entrada, text="b : ")
lb_b.config(bg="white", fg="green", font=("Helvetica", 20))
lb_b.place(x=250, y=100)

# caja de texto (Entry) para el segundo número
entry_b = Entry(frame_entrada, textvariable=b)
entry_b.config(bg="white", fg="green", font=("Courier", 20))
entry_b.place(x=290, y=100, width=100, height=30)

#--------------------------
# frame operaciones
#--------------------------

frame_operaciones = Frame(ventana_principal)
frame_operaciones.config(bg="white", width=480, height=100)
frame_operaciones.place(x=10,y=200)

# boton calcular
bt_calcular = Button(frame_operaciones, text="Calcular", command=calcular)
bt_calcular.place(x=45,y=35, width=100, height=30)

# boton borrar
bt_borrar = Button(frame_operaciones, text="Borrar", command=borrar)
bt_borrar.place(x=190,y=35, width=100, height=30)

# boton salir
bt_salir = Button(frame_operaciones, text="Salir",command=salir)
bt_salir.place(x=335,y=35, width=100, height=30)

#--------------------------
# frame resultados
#--------------------------

frame_resultados = Frame(ventana_principal)
frame_resultados.config(bg="white", width=480, height=180)
frame_resultados.place(x=10,y=310)

# area de texto para resultados
t_resultados = Text(frame_resultados)
t_resultados.config(bg="black", fg="green", font=("Courier", 15))
t_resultados.place(x=10,y=10,width=460, height=160)

# run
# se ejecuta la función (metodo) mainloop() de la clase Tk() a través de la instancia ventana_principal.  Este método despliega una ventana simple en pantalla y queda a la espera de lo que el usuario haga.  Cada acción del usuario se conoce como evento.  El mainloop() es unn bucle infinito.
ventana_principal.mainloop()
