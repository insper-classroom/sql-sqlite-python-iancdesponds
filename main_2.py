from db.db_utils import *
import sqlite3


# Exercício de Python - Sqlite

tabela = Database('db/database_alunos.db', 'Alunos', 'ID INTEGER PRIMARY KEY AUTOINCREMENT, Nome TEXT NOT NULL, Curso TEXT NOT NULL, Ano_de_Ingresso INTEGER', 'Nome, Curso, Ano_de_Ingresso')
tabela.drop_table() # Só funciona se já tiver criado a tabela
tabela.criar_tabela()
estudantes=[
('Ana Silva', 'Computação', 2019),
('Pedro Mendes', 'Física', 2021),
('Carla Souza', 'Computação', 2020),
('João Alves', 'Matemática', 2018),
('Maria Oliveira', 'Química', 2022)
]
tabela.inserir_dados(estudantes)
tabela.ler_dados('*', f'Ano_de_Ingresso IN (2019, 2020)')
tabela.atualizar_dados('Ano_de_Ingresso', 2023, 'Curso = "Química"')
tabela.deletar_dados('ID = 4')
tabela.ler_dados('*', "Ano_de_Ingresso>2019 AND Curso='Computação'")
tabela.atualizar_dados('Ano_de_Ingresso','2018', '"Computação"')
tabela.ler_dados('*','')