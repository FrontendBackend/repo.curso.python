import tkinter as tk
from tkinter import messagebox

class Persona:
    def __init__(self, nombre, edad, email):
        self.nombre = nombre
        self.edad = edad
        self.email = email

def crear_persona():
    nombre = entry_nombre.get()
    edad = entry_edad.get()
    email = entry_email.get()
    return Persona(nombre, edad, email)

def agregar_persona():
    persona = crear_persona()
    lista_personas.append(persona)
    messagebox.showinfo("Éxito", "Persona agregada correctamente.")

def mostrar_personas():
    for persona in lista_personas:
        messagebox.showinfo("Información de persona",
                            f"Nombre: {persona.nombre}\nEdad: {persona.edad}\nEmail: {persona.email}")

def limpiar_campos():
    entry_nombre.delete(0, tk.END)
    entry_edad.delete(0, tk.END)
    entry_email.delete(0, tk.END)

# Crear ventana
root = tk.Tk()
root.title("CRUD de Personas")

# Campos del formulario
tk.Label(root, text="Nombre:").grid(row=0, column=0)
entry_nombre = tk.Entry(root)
entry_nombre.grid(row=0, column=1)

tk.Label(root, text="Edad:").grid(row=1, column=0)
entry_edad = tk.Entry(root)
entry_edad.grid(row=1, column=1)

tk.Label(root, text="Email:").grid(row=2, column=0)
entry_email = tk.Entry(root)
entry_email.grid(row=2, column=1)

# Botones
btn_agregar = tk.Button(root, text="Agregar Persona", command=agregar_persona)
btn_agregar.grid(row=3, column=0, columnspan=2, pady=5)

btn_mostrar = tk.Button(root, text="Mostrar Personas", command=mostrar_personas)
btn_mostrar.grid(row=4, column=0, columnspan=2, pady=5)

btn_limpiar = tk.Button(root, text="Limpiar Campos", command=limpiar_campos)
btn_limpiar.grid(row=5, column=0, columnspan=2, pady=5)

# Lista para almacenar personas
lista_personas = []

root.mainloop()
