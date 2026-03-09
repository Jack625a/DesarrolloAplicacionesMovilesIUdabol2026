import flet as ft


def main(page: ft.Page):
    page.appbar=ft.AppBar(title=ft.Text("Mi aplicacion"),bgcolor=ft.Colors.BLUE_GREY_100)   
    page.bottom_appbar=ft.NavigationBar(
        destinations=[
            ft.NavigationBarDestination(label="Inicio")
        ]
    )
    
    page.add(
       ft.Button("Boton de Prueba"),
       ft.CupertinoFilledButton("Boton iOS"),
       ft.ElevatedButton("Boton Android"),
       ft.FilledButton("Boton Android")
    )
ft.app(main)
