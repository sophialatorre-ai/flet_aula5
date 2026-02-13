import flet as ft

def main(page: ft.Page):
    mensagem = ft.Text("Escolha a opção correta!")
    resposta_correta = "Bob Esponja"

    def verificar_resposta(e):
        if e.control.content == resposta_correta:
            mensagem.value = "Parabéns!!"
        else:
            mensagem.value = "Resposta errada"
        page.update()

    page.title = "Game: Adivinhe a imagem"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.bgcolor ="#f8fbc1"

    page.add(
        ft.Column(
            controls=[
                ft.Text(
                    "Adivinhe a Imagem",
                    size=24,
                    weight="bold",
                    color="#000000"
                    
                ),
                ft.Image(
                    src="images/bob.jpg",
                    height=200,
                    border_radius= 30
                ),
                ft.Row(
                    controls=[ 
                        ft.Button(
                            content="Bob Esponja",
                            on_click=verificar_resposta,
                            bgcolor="#e0d370",
                            color="#706510"
                           

                          ),
                          
                        ft.Button(
                            content="Patrick ",
                            on_click=verificar_resposta,
                            bgcolor="#e0d370",
                            color="#706510"
                            
                            
                          ),
                          
                        ft.Button(
                            content="Lula ",
                            on_click=verificar_resposta,
                            bgcolor="#e0d370",
                            color="#706510"
                            

                          ),
                          
                    ],
                    alignment = ft.MainAxisAlignment.CENTER
                ),
                mensagem 
            ],
            horizontal_alignment = ft.CrossAxisAlignment.CENTER
        
        )
    )

ft.run(main)