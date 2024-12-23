from tkinter import *
from tkinter import messagebox
from tkinter.font import Font

### CREDENTIALS ###
usuario = 'PGX'
clave = '0000'

def comprobar():
 user = entrada1.get()
 password = entrada2.get()
 range_chars = len(user) + len(password)
 if range_chars != 0:
  if user == usuario and password == clave:
   messagebox.showinfo("", "CREDENCIALES CORRECTAS")
  else:
   messagebox.showwarning("", "USUARIO O CLAVE INVALIDO")
 else:
  print("CAMPO VACIO")

ventana = Tk()
ventana.geometry("400x200")
ventana.title("CONTROL DE ACCESO")
ventana.config(bg="#4fc3ff")
btn_font = Font(family="Arial", size=15)
user = Label(text="USUARIO", bg="#4fc3ff", font=btn_font)
user.grid(row=1, column=0, pady=5)
entrada1 = Entry(ventana, font=btn_font, justify='center')
entrada1.grid(row=1, column=1)

password = Label(text="CLAVE", bg="#4fc3ff", font=btn_font)
password.grid(row=2, column=0)
entrada2 = Entry(ventana, font=btn_font, justify='center')
entrada2.grid(row=2, column=1)
entrada2.config(show="*")

x = Label(text="", bg="#4fc3ff")
x.grid(row=3, column=0)


button = Button(ventana, text="INGRESAR", command=comprobar, bg="#008fff", fg="white", font=btn_font)
button.grid(row=4, column=1)
ventana.mainloop()
