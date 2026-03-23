import flet as ft

from pantallaInicio import vistaPantallaInicio
from pantallaBuscar import vistaPantallaBuscar
from pantallaConfiguracion import vistaPantallaConfiguracion
from pantallaFavoritos import vistaPantallaFavoritos 


def main(page: ft.Page):
    #Funcion para el enrutamiento
    def enrutamiento(e):
        inicio=barraNavegacion.selected_index
        page.views.clear()

        if inicio==0:
            page.views.append(vistaPantallaInicio(page))
        elif inicio==1:
            page.views.append(vistaPantallaBuscar(page))
        elif inicio==2:
            page.views.append(vistaPantallaFavoritos(page))
        elif inicio==3:
            page.views.append(vistaPantallaConfiguracion(page))
    

    page.appbar=ft.AppBar(
        title=ft.Text("Componentes Cuerpo"),
        leading=ft.Icon(name='MENU'),
        bgcolor=ft.Colors.PURPLE_900,
        color=ft.Colors.WHITE
    )

    barraNavegacion=ft.NavigationBar(
        destinations=[
            ft.NavigationBarDestination(icon=ft.icons.HOME,label="Inicio"),
            ft.NavigationBarDestination(icon=ft.icons.SEARCH,label="Buscar"),
            ft.NavigationBarDestination(icon=ft.icons.FAVORITE,label="Favoritos"),
            ft.NavigationBarDestination(icon=ft.icons.SETTINGS,label="Configuración"),
        ],
        bgcolor=ft.Colors.PURPLE_900,
        selected_index=0,
        on_change=enrutamiento

        
    )
    
    page.add(ft.View(
        controls=[
            vistaPantallaInicio,
            barraNavegacion
        ]
    )   
    )
    #page.views.append(vistaPantallaInicio(page))


ft.app(main)
