import flet as ft
import atletas
def mostrar_pagina_inicial(page):
    page.clean()
    page.add(
        ft.Column([
            ft.Text("Bem-vindo ao sistema de análise de judô!", size=30),
            ft.ElevatedButton("Registrar Atleta", on_click=lambda e: atletas.mostrar_cadastro_atleta(page)),
            # Você pode adicionar outros botões ou informações aqui
        ])
    )