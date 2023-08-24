import sqlite3

class Database:
    def __init__(self, nome_database, nome_tabela, str_colunas, colunas):
        self.nome_database = nome_database # Nome do arquivo de banco de dados
        self.nome_tabela = nome_tabela # Nome da tabela
        self.str_colunas = str_colunas # Lista com nomes e tipos de dados das colunas
        self.colunas = colunas # Str com nomes das colunas

    def criar_tabela(self):
        conn = sqlite3.connect(self.nome_database) # Conectar ao banco de dados
        cursor = conn.cursor() # Criar cursor para executar comandos SQL
        
        cursor.execute(f"""
                        CREATE TABLE IF NOT EXISTS {self.nome_tabela} (
                        {self.str_colunas}
                        );
                        """) # Criar tabela
        conn.commit() # Salvar alterações
        conn.close() # Fechar conexão com o banco de dados

    def inserir_dados(self, dados): # dados é uma tupla com os dados a serem inseridos
        
        conn = sqlite3.connect(self.nome_database) # Conectar ao banco de dados
        cursor = conn.cursor() # Criar cursor para executar comandos SQL
        interrogacao = len(dados[0])*'?,'
        interrogacao = interrogacao[:-1]

        cursor.executemany(f"""
        INSERT INTO {self.nome_tabela} ({self.colunas})
        VALUES ({interrogacao});
        """, dados) # Inserir dados
        conn.commit() # Salvar alterações
        conn.close() # Fechar conexão com o banco de dados

    def ler_dados(self, parametro_select, where):
        # parametro_select é o que será selecionado na query
        # where são as condições do filtro - ex: "ID = 1"
        conn = sqlite3.connect(self.nome_database) # Conectar ao banco de dados
        cursor = conn.cursor() # Criar cursor para executar comandos SQL
        if where == None or where == '': # Se não houver filtro
            cursor.execute(f"SELECT {parametro_select} FROM {self.nome_tabela}")
        else: # Se houver filtro
            cursor.execute(f"SELECT {parametro_select} FROM {self.nome_tabela} WHERE {where}")
        conn.commit()
        print(cursor.fetchall()) # Ler dados
        conn.close() # Fechar conexão com o banco de dados
    
    def atualizar_dados(self, coluna, valor, where):
        
        # coluna é a coluna que será atualizada
        # valor é o novo valor que será inserido
        # where são as condições do filtro - ex: "ID = 1"
        conn = sqlite3.connect(self.nome_database) # Conectar ao banco de dados
        cursor = conn.cursor() # Criar cursor para executar comandos SQL
        cursor.execute(f"UPDATE {self.nome_tabela} SET {coluna} = {str(valor)} WHERE {where}") # Atualizar dados
        conn.commit() # Salvar alterações
        conn.close() # Fechar conexão com o banco de dados

    def deletar_dados(self, where):
        
        # where são as condições do filtro - ex: "ID = 1"
        conn = sqlite3.connect(self.nome_database) # Conectar ao banco de dados
        cursor = conn.cursor() # Criar cursor para executar comandos SQL
        cursor.execute(f"DELETE FROM {self.nome_tabela} WHERE {where}") # Deletar dados
        conn.commit() # Salvar alterações
        conn.close() # Fechar conexão com o banco de dados

    def drop_table(self): # Deleta a tabela e cria uma nova
        conn = sqlite3.connect(self.nome_database) # Conectar ao banco de dados
        cursor = conn.cursor() # Criar cursor para executar comandos SQL
        cursor.execute(f"""
                       DROP TABLE {self.nome_tabela};
                       """) # Apagar tabela se ela já existir
        conn.commit() # Salvar alterações
        conn.close() # Fechar conexão com o banco de dados
        self.criar_tabela()