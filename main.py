# main.py
import flet as ft
from login import mostrar_login
from database import inicializar_db

def main(page: ft.Page):
    inicializar_db()  # Inicializa o banco de dados

    def on_login(cpf):
        page.clean()
        page.add(ft.Text(f"Bem-vindo, {cpf}"))

    mostrar_login(page, on_login)

ft.app(main)
