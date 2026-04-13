import flet as ft


def main(page: ft.Page):
    #Componentes Interfaz
    #Formulario (tipos de entrada)
    nombre=ft.TextField(
        keyboard_type=ft.KeyboardType.NAME,
        icon=ft.Icons.PERSON,
    )
    contraseña=ft.TextField(
        icon=ft.Icons.PASSWORD,
        password=True,
        can_reveal_password=True
    )
    numero=ft.TextField(
        keyboard_type=ft.KeyboardType.NUMBER,
        icon=ft.Icons.NUMBERS
    )
    opciones=ft.DatePicker(
        open=True,
        date_picker_mode=ft.DatePickerMode.DAY
        )
    
    hora=ft.TimePicker(
        open=True,
        time_picker_entry_mode=ft.TimePickerEntryMode.DIAL_ONLY
    )

    archivos=ft.FilePicker(
        on_result=ft.FilePickerResultEvent

    )


    botonEnviar=ft.FilledButton(text="Enviar")

    page.add(
        nombre,
        contraseña,
        numero,
         opciones,
        hora,
        #archivos,
        botonEnviar
    )


ft.app(main)
