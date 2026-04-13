import flet as ft
import sqlite3

#Paso 1.. Crear o conectar a la base de datos
def basedatos():
    conexion=sqlite3.connect("usuarios.db")
    ejecucion=conexion.cursor()
    ejecucion.execute("""
        CREATE TABLE IF NOT EXISTS estudiantes(
        codEstudiente INTEGER PRIMARY KEY,
        nombre TEXT,
        carrera TEXT
        )
    """)
    conexion.commit()
    return conexion

basedatos()

def main(page: ft.Page):
    page.appbar=ft.AppBar(title=ft.Text("Base datos"))
    
    codEstudiante=ft.TextField(label="Cod Esutdiamate: ")
    nombreEstudiante=ft.TextField(label="Nombre: ")
    carreraEstudiante=ft.TextField(label="Carrera ")
        
    def insertar():
       with sqlite3.connect("usuarios.db") as conexion:
           ejecucion=conexion.cursor()
           ejecucion.execute("INSERT INTO estudiantes (codEstudiente,nombre,carrera) VALUES (?)",(codEstudiante,nombreEstudiante,carreraEstudiante))
           conexion.commit()

    botonRegistrar=ft.FilledButton("Registrar",on_click=insertar)
    page.add(
        codEstudiante,
        nombreEstudiante,
        carreraEstudiante,
        botonRegistrar
    )


ft.app(main)
