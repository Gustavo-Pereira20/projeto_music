from database.conexao import conectar

def recuperar_musicas():
    conexao, cursor = conectar()

    cursor.execute("SELECT codigo, cantor, duracao, nome_musica, caminho_capa, nome_genero FROM musica")
    musicas = cursor.fetchall()

    conexao.close()

    return musicas

