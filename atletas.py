import flet as ft
from database import salvar_atleta, obter_atletas_por_analista  # Importa as funções do database.py

def mostrar_cadastro_atleta(page, analista_cpf):
    categorias_idade = ["Sub 18", "Sub 21", "Senior"]
    
    categorias_peso = {
        "Sub 18": {
            "Masculino": ["-50 kg", "-55 kg", "-60 kg", "-66 kg", "-73 kg", "-81 kg", "-90 kg", "+90 kg"],
            "Feminino": ["-40 kg", "-44 kg", "-48 kg", "-52 kg", "-57 kg", "-63 kg", "-70 kg", "+70 kg"]
        },
        "Sub 21": {
            "Masculino": ["-60 kg", "-66 kg", "-73 kg", "-81 kg", "-90 kg", "-100 kg", "+100 kg"],
            "Feminino": ["-48 kg", "-52 kg", "-57 kg", "-63 kg", "-70 kg", "-78 kg", "+78 kg"]
        },
        "Senior": {
            "Masculino": ["-60 kg", "-66 kg", "-73 kg", "-81 kg", "-90 kg", "-100 kg", "+100 kg"],
            "Feminino": ["-48 kg", "-52 kg", "-57 kg", "-63 kg", "-70 kg", "-78 kg", "+78 kg"]
        }
    }

    # Componentes de entrada do formulário de cadastro
    nome_input = ft.TextField(label="Nome")
    clube_input = ft.TextField(label="Clube")
    sexo_input = ft.Dropdown(label="Sexo", options=[ft.dropdown.Option("Masculino"), ft.dropdown.Option("Feminino")])
    idade_input = ft.Dropdown(label="Categoria de Idade", options=[ft.dropdown.Option(idade) for idade in categorias_idade])
    peso_input = ft.Dropdown(label="Categoria de Peso")

    # Função para atualizar categorias de peso com base na idade e no sexo
    def atualizar_peso(e):
        idade = idade_input.value
        sexo = sexo_input.value
        if idade and sexo:
            peso_input.options = [ft.dropdown.Option(peso) for peso in categorias_peso[idade][sexo]]
            peso_input.update()

    # Atualiza a lista de categorias de peso quando idade ou sexo são alterados
    idade_input.on_change = atualizar_peso
    sexo_input.on_change = atualizar_peso

    # Função de callback para o botão de cadastro
    def on_cadastrar_click(e):
        nome = nome_input.value
        clube = clube_input.value
        sexo = sexo_input.value
        idade = idade_input.value
        peso = peso_input.value

        # Verifica se todos os campos foram preenchidos
        if nome and clube and sexo and idade and peso:
            atleta_id = salvar_atleta(nome, clube, sexo, idade, peso)  # Chama a função de cadastro no banco
            page.snack_bar = ft.SnackBar(ft.Text("Atleta cadastrado com sucesso!"), open=True)
            atualizar_lista_atletas()  # Atualiza a lista de atletas após cadastro
        else:
            page.snack_bar = ft.SnackBar(ft.Text("Por favor, preencha todos os campos."), open=True)
        page.update()

    # Função para atualizar a lista de atletas do analista
    def atualizar_lista_atletas():
        atletas = obter_atletas_por_analista(analista_cpf)
        tabela_atletas.rows = [
            ft.DataRow(
                cells=[
                    ft.DataCell(ft.Text(atleta[0])),  # Nome
                    ft.DataCell(ft.Text(atleta[1])),  # Clube
                    ft.DataCell(ft.Text(atleta[2])),  # Sexo
                    ft.DataCell(ft.Text(atleta[3])),  # Categoria Peso
                    ft.DataCell(ft.Text(atleta[4])),  # Categoria Idade
                ]
            ) for atleta in atletas
        ]
        tabela_atletas.update()

    # Tabela para exibir a lista de atletas do analista
    tabela_atletas = ft.DataTable(
        columns=[
            ft.DataColumn(label=ft.Text("Nome")),
            ft.DataColumn(label=ft.Text("Clube")),
            ft.DataColumn(label=ft.Text("Sexo")),
            ft.DataColumn(label=ft.Text("Categoria Peso")),
            ft.DataColumn(label=ft.Text("Categoria Idade")),
        ],
        rows=[]
    )

    # Adiciona os componentes à página
    page.add(
        ft.Column(
            controls=[
                ft.Text("Cadastrar Atleta", style="headlineMedium"),
                nome_input,
                clube_input,
                sexo_input,
                idade_input,
                peso_input,
                ft.ElevatedButton("Cadastrar Atleta", on_click=on_cadastrar_click),
                ft.Text("Lista de Atletas Cadastrados", style="headlineSmall"),
                tabela_atletas
            ]
        )
    )

    # Carrega a lista inicial de atletas
    atualizar_lista_atletas()