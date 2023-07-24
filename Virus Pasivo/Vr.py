import tkinter as tk
import webbrowser
import pyautogui
from tkinter import messagebox
import time

def update_counter():
    global count
    count -= 1
    if count >= 0:
        label.config(text=f"Tiempo restante: {count}")
        root.after(1000, update_counter)
    else:
        messagebox.showinfo("Tiempo Terminado", "¡Tiempo agotado!")

def open_link():
    global link_index
    current_link = links[link_index % len(links)]
    link_index += 1

    # Abrir el enlace en una nueva ventana
    webbrowser.open(current_link, new=2)  # Reemplaza la URL con el enlace que desees abrir

def center_mouse_repeatedly():
    center_mouse()
    root.after(3000, center_mouse_repeatedly)  # Programar el próximo centrado después de 6 o 3 segundos

def center_mouse():
    x, y = pyautogui.size()
    pyautogui.moveTo(x // 2, y // 2)

def open_new_window_repeatedly():
    open_link()
    root.after(3000, open_new_window_repeatedly)  # Programar la próxima apertura después de 3 segundos

def close_window():
    if messagebox.askokcancel("Salir", "¿Estás seguro que deseas salir?"):
        root.destroy()

# Configuración inicial
count = 60
link_index = 0
links = [
    "https://www.ejemplo.com",
    "https://www.otro-ejemplo.com",
    "https://www.mas-ejemplos.com"
]

# Crear ventana principal
root = tk.Tk()
root.title("Contador Regresivo")

# Establecer las dimensiones de la ventana
window_width = 500
window_height = 500
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_pos = (screen_width // 2) - (window_width // 2)
y_pos = (screen_height // 2) - (window_height // 2)
root.geometry(f"{window_width}x{window_height}+{x_pos}+{y_pos}")

# Etiqueta para mostrar el contador con una fuente más grande (tamaño 24)
font_style = ("Helvetica", 24)
label = tk.Label(root, text=f"Tiempo restante: {count}", font=font_style)
label.pack(pady=20)

# Botón de "Reiniciar contador y abrir enlace" con fuente más grande (tamaño 16)
button_font = ("Helvetica", 16)
restart_button = tk.Button(root, text="Reiniciar Contador", font=button_font, command=open_link)
restart_button.pack(pady=15)

# Botón de "Salir" con fuente más grande (tamaño 16)
exit_button = tk.Button(root, text="Salir", font=button_font, command=close_window)
exit_button.pack(pady=15)

# Llamar a la función para actualizar el contador
update_counter()

# Llamar a la función para centrar el mouse cada 6 segundos
center_mouse_repeatedly()

# Llamar a la función para abrir una nueva ventana cada 3 segundos
root.after(3000, open_new_window_repeatedly)

# Iniciar el bucle principal de la aplicación
root.mainloop()
