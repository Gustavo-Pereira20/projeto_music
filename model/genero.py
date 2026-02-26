from database.conexao import conectar

def recuperar_generos():
    conexao, cursor = conectar()

    cursor.execute("SELECT nome_genero, cor, caminho_icone FROM categoria")
    genero = cursor.fetchall()

    conexao.close()

    return genero

def filtrar_generos(a:str) -> list:
    conexao, cursor = conectar()

    cursor.execute("SELECT codigo, cantor, duracao, atividade, nome_musica, caminho_capa, nome_genero FROM musica WHERE nome_genero = %s ORDER BY atividade", (a,))
    musicas = cursor.fetchall()

    conexao.close()

    return musicas