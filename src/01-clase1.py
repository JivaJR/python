import random
import tkinter as tk
from tkinter import ttk

# Ejecucion del juego
def jugar(opcion_usuario):
    global victorias, derrotas,empates
    opciones = ["piedra", "papel", "tijeras"]
    opcion_pc = random.choice(opciones)
    elecciones.config(text=f"Elegiste: {opcion_usuario}\nLa computadora eligió: {opcion_pc}")

    if opcion_usuario == opcion_pc:
        empates += 1
        resultado.config(text="¡Empate! :/")
    elif (opcion_usuario == "piedra" and opcion_pc == "tijeras") or \
        (opcion_usuario == "papel" and opcion_pc == "piedra") or \
        (opcion_usuario == "tijeras" and opcion_pc == "papel"):
        victorias += 1
        resultado.config(text="¡Ganaste! :)")
    else:
        resultado.config(text="¡Perdiste! :(")
        derrotas += 1
    historial.config(text=f'Maquina:  {derrotas} - Humano:  {victorias} - Empates:  {empates}')

# Interfaz gráfica
root = tk.Tk()
root.title("Piedra, Papel o Tijeras")
root.geometry("600x350")
root.tk_setPalette(background='#ECECEC', foreground='#000000', activeBackground='#4CAF50', activeForeground='#FFFFFF', highlightBackground='#4CAF50', highlightColor='#000000')

# Estilos
root_style = ttk.Style()
root_style.configure('TFrame', background='#ECECEC')
root_style.configure('TButton', font=('Arial', 12, 'bold'), background='#0059FF', foreground='black')

#Frames
options_frame = ttk.Frame(root, style='TFrame')
options_frame.pack(pady=10)
info_frame = ttk.Frame(root, style='TFrame')
info_frame.pack(pady=10)

resultados_frame = tk.Frame(info_frame, bd=5)
resultados_frame.pack()
history_frame = tk.Frame(info_frame, bd=5)
history_frame.pack()

#Seteo de historial
victorias = 0
derrotas = 0
empates = 0

# Botones de las opciones
boton_piedra = ttk.Button(options_frame, text="Piedra", command=lambda: jugar("piedra"), style='TButton')
boton_piedra.grid(row=0, column=0, padx=10)

boton_papel = ttk.Button(options_frame, text="Papel", command=lambda: jugar("papel"), style='TButton')
boton_papel.grid(row=0, column=1, padx=10)

boton_tijeras = ttk.Button(options_frame, text="Tijeras", command=lambda: jugar("tijeras"), style='TButton')
boton_tijeras.grid(row=0, column=2, padx=10)

# Resultado del juego
resultado = tk.Label(resultados_frame, text="Aun no hay resultados")
resultado.pack(side=tk.BOTTOM, pady=20)
elecciones = tk.Label(resultados_frame,text="Haz tu primera jugada")
elecciones.pack(side=tk.BOTTOM, pady=20)
historial = ttk.Label(history_frame,text=f'Maquina:  {derrotas} - Humano:  {victorias} - Empates:  {empates}',style='TButton')
historial.pack(side=tk.BOTTOM, pady=20)

# Bucle
root.mainloop()
