import flet as ft

def vistaPantallaInicio():
    return ft.View(
        controls=[
            ft.Image(src="https://static.vecteezy.com/system/resources/thumbnails/012/047/870/small/trendy-minimalistic-food-delivery-service-or-online-food-order-application-banner-design-template-with-smartphone-screen-and-delivery-scooter-or-it-illustration-free-vector.jpg",
                 border_radius=ft.BorderRadius(top_left=20,top_right=20,bottom_left=20,bottom_right=20),
                 height=200,
                 width=800,
                 fit=ft.ImageFit.COVER
                 ),
        ft.Text(value="Mi aplicación",
                size=25,
                color=ft.Colors.PURPLE_900,
                weight=ft.FontWeight.BOLD
                ),
        ft.ListView(
            spacing=10,
            expand=1,
            controls=[
                ft.ListTile(title=ft.Text("Opcion 1",size=18,weight=ft.FontWeight.BOLD),
                            subtitle=ft.Text("Subtitulo 1"),
                            bgcolor=ft.Colors.GREY_200,
                            leading=ft.Image(src="https://static.vecteezy.com/system/resources/thumbnails/012/047/870/small/trendy-minimalistic-food-delivery-service-or-online-food-order-application-banner-design-template-with-smartphone-screen-and-delivery-scooter-or-it-illustration-free-vector.jpg",
                                             border_radius=ft.BorderRadius(top_left=30,top_right=30,bottom_left=30,bottom_right=30)
                                             ),            
                            ),
                ft.ListTile(title=ft.Text("Opcion 2",size=18,weight=ft.FontWeight.BOLD),
                            subtitle=ft.Text("Subtitulo 2"),
                            bgcolor=ft.Colors.GREY_200,
                            leading=ft.Image(src="https://static.vecteezy.com/system/resources/thumbnails/012/047/870/small/trendy-minimalistic-food-delivery-service-or-online-food-order-application-banner-design-template-with-smartphone-screen-and-delivery-scooter-or-it-illustration-free-vector.jpg",
                                             border_radius=ft.BorderRadius(top_left=30,top_right=30,bottom_left=30,bottom_right=30)
                                             ),            
                            ),
                ft.ListTile(title=ft.Text("Opcion 3",size=18,weight=ft.FontWeight.BOLD),
                            subtitle=ft.Text("Subtitulo 3"),
                            bgcolor=ft.Colors.GREY_200,
                            leading=ft.Image(src="https://static.vecteezy.com/system/resources/thumbnails/012/047/870/small/trendy-minimalistic-food-delivery-service-or-online-food-order-application-banner-design-template-with-smartphone-screen-and-delivery-scooter-or-it-illustration-free-vector.jpg",
                                             border_radius=ft.BorderRadius(top_left=30,top_right=30,bottom_left=30,bottom_right=30)
                                             ),            
                            ),
                ft.ListTile(title=ft.Text("Opcion 4",size=18,weight=ft.FontWeight.BOLD),
                            subtitle=ft.Text("Subtitulo 4"),
                            bgcolor=ft.Colors.GREY_200,
                            leading=ft.Image(src="https://static.vecteezy.com/system/resources/thumbnails/012/047/870/small/trendy-minimalistic-food-delivery-service-or-online-food-order-application-banner-design-template-with-smartphone-screen-and-delivery-scooter-or-it-illustration-free-vector.jpg",
                                             border_radius=ft.BorderRadius(top_left=30,top_right=30,bottom_left=30,bottom_right=30)
                                             ),            
                            ),

                ft.ListTile(title=ft.Text("Opcion 5",size=18,weight=ft.FontWeight.BOLD),
                            subtitle=ft.Text("Subtitulo 5"),
                            bgcolor=ft.Colors.GREY_200,
                            leading=ft.Image(src="https://static.vecteezy.com/system/resources/thumbnails/012/047/870/small/trendy-minimalistic-food-delivery-service-or-online-food-order-application-banner-design-template-with-smartphone-screen-and-delivery-scooter-or-it-illustration-free-vector.jpg",
                                             border_radius=ft.BorderRadius(top_left=30,top_right=30,bottom_left=30,bottom_right=30)
                                             ),            
                            ),
                ft.ListTile(title=ft.Text("Opcion 6",size=18,weight=ft.FontWeight.BOLD),
                            subtitle=ft.Text("Subtitulo 6"),
                            bgcolor=ft.Colors.GREY_200,
                            leading=ft.Image(src="https://static.vecteezy.com/system/resources/thumbnails/012/047/870/small/trendy-minimalistic-food-delivery-service-or-online-food-order-application-banner-design-template-with-smartphone-screen-and-delivery-scooter-or-it-illustration-free-vector.jpg",
                                             border_radius=ft.BorderRadius(top_left=30,top_right=30,bottom_left=30,bottom_right=30)
                                             ),            
                            ),
                            
            ]
        ),
        ]
    )