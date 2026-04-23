import flet as ft
import requests

#conexion a la base de datos Airtable
#token - idBasedatos
tokenAirtable=""
idBaseDatos=""
nombreTabla=""


def main(page: ft.Page):

    listaEstudiante=ft.ListView(
        padding=20,
        spacing=10,
        expand=True
    )

    #CARGADO DE DATOS AL LISTVIEW
    def cargarDatos():
        url=f"https://api.airtable.com/v0/{idBaseDatos}/{nombreTabla}"
        headers={
            "Authorization":f"Bearer {tokenAirtable}"
        }
        respuesta=requests.get(url,headers=headers)

        if respuesta.status_code==200:
            data=respuesta.json()
            #Limpiar el componente
            listaEstudiante.controls.clear()

            for registro in data["records"]:
                campos=registro["fields"]
                nombre=campos.get("Nombre","Sin Nombre")
                carrera=campos.get("Carrera","Sin Carrera")
                correo=campos.get("Correo","Sin Correo")
                celular=campos.get("Celular","Sin Celular")
                foto=campos.get("Foto","Sin Foto")

                tarjeta=ft.Card(
                    content=ft.Container(
                        content=ft.Column(
                                    [
                                    ft.Image(src=foto,width=100,height=100),
                                    ft.Text(nombre),
                                    ft.Text(carrera) ,
                                    ft.Text(celular),
                                    ]
                        )

                                   
                                                
                                
                    ),
                    
                    
                )
                listaEstudiante.controls.append(tarjeta)
        else:
            print("Error....")
    
    cargarDatos()
    page.add(
        listaEstudiante 
    )


ft.run(main)
