import flet as ft #importacion del framework


def main(page: ft.Page): #funcion principal
    #APPBAR 1
    page.appbar=ft.AppBar(
        title=ft.Text("Componentes"),
        bgcolor=ft.Colors.BLUE_900,
        color=ft.Colors.WHITE,
        leading=ft.Icon(name="MENU")
        )
    page.bottom_appbar=ft.NavigationBar(
        destinations=[
            ft.NavigationBarDestination(label="Inicio",icon=ft.Icons.HOME),
            ft.NavigationBarDestination(label="Productos",icon=ft.Icons.STORE),
            ft.NavigationBarDestination(label="Perfil",icon=ft.Icons.PERSON_2),
            ft.NavigationBarDestination(label="Notificaciones",icon=ft.Icons.NOTIFICATIONS)
        ],
        bgcolor=ft.Colors.LIGHT_GREEN_ACCENT_200,
        indicator_color=ft.Colors.YELLOW,
        surface_tint_color=ft.Colors.WHITE
        
    )
    
    page.add( #interfaz de ususario
       
    )


ft.app(main)
