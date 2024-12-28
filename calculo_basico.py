from tkinter import *

def operacion(op, en1, en2):
 rangex = len(en1+en2)
 if rangex != 0:
  n1 = float(en1)
  n2 = float(en2)
  if op == '+':
   x = n1 + n2
  elif op == '-':
   x = n1 - n2
  elif op == '*':
   x = n1 * n2
  else:
   x = n1 / n2
  resultado.config(text=f"RESULTADO = {x}")
 else:
  resultado.config(text="Campos Vacios...")
 resultado.after(4000, lambda: resultado.config(text=""))

estilo = ("Arial", "12", "bold")

ventana = Tk()
ventana.title("OPERACIOS MATEMATICAS")
ventana.geometry("400x320")
ventana.config(bg="#0075c9")

entry1 = Entry(ventana, justify="center", font=("helvetica", "15"), width="15")
entry1.pack(pady=(15,4))
entry2 = Entry(ventana, justify="center", font=("helvetica", "15"), width="15")
entry2.pack(pady=(0,8))
sumar = Button(text="Sumar", bg="#7fbfd5", width=15, font=estilo, command=lambda:operacion("+", entry1.get(), entry2.get()))
sumar.pack()
restar = Button(text="Restar", width=15, bg="#7fbfd5", font=estilo, command=lambda:operacion("-", entry1.get(), entry2.get()))
restar.pack(pady=5)
multiplicar = Button(text="Multiplicar", bg="#7fbfd5", width=15, font=estilo, command=lambda:operacion("*", entry1.get(), entry2.get()))
multiplicar.pack(pady=5)
dividir = Button(text="Dividir", bg="#7fbfd5", width=15, font=estilo, command=lambda:operacion("/", entry1.get(), entry2.get()))
dividir.pack(pady=5)

resultado = Label(text="", bg="#0075c9", fg="#fff", font=estilo)
resultado.pack(pady=10)
ventana.mainloop()