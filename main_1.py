import sqlite3

# Exercício de Python - Sqlite

# Conexão com o banco de dados dentro da pasta "db"
conn = sqlite3.connect('db/database_alunos.db')
cursor = conn.cursor()

cursor.execute("""
DROP TABLE Estudantes;
""")
# Vamos criar uma tabela chamada "Estudantes" com os seguintes campos:
# ID (chave primária) -  Criado automáticamente pela base de dados
# Nome
# Curso
# Ano de Ingresso

cursor.execute("""
CREATE TABLE IF NOT EXISTS Estudantes (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Nome TEXT NOT NULL,
    Curso TEXT NOT NULL,
    Ano_de_Ingresso INTEGER
);
""")

estudantes=[
('Ana Silva', 'Computação', 2019),
('Pedro Mendes', 'Física', 2021),
('Carla Souza', 'Computação', 2020),
('João Alves', 'Matemática', 2018),
('Maria Oliveira', 'Química', 2022)
]

cursor.executemany("""
INSERT INTO Estudantes (Nome, Curso, Ano_de_Ingresso)
VALUES (?, ?, ?);
""", estudantes)

conn.commit()

cursor.execute("SELECT * FROM Estudantes WHERE Ano_de_Ingresso IN (2019, 2020)")
print(cursor.fetchall())

cursor.execute("UPDATE Estudantes SET Ano_de_Ingresso = ? WHERE Curso = ? ", (2023,'Química'))
conn.commit()

cursor.execute("DELETE FROM Estudantes WHERE ID = ?", (4,))
conn.commit()

cursor.execute("SELECT * FROM Estudantes WHERE Ano_de_Ingresso>2019 AND Curso='Computação' ")
print(cursor.fetchall())

cursor.execute("UPDATE Estudantes SET Ano_de_Ingresso = ? WHERE Curso = ?", (2018, "Computação"))
conn.commit()

cursor.execute("SELECT * FROM Estudantes")
print(cursor.fetchall())

conn.close()