# database.py
import sqlite3
import bcrypt

def inicializar_db():
    # Conecta ao banco de dados (cria se não existir)
    conn = sqlite3.connect("analise_judo.db")
    cursor = conn.cursor()

    # Criação da tabela de analistas
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS analistas (
        cpf TEXT PRIMARY KEY,
        nome TEXT,
        clube TEXT,
        funcao TEXT,
        data_nascimento TEXT,
        senha_hash TEXT
    )
    ''')

    # Criação da tabela de atletas
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS atletas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT,
        clube TEXT,
        sexo TEXT,
        categoria_peso TEXT,
        categoria_idade TEXT
    )
    ''')

    # Criação da tabela de relação entre analistas e atletas
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS atleta_analista (
        analista_cpf TEXT,
        atleta_id INTEGER,
        FOREIGN KEY (analista_cpf) REFERENCES analistas (cpf),
        FOREIGN KEY (atleta_id) REFERENCES atletas (id),
        PRIMARY KEY (analista_cpf, atleta_id)
    )
    ''')

    conn.commit()
    conn.close()

# Função para salvar um novo analista no banco de dados
def salvar_analista(cpf, nome, clube, funcao, data_nascimento, senha_hash):
    conn = sqlite3.connect("analise_judo.db")
    cursor = conn.cursor()
    
    cursor.execute('''
    INSERT INTO analistas (cpf, nome, clube, funcao, data_nascimento, senha_hash)
    VALUES (?, ?, ?, ?, ?, ?)
    ''', (cpf, nome, clube, funcao, data_nascimento, senha_hash))
    
    conn.commit()
    conn.close()

# Função para salvar um novo atleta no banco de dados
def salvar_atleta(nome, clube, sexo, categoria_peso, data_nascimento):
    conn = sqlite3.connect("analise_judo.db")
    cursor = conn.cursor()

    cursor.execute('''
    INSERT INTO atletas (nome, clube, sexo, categoria_peso, categoria_idade)
    VALUES (?, ?, ?, ?, ?)
    ''', (nome, clube, sexo, categoria_peso, data_nascimento))
    
    atleta_id = cursor.lastrowid  # Obtém o ID do atleta inserido
    conn.commit()
    conn.close()
    
    return atleta_id  # Retorna o ID do atleta

# Função para associar um atleta a um analista
def associar_atleta_a_analista(analista_cpf, atleta_id):
    conn = sqlite3.connect("analise_judo.db")
    cursor = conn.cursor()

    cursor.execute('''
    INSERT INTO atleta_analista (analista_cpf, atleta_id)
    VALUES (?, ?)
    ''', (analista_cpf, atleta_id))
    
    conn.commit()
    conn.close()

# Função para obter todos os atletas de um analista
def obter_atletas_por_analista(analista_cpf):
    conn = sqlite3.connect("analise_judo.db")
    cursor = conn.cursor()

    cursor.execute('''
    SELECT a.nome, a.clube, a.sexo, a.categoria_peso 
    FROM atletas a
    JOIN atleta_analista aa ON a.id = aa.atleta_id
    WHERE aa.analista_cpf = ?
    ''', (analista_cpf,))
    
    atletas = cursor.fetchall()
    conn.close()
    return atletas

def cadastrar_atleta(nome, clube, sexo, categoria_peso, categoria_idade, analista_cpf):
    # Salvar o atleta no banco e obter o ID dele
    atleta_id = salvar_atleta(nome, clube, sexo, categoria_peso, categoria_idade)
    
    # Associar o atleta ao analista que fez o cadastro
    associar_atleta_a_analista(analista_cpf, atleta_id)


def verificar_login(cpf, senha):
    conn = sqlite3.connect('analise_judo.db')
    cursor = conn.cursor()

    cursor.execute("SELECT senha_hash FROM analistas WHERE cpf = ?", (cpf,))
    resultado = cursor.fetchone()
    conn.close()  # Fechar a conexão após a consulta

    if resultado and len(resultado) > 0:  # Verifique se existe um resultado
        senha_armazenada = resultado[0]
        if senha_armazenada == senha:  # Verifica a senha
            return True
    return False

def obter_atletas_por_analista(analista_cpf):
    conn = sqlite3.connect("analise_judo.db")
    cursor = conn.cursor()

    cursor.execute('''
    SELECT a.nome, a.clube, a.sexo, a.categoria_peso, a.categoria_idade
    FROM atletas a
    JOIN atleta_analista aa ON a.id = aa.atleta_id
    WHERE aa.analista_cpf = ?
    ''', (analista_cpf,))
    
    atletas = cursor.fetchall()
    conn.close()
    return atletas
