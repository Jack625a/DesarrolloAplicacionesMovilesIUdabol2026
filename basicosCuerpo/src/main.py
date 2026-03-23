import flet as ft

from pantallaInicio import vistaPantallaInicio
from pantallaBuscar import vistaPantallaBuscar
from pantallaConfiguracion import vistaPantallaConfiguracion
from pantallaFavoritos import vistaPantallaFavoritos 


def main(page: ft.Page):
    page.appbar=ft.AppBar(
        title=ft.Text("Componentes Cuerpo"),
        leading=ft.Icon(name='MENU'),
        bgcolor=ft.Colors.PURPLE_900,
        color=ft.Colors.WHITE
    )
    page.bottom_appbar=ft.NavigationBar(
        destinations=[
            ft.NavigationBarDestination(icon=ft.icons.HOME,label="Inicio"),
            ft.NavigationBarDestination(icon=ft.icons.SEARCH,label="Buscar"),
            ft.NavigationBarDestination(icon=ft.icons.FAVORITE,label="Favoritos"),
            ft.NavigationBarDestination(icon=ft.icons.SETTINGS,label="Configuración"),
        ],
        bgcolor=ft.Colors.PURPLE_900,
        
    )
    #Funcion para el enrutamiento
    def enrutamiento(e):
        inicio=page.bottom_appbar._id
        if inicio==0:
            page.views.append(vistaPantallaInicio(page))
        elif inicio==1:
            page.views.append(vistaPantallaBuscar(page))
        elif inicio==3:
            page.views.append(vistaPantallaFavoritos(page))
        elif inicio==4:
            page.views.append(vistaPantallaConfiguracion)(page)
    
    page.add(
        
        
    )


ft.app(main)
