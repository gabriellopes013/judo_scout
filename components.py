# components.py
import flet as ft

def criar_lista_atletas(atletas):
    lista_componentes = [ft.Row([ft.Text("Nome"), ft.Text("Clube"), ft.Text("Sexo"), ft.Text("Categoria de Peso")], alignment="spaceAround")]
    for atleta in atletas:
        nome, clube, sexo, categoria_peso = atleta
        lista_componentes.append(
            ft.Row([
                ft.Text(nome),
                ft.Text(clube),
                ft.Text(sexo),
                ft.Text(categoria_peso)
            ], alignment="spaceAround")
        )
    return lista_componentes
