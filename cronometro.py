from tkinter import *
seg = 0
iniciado = None

def iniciar():
 global seg, iniciado
 seg += 1
 tiempo = f"{seg // 60:02}:{seg % 60:02}"
 etiqueta.config(text=tiempo)
 iniciado = ventana.after(1000, iniciar)

def detener():
 global iniciado
 if iniciado is not None:
  ventana.after_cancel(iniciado)
ventana = Tk()
ventana.config(bg="black")
ventana.geometry("400x300")
ventana.title("CRONOMETRO")
frame = Frame(ventana)
frame.pack(expand=True)

etiqueta = Label(frame, text="00:00", font=("helvetica", "48"))
etiqueta.pack()

boton_iniciar = Button(frame, text="INICIAR", command=iniciar, font=("helvetica", "17"))
boton_iniciar.pack(side="left")
boton_detener = Button(frame, text="DETENER", command=detener, font=("helvetica", "17"))
boton_detener.pack(side="left")
ventana.mainloop()