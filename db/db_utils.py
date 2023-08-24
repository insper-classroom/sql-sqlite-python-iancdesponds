import sqlite3

def inicialização(nome_database, nome_tabela):
    # Conexão com o banco de dados dentro da pasta "db"
    conn = sqlite3.connect(nome_database)
    cursor = conn.cursor()
    cursor.execute(f"""
DROP TABLE {nome_tabela};
""")
    
def criar_tabela(nome_tabela, colunas, )