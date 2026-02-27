from database.conexao import conectar

def recuperar_generos():
    conexao, cursor = conectar()

    cursor.execute("SELECT nome_genero, cor, caminho_icone FROM categoria")
    genero = cursor.fetchall()

    conexao.close()

    return genero
