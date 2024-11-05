import flet as ft
from database import verificar_login
import cadastro  # Importando o módulo de cadastro para redirecionar
import atletas  # Importando o módulo de atletas para redirecionar
from home import mostrar_pagina_inicial
def mostrar_login(page, on_login):
    page.clean()

    cpf_input = ft.TextField(label="CPF", width=300)
    senha_input = ft.TextField(label="Senha", password=True, width=300)

    def realizar_login(page, cpf, senha):
        if verificar_login(cpf, senha):
            on_login(cpf)
            mostrar_pagina_inicial(page)  # Mostra a página inicial após login
        else:
            page.add(ft.Text("Login falhou. Verifique seu CPF e senha.", color=ft.colors.RED))

    page.add(
        ft.Row([
            ft.Column([
                ft.Text("Login", size=30),
                cpf_input,
                senha_input,
                ft.ElevatedButton("Entrar", on_click=lambda e: realizar_login(page, cpf_input.value, senha_input.value)),
                ft.ElevatedButton("Cadastrar Analista", on_click=lambda e: cadastro.mostrar_cadastro(page))
            ], alignment=ft.MainAxisAlignment.CENTER),
            ft.VerticalDivider()
        ])
    )
