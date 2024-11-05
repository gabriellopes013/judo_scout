# cadastro.py
import flet as ft
import datetime
from database import salvar_analista

def mostrar_cadastro(page):
    page.clean()
    page.add(ft.Text("Cadastro de Analista", size=30))

    cpf_input = ft.TextField(label="CPF (único)", width=300)
    nome_input = ft.TextField(label="Nome", width=300)
    clube_input = ft.TextField(label="Clube", width=300)
    funcao_input = ft.TextField(label="Função", width=300)
    data_nascimento_text = ft.Text("Data de Nascimento: ", size=15)
    senha_input = ft.TextField(label="Senha", width=300, password=True)
    confirmar_senha_input = ft.TextField(label="Confirmar Senha", width=300, password=True)

    # Função para abrir o DatePicker e atualizar o campo de data
    def abrir_datepicker(e):
        page.open(
            ft.DatePicker(
                first_date=datetime.datetime(year=1900, month=1, day=1),
                last_date=datetime.datetime(year=2050, month=12, day=31),
                on_change=atualizar_data_nascimento,
                on_dismiss=lambda e: page.add(ft.Text("DatePicker dismissed"))
            )
        )

    # Função para atualizar o texto da data selecionada
    def atualizar_data_nascimento(e):
        data_nascimento_text.value = f"Data de Nascimento: {e.control.value.strftime('%d/%m/%Y')}"
        page.update()
        
    def cadastrar(e):
        cpf = cpf_input.value
        nome = nome_input.value
        clube = clube_input.value
        funcao = funcao_input.value
        data_nascimento = data_nascimento_text.value.split(": ")[1]  # Extrai a data formatada
        senha = senha_input.value
        confirmar_senha = confirmar_senha_input.value

        # Aqui você deve implementar a lógica para cadastrar o analista no banco de dados
        if senha == confirmar_senha:
            salvar_analista(cpf, nome, clube, funcao, data_nascimento, senha)
            page.add(ft.Text("Analista cadastrado com sucesso!", color=ft.colors.GREEN))
        else:
            page.add(ft.Text("As senhas não coincidem!", color=ft.colors.RED))
        
    def voltar(e):
        from login import mostrar_login
        mostrar_login(page, None)
        
    # Botão para abrir o DatePicker
    data_nascimento_botao = ft.ElevatedButton("Selecionar Data de Nascimento", on_click=abrir_datepicker)
    
    cadastrar_botao = ft.ElevatedButton("Cadastrar", on_click=cadastrar)
    voltar_botao = ft.ElevatedButton("Voltar", on_click=voltar)
    # Adicionar todos os campos e botões ao layout
    page.add(
        cpf_input, 
        nome_input, 
        clube_input, 
        funcao_input, 
        data_nascimento_text, 
        data_nascimento_botao, 
        senha_input, 
        confirmar_senha_input,
        cadastrar_botao,
        voltar_botao)
    