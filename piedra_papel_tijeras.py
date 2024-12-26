from tkinter import *
from tkinter import messagebox
from tkinter.font import Font
from random import randint as r

victorias = 0
derrotas = 0

def nrandom():
 nr = r(0, 2)
 if nr == 0:
  pc = "Piedra"
 elif nr == 1:
  pc = "Papel"
 else:
  pc = 'Tijera'
 return pc

def play(p):
 global victorias, derrotas
 pc = nrandom()
 def px(p):
  if pc == 'Papel' and p == 'Piedra':
   return 'Perdistes'
  elif pc == 'Tijera' and p == 'Papel':
   return 'Perdistes'
  elif pc == 'Piedra' and p == 'Tijera':
   return 'Perdistes'
  elif pc == p:
   return 'Empate'
  else:
   return 'Ganastes'
 vs = f"{p} VS {pc}"
 resultado = px(p)
 if resultado == 'Ganastes':
  victorias += 1
 elif resultado == 'Perdistes':
  derrotas += 1
 resultado_label.config(text=f"{vs}\n{resultado}")
 estadisticas.config(text=f"Victorias: {victorias} | Derrotas: {derrotas}")
 if victorias == 5:
  messagebox.showinfo("Fin del juego", "¡Eres el ganador!")
  reset_game()
 elif derrotas == 5:
  messagebox.showinfo("Fin del juego", "¡Eres el perdedor!")
  reset_game()
 resultado_label.after(4000, lambda: resultado_label.config(text=""))

def reset_game():
 global victorias, derrotas
 victorias = 0
 derrotas = 0
 estadisticas.config(text=f"Victorias: {victorias} | Derrotas: {derrotas}")
 resultado_label.config(text="")

interfaz = Tk()
interfaz.geometry("400x300")
interfaz.title("Piedra, Papel O Tijeras")
interfaz.config(bg="#0076f5")
font = Font(family="Calibri", size=17)
ngame = Label(interfaz, text="PIEDRA, PAPEL O TIJERAS", font=font, bg="#0076f5", fg="black")
ngame.pack(pady=20)

button_frame = Frame(interfaz, bg="#008fff")
button_frame.pack()

button_piedra = Button(button_frame, text="PIEDRA", command=lambda: play("Piedra"), width=10, height=2, bg="white")
button_papel = Button(button_frame, text="PAPEL", command=lambda: play("Papel"), width=10, height=2, bg="white")
button_tijeras = Button(button_frame, text="TIJERA", command=lambda: play("Tijera"), width=10, height=2, bg="white")

button_piedra.grid(row=0, column=1, padx=10, pady=10)
button_papel.grid(row=0, column=2, padx=10, pady=10)
button_tijeras.grid(row=0, column=3, padx=10, pady=10)

resultado_label = Label(interfaz, text="", font=font, bg="#0076f5", fg="#fff")
resultado_label.pack(pady=20)

estadisticas = Label(interfaz, text="Victorias: 0 | Derrotas: 0", font=font, bg="#0076f5", fg="black")
estadisticas.pack(pady=20)

interfaz.mainloop()
