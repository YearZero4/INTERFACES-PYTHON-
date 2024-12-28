from PIL import Image, ImageTk
import tkinter as tk
import requests, threading, time

def comprobar_conexion():
 url = 'https://www.google.com/'
 while True:
  try:
   st = requests.get(url, timeout=5)
   estado = 'CONEXION ESTABLE'
  except:
   estado = 'SIN CONEXION'
  actualizar_status(estado)
  time.sleep(300)

def actualizar_status(estado):
 def update_gui():
  st0.config(text=estado)
  if estado == "CONEXION ESTABLE":
   st0.config(bg="black", fg="white")
   mostrar_imagen('online0.png')
  else:
   st0.config(bg="black", fg="white")
   mostrar_imagen('offline0.png')
 interfaz.after(0, update_gui) 

def mostrar_imagen(ruta_imagen):
 img = Image.open(ruta_imagen)
 img = img.resize((170, 170), Image.LANCZOS)
 img_tk = ImageTk.PhotoImage(img)
 if hasattr(mostrar_imagen, "imagen_actual"):
  mostrar_imagen.imagen_actual.destroy()
 mostrar_imagen.imagen_actual = tk.Label(interfaz, image=img_tk)
 mostrar_imagen.imagen_actual.image = img_tk
 mostrar_imagen.imagen_actual.pack(pady=20)

interfaz = tk.Tk()
interfaz.title("STATUS DE CONEXION")
interfaz.geometry("300x300")
interfaz.config(bg="black")

st0 = tk.Label(text="COMPROBANDO CONEXION A INTERNET")
st0.pack(pady=20)

hilo_conexion = threading.Thread(target=comprobar_conexion, daemon=True)
hilo_conexion.start()

interfaz.mainloop()